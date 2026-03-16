# Video a PDF — Transcriptor de YouTube

Aplicación en **Python** que permite **transcribir videos de YouTube** y generar un documento en **PDF o HTML** a partir de los subtítulos automáticos del video.

---

# Características

* Transcribe videos de **YouTube**
* Usa **subtítulos automáticos (auto-subs)**
* Genera documentos en **PDF o HTML**
* Permite elegir el **idioma de los subtítulos**
* Compatible con **Linux, Mac y Windows**

---

# Requisitos

### Python

* Python **3.8 o superior**

### Dependencias del sistema

* **pandoc** (para generar PDF o HTML)

Opcional para PDF:

* **LaTeX (texlive)**
  o
* **wkhtmltopdf**

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/video-a-pdf.git
cd video-a-pdf
```

---

## 2. Crear entorno virtual

```bash
python3 -m venv venv
```

---

## 3. Activar entorno virtual

Linux / Mac

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## 4. Instalar dependencias

```bash
pip install yt-dlp[curl_cffi]
```

---

# Uso

```bash
python video_a_pdf.py "URL_YOUTUBE" -o salida.html --html -l es
```

---

# Opciones disponibles

| Opción            | Descripción                                      |
| ----------------- | ------------------------------------------------ |
| `-o`, `--output`  | Archivo de salida (default: `transcripcion.pdf`) |
| `-l`, `--lang`    | Idioma de subtítulos (default: `es`)             |
| `-v`, `--verbose` | Mostrar información detallada                    |
| `--html`          | Generar HTML en lugar de PDF                     |

---

# Ejemplos

### Transcripción básica (español)

```bash
python video_a_pdf.py "https://www.youtube.com/watch?v=2gO8WyctqMk&t=10s" -o transcripcion.html --html
```
python3 scripts/video_a_pdf.py "https://www.youtube.com/watch?v=pFyAu4R684s"  


---

### Transcripción en inglés

```bash
python video_a_pdf.py "URL_VIDEO" -l en -o salida.html --html
```

---

# Dependencias

## Python (entorno virtual)

* certifi
* cffi
* curl_cffi
* pycparser
* yt-dlp

---

## Sistema

* pandoc

---

# Notas

* Por defecto se utilizan **subtítulos automáticos de YouTube**
* Para generar **PDF reales**, es necesario instalar:

  * **LaTeX (texlive)**
    o
  * **wkhtmltopdf**
* Alternativamente se puede usar la opción `--html` para generar un archivo HTML.

---

---
FastAPI

uvicorn app.main:app --reload  -- Iniciar app
source venv/bin/activate

-----

-----
REACT

Iniciamos proyecto con VITE
npm create vite@latest frontend  
correr el front  --- npm run dev

----


# Licencia

MIT
