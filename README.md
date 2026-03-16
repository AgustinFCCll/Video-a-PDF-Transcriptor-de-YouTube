# Video a PDF - Transcriptor de YouTube

Convierte videos de YouTube en documentos PDF o HTML usando subtítulos automáticos.

## Características

- Extracción de subtítulos de videos de YouTube
- Generación de documentos PDF o HTML
- Soporte múltiples idiomas (Español, Inglés, Portugués, Francés, Alemán)
- Interfaz moderna con diseño glassmorphism (frontend)
- API REST con FastAPI

## Tech Stack

- **Backend**: FastAPI + Python
- **Video Processing**: yt-dlp
- **Document Generation**: Pandoc
- **Frontend**: React + Vite (en carpeta `frontend/`)

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

## Instalación

```bash
# Clonar repositorio
git clone https://github.com/AgustinFCCll/Video-a-PDF-Transcriptor-de-YouTube.git
cd Video-a-PDF-Transcriptor-de-YouTube

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
# Iniciar servidor
uvicorn main:app --reload

# O ejecutar directamente
python main.py
```

El backend estará disponible en: `http://localhost:8000`

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

```bash
curl -X POST http://localhost:8000/convert \
  -H "Content-Type: application/json" \
  -d '{"url": "https://youtube.com/watch?v=...", "lang": "es", "as_html": false}'
```

## Licencia

MIT
