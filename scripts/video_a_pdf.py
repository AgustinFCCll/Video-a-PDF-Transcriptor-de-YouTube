#!/usr/bin/env python3
import argparse
import subprocess
import sys
import os
import tempfile
import re
import time


def extract_video_id(url: str) -> str:
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'(?:embed\/)([0-9A-Za-z_-]{11})',
        r'(?:youtu\.be\/)([0-9A-Za-z_-]{11})'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError("URL de YouTube inválida")


def get_video_title(url: str) -> str:
    cmd = ['yt-dlp', '--no-download', '--print', '%(title)s', url]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode == 0:
        title = result.stdout.strip()
        title = re.sub(r'[^\w\s\-]', '', title)
        title = re.sub(r'\s+', '_', title)
        return title[:100]
    return "transcripcion"


def get_subtitles(url: str, lang: str = "es", use_auto: bool = True) -> str:
    with tempfile.TemporaryDirectory() as work_dir:
        cmd = [
            'yt-dlp',
            '--skip-download',
            '--write-auto-subs',
            '--sub-lang', lang,
            '--output', os.path.join(work_dir, 'subs'),
        ]
        
        cmd.append(url)
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        subtitle_files = [
            f for f in os.listdir(work_dir) 
            if f.endswith('.srt') or f.endswith('.vtt')
        ]
        
        if not subtitle_files:
            raise RuntimeError(f"No se encontraron subtítulos en {lang}. "
                               f"Puede que el video no tenga subtitulos automaticos en este idioma")
        
        subtitle_file = os.path.join(work_dir, subtitle_files[0])
        
        with open(subtitle_file, 'r', encoding='utf-8') as f:
            return f.read()


def srt_to_markdown(srt_content: str) -> str:
    import re
    lines = srt_content.strip().split('\n')
    result = []
    seen_lines = set()
    
    is_vtt = lines[0].strip().startswith('WEBVTT')
    
    i = 0
    if is_vtt:
        while i < len(lines) and '-->' not in lines[i]:
            i += 1
    
    while i < len(lines):
        line = lines[i].strip()
        
        if '-->' in line:
            i += 1
            while i < len(lines) and lines[i].strip() and '-->' not in lines[i]:
                text = lines[i].strip()
                text = re.sub(r'<[^>]+>', '', text)
                text = re.sub(r'^[A-Z][a-z]+\s+', '', text)
                text = text.strip()
                
                if text and text not in seen_lines:
                    result.append(text)
                    seen_lines.add(text)
                i += 1
            result.append('')
        elif line.isdigit():
            i += 1
        else:
            i += 1
    
    return '\n'.join(result).strip()


def generate_pdf(markdown_content: str, output_path: str, as_html: bool = False, title: str = None) -> str:
    if title is None:
        title = "Transcripcion"
    markdown_content = f"---\ntitle: \"{title}\"\n---\n\n{markdown_content}"
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(markdown_content)
        temp_md = f.name
    
    try:
        cmd = None
        if as_html:
            cmd = ['pandoc', '-s', '-o', output_path, temp_md]
            subprocess.run(cmd, check=True, capture_output=True, timeout=30)
            return output_path
        else:
            engines = ['pdflatex', 'xelatex', 'wkhtmltopdf']
            last_error = None
            result = None
            
            for engine in engines:
                if engine == 'wkhtmltopdf':
                    cmd = ['pandoc', temp_md, '-o', output_path, '--pdf-engine', engine]
                else:
                    cmd = ['pandoc', temp_md, '-o', output_path]
                
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                
                if result.returncode == 0:
                    break
                
                last_error = result.stderr
            
            if not result or result.returncode != 0:
                print(f"ADVERTENCIA: No se encontró motor PDF. Generando HTML en su lugar.", file=sys.stderr)
                html_output = output_path.replace('.pdf', '.html')
                cmd = ['pandoc', '-s', '-o', html_output, temp_md]
                subprocess.run(cmd, check=True, capture_output=True, timeout=30)
                return html_output
            
            subprocess.run(cmd, check=True, capture_output=True, timeout=30)
            return output_path
    finally:
        if os.path.exists(temp_md):
            os.remove(temp_md)


def process_video(url: str, output_path: str = None, lang: str = "es", as_html: bool = False) -> dict:
    import shutil
    
    video_title = get_video_title(url)
    
    if output_path is None:
        output_dir = "outputs"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        ext = ".html" if as_html else ".pdf"
        output_path = os.path.join(output_dir, f"{video_title}{ext}")
    else:
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    srt = get_subtitles(url, lang)
    md = srt_to_markdown(srt)
    output_file = generate_pdf(md, output_path, as_html, title=video_title)
    
    return {
        "output_path": output_file,
        "file_size": os.path.getsize(output_file),
        "file_type": "html" if output_file.endswith('.html') else "pdf"
    }


def main():
    parser = argparse.ArgumentParser(
        description='Transcribe un video de YouTube a PDF',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Ejemplos:
  python3 video_a_pdf.py "https://youtube.com/watch?v=xxx"
  python3 video_a_pdf.py "https://youtu.be/xxx" -o mi_archivo.pdf
  python3 video_a_pdf.py "url" -l en -o salida.pdf
        '''
    )
    parser.add_argument('url', help='URL del video de YouTube')
    parser.add_argument('-o', '--output', default='outputs/transcripcion.pdf', help='Archivo de salida PDF')
    parser.add_argument('-l', '--lang', default='es', help='Idioma de subtítulos (default: es)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Modo verbose')
    parser.add_argument('--auto', action='store_true', help='Usar subtítulos autogenerados si no hay disponibles')
    parser.add_argument('--html', action='store_true', help='Generar HTML en lugar de PDF')
    
    args = parser.parse_args()
    
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if args.html:
        args.output = args.output.replace('.pdf', '.html')
    
    if args.verbose:
        print(f"URL: {args.url}")
        print(f"Idioma: {args.lang}")
        print(f"Output: {args.output}")
    
    print(f"Obteniendo subtítulos en {args.lang}...")
    
    try:
        srt = get_subtitles(args.url, args.lang, args.auto)
    except subprocess.TimeoutExpired:
        print("Error: Timeout al descargar subtítulos", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: yt-dlp no está instalado", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    if not srt.strip():
        print("Error: No se obtuvo contenido de subtítulos", file=sys.stderr)
        sys.exit(1)
    
    print("Convirtiendo a Markdown...")
    md = srt_to_markdown(srt)
    
    if args.verbose:
        print(f"Caracteres Markdown: {len(md)}")
    
    output_file = args.output
    if args.output.endswith('.html'):
        print(f"Generando HTML: {args.output}")
    else:
        print(f"Generando PDF: {args.output}")
    
    try:
        output_file = generate_pdf(md, args.output, args.html)
    except FileNotFoundError:
        print("Error: pandoc no está instalado", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    size = os.path.getsize(output_file)
    ext = "HTML" if output_file.endswith('.html') else "PDF"
    print(f"¡Listo! {ext} generado ({size/1024:.1f} KB): {output_file}")


if __name__ == '__main__':
    main()