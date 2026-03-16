# Video a PDF - Transcriptor de YouTube

Convierte videos de YouTube a documentos PDF o HTML utilizando los subtítulos disponibles.

## Características

- Extracción de subtítulos de videos de YouTube
- Generación de documentos PDF o HTML
- Soporte múltiples idiomas (Español, Inglés, Portugués, Francés, Alemán)
- Interfaz moderna con diseño glassmorphism
- Fondo animado con gradientes y textura noise

## Tech Stack

- **Frontend**: React 19 + Vite
- **Backend**: Python (FastAPI)
- **Estilos**: CSS moderno con glassmorphism

## Requisitos Previos

- Node.js 18+
- Python 3.8+
- pip

## Instalación

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## Uso

1. Inicia el backend en `http://localhost:8000`
2. Inicia el frontend en `http://localhost:5173`
3. Ingresa la URL de un video de YouTube
4. Selecciona el idioma de los subtítulos
5. Elige el formato de salida (PDF o HTML)
6. Haz clic en "Convertir" y descarga el resultado

## Estructura del Proyecto

```
Video-a-PDF-Transcriptor-de-YouTube/
├── frontend/           # Aplicación React
│   ├── src/
│   │   ├── App.jsx     # Componente principal
│   │   ├── App.css     # Estilos
│   │   └── index.css   # Estilos globales
│   └── index.html
├── backend/            # API FastAPI
│   └── main.py
└── README.md
```

## Capturas

La aplicación cuenta con:
- Diseño moderno con efecto glassmorphism
- Fondo con gradientes multicolores y textura noise
- Botones stilizados con efectos hover
- Inputs con estilos transparentes y bordes sutiles

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

## Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios.

## Licencia

MIT
