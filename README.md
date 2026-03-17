# Video a PDF - Transcriptor de YouTube

Convierte videos de YouTube en documentos PDF o HTML usando subtítulos automáticos.

## Características

- Extracción de subtítulos de videos de YouTube
- Generación de documentos PDF o HTML
- Soporte múltiples idiomas (Español, Inglés, Portugués, Francés, Alemán)
- Interfaz moderna con diseño responsive y efectos visuales
- API REST con FastAPI
- Compatible con Windows y Linux

## Imagen

<img width="1300" height="688" alt="Captura desde 2026-03-16 20-48-11" src="https://github.com/user-attachments/assets/776ebbdd-11aa-4174-8db1-576d7c2fdd98" />


## Tech Stack

- **Backend**: FastAPI + Python
- **Video Processing**: yt-dlp
- **Document Generation**: Pandoc
- **Frontend**: React + Vite + Tailwind CSS

## Estructura del Proyecto (Arquitectura Limpia)

```
Video-a-PDF-Transcriptor-de-YouTube/
├── app/
│   ├── core/              # Configuración central
│   │   └── __init__.py   # CORS, settings
│   ├── models/            # Modelos de datos
│   │   └── request_models.py
│   ├── routes/            # Endpoints de API
│   │   └── transcribe.py
│   └── services/         # Lógica de negocio
│       └── video_service.py
├── main.py               # Punto de entrada
├── tests/                # Tests
├── requirements.txt      # Dependencias Python
├── frontend/             # Aplicación React
└── README.md
```

## Requisitos Previos

- Python 3.8+
- Node.js 18+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (se instala automáticamente)
- [Pandoc](https://pandoc.org/) - Para generación de PDF/HTML

### Instalación de Pandoc

**Windows:**
```powershell
# Usando winget
winget install JohnMacFarlane.Pandoc

# O descargar desde: https://github.com/jgm/pandoc/releases/tag/3.9
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt install pandoc
```

**Linux (Arch):**
```bash
sudo pacman -S pandoc
```

**macOS:**
```bash
brew install pandoc
```

## Instalación

```bash
# Clonar repositorio
git clone https://github.com/AgustinFCCll/Video-a-PDF-Transcriptor-de-YouTube.git
cd Video-a-PDF-Transcriptor-de-YouTube

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
# .venv\Scripts\activate  # Windows/PowerShell

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución

### Backend

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Iniciar servidor con uvicorn (recomendado)
uvicorn main:app --reload

# O ejecutar directamente
python main.py
```

El backend estará disponible en: `http://localhost:8000`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

El frontend estará disponible en: `http://localhost:5173`

## Comandos completos

### Linux/Mac
```bash
cd /ruta/al/proyecto
source venv/bin/activate
uvicorn main:app --reload

# En otra terminal
cd frontend
npm install
npm run dev
```

### Windows
```bash
cd C:\ruta\al\proyecto
venv\Scripts\activate
uvicorn main:app --reload

# En otra terminal
cd frontend
npm install
npm run dev
```

## Tests

```bash
pytest tests/ -v
```

## API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/convert` | Convierte video a PDF/HTML |
| GET | `/download/{filename}` | Descarga archivo generado |
| GET | `/health` | Estado de la API |
| GET | `/` | Información de la API |

## Ejemplo de uso

### cURL
```bash
curl -X POST http://localhost:8000/convert \
  -H "Content-Type: application/json" \
  -d '{"url": "https://youtube.com/watch?v=...", "lang": "es", "as_html": false}'
```

### Request body
```json
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "lang": "es",
  "as_html": false
}
```

### Parámetros
- `url` (required): URL del video de YouTube
- `lang` (optional): Idioma de subtítulos (es, en, pt, fr, de). Por defecto: "es"
- `as_html` (optional): Generar HTML en lugar de PDF. Por defecto: false

### Response
```json
{
  "success": true,
  "message": "PDF generado exitosamente",
  "file_path": "outputs/titulo_video.pdf",
  "file_size": 12345
}
```

## Solución de problemas

### Error: "No se encontraron subtítulos"
- Verifica que el video tenga subtítulos automáticos
- Intenta con otro idioma

### Error: "No se encontró motor PDF"
- Instala Pandoc correctamente
- O usa la opción `as_html: true` para generar HTML en lugar de PDF

### Error de CORS en desarrollo
- Asegúrate de tener el backend corriendo en localhost:8000
- El proxy de Vite está configurado para reenviar las peticiones

## Licencia

MIT
