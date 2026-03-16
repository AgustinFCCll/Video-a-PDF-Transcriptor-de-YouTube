# Video a PDF - Transcriptor de YouTube

Convierte videos de YouTube en documentos PDF o HTML utilizando los subtítulos automáticos disponibles.

## Características

- Extracción de subtítulos de videos de YouTube
- Generación de documentos PDF o HTML
- Soporte múltiples idiomas (Español, Inglés, Portugués, Francés, Alemán)
- Interfaz moderna con diseño glassmorphism
- Fondo animado con gradientes multicolores y textura noise

## Tech Stack

### Frontend
- React 19
- Vite
- CSS moderno (glassmorphism)

### Backend
- Python 3.8+
- FastAPI
- yt-dlp (extracción de subtítulos)
- Pandoc (conversión a PDF/HTML)

## Requisitos Previos

- Node.js 18+
- Python 3.8+
- pip
- pandoc (instalar con: `sudo apt install pandoc` o similar)

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/AgustinFCCll/Video-a-PDF-Transcriptor-de-YouTube.git
cd Video-a-PDF-Transcriptor-de-YouTube
```

### Backend

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instalar dependencias
pip install yt-dlp[curl_cffi] fastapi uvicorn python-multipart
```

### Frontend

```bash
cd frontend
npm install
```

## Ejecución

### Iniciar Backend

```bash
cd app
uvicorn main:app --reload
```

El backend estará disponible en: `http://localhost:8000`

### Iniciar Frontend

```bash
cd frontend
npm run dev
```

El frontend estará disponible en: `http://localhost:5173`

## Uso de la Aplicación

1. Inicia el backend en `http://localhost:8000`
2. Inicia el frontend en `http://localhost:5173`
3. Ingresa la URL de un video de YouTube
4. Selecciona el idioma de los subtítulos
5. Elige el formato de salida (PDF o HTML)
6. Haz clic en "Convertir" y descarga el resultado

## Estructura del Proyecto

```
Video-a-PDF-Transcriptor-de-YouTube/
├── app/                    # Backend FastAPI
│   ├── __init__.py
│   ├── main.py             # Punto de entrada
│   ├── routes/             # Rutas de la API
│   │   ├── __init__.py
│   │   └── transcribe.py
│   ├── services/           # Lógica de negocio
│   │   ├── __init__.py
│   │   └── video_service.py
│   └── models/             # Modelos de datos
│       ├── __init__.py
│       └── request_models.py
├── frontend/               # Aplicación React
├── tests/                  # Tests
├── outputs/                # Archivos generados
├── venv/                   # Entorno virtual Python
├── scripts/                # Scripts CLI
├── README.md
└── README.txt
```

## Tests

```bash
# Instalar pytest
pip install pytest httpx

# Ejecutar tests
pytest tests/ -v
```
Video-a-PDF-Transcriptor-de-YouTube/
├── app/                    # Backend FastAPI
│   ├── main.py             # Punto de entrada
│   ├── routes/             # Rutas de la API
│   ├── services/           # Lógica de negocio
│   └── models/             # Modelos de datos
├── frontend/               # Aplicación React
│   ├── src/
│   │   ├── App.jsx        # Componente principal
│   │   ├── App.css        # Estilos
│   │   └── index.css      # Estilos globales
│   ├── index.html
│   └── package.json
├── outputs/                # Archivos generados
├── venv/                  # Entorno virtual Python
├── README.md
└── README.txt             # Documentación legacy
```

## API Endpoints

### `POST /convert`

Convierte un video de YouTube a PDF o HTML.

**Request:**
```json
{
  "url": "https://youtube.com/watch?v=...",
  "lang": "es",
  "as_html": false
}
```

**Response:**
```json
{
  "message": "Video procesado exitosamente",
  "file_path": "/tmp/output.pdf"
}
```

### `GET /download/{filename}`

Descarga el archivo generado.

## Opciones de Línea de Comando (Legacy)

```bash
python scripts/video_a_pdf.py "URL_YOUTUBE" -o salida.html --html -l es
```

| Opción | Descripción |
|--------|-------------|
| `-o`, `--output` | Archivo de salida |
| `-l`, `--lang` | Idioma de subtítulos |
| `--html` | Generar HTML en lugar de PDF |

## Tecnologías Utilizadas

- **yt-dlp**: Extracción de videos y subtítulos de YouTube
- **FastAPI**: Framework web moderno y rápido
- **React**: Biblioteca para interfaces de usuario
- **Vite**: Build tool moderno
- **Pandoc**: Conversión de documentos

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

MIT License - ver el archivo LICENSE para más detalles.
