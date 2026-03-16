import { useState } from 'react'
import './App.css'

function App() {
  const [url, setUrl] = useState('')
  const [lang, setLang] = useState('es')
  const [asHtml, setAsHtml] = useState(false)
  const [status, setStatus] = useState('idle')
  const [message, setMessage] = useState('')
  const [downloadUrl, setDownloadUrl] = useState(null)

  const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!url.trim()) return

    setStatus('loading')
    setMessage('Procesando video...')
    setDownloadUrl(null)

    try {
      const response = await fetch(`${API_URL}/convert`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url, lang, as_html: asHtml })
      })

      const data = await response.json()

      if (response.ok) {
        setStatus('success')
        setMessage(data.message)
        const filename = data.file_path.split('/').pop()
        setDownloadUrl(`${API_URL}/download/${filename}`)
      } else {
        setStatus('error')
        setMessage(data.detail || 'Error al procesar el video')
      }
    } catch {
      setStatus('error')
      setMessage('Error de conexión. ¿El servidor está corriendo?')
    }
  }

  const handleDownload = () => {
    if (downloadUrl) {
      window.open(downloadUrl, '_blank')
    }
  }

  return (
    <div className="container">
      <header className="header">
        <h1>Video a PDF</h1>
        <p>Convierte videos de YouTube a PDF o HTML</p>
      </header>

      <main className="main">
        <form onSubmit={handleSubmit} className="form">
          <div className="form-group">
            <label htmlFor="url">URL del video de YouTube</label>
            <input
              type="text"
              id="url"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="https://youtube.com/watch?v=..."
              disabled={status === 'loading'}
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="lang">Idioma de subtítulos</label>
              <select
                id="lang"
                value={lang}
                onChange={(e) => setLang(e.target.value)}
                disabled={status === 'loading'}
              >
                <option value="es">Español</option>
                <option value="en">Inglés</option>
                <option value="pt">Portugués</option>
                <option value="fr">Francés</option>
                <option value="de">Alemán</option>
              </select>
            </div>

            <div className="form-group checkbox-group">
              <label>
                <input
                  type="checkbox"
                  checked={asHtml}
                  onChange={(e) => setAsHtml(e.target.checked)}
                  disabled={status === 'loading'}
                />
                Generar HTML en lugar de PDF
              </label>
            </div>
          </div>

          <button
            type="submit"
            className={`btn ${status === 'loading' ? 'loading' : ''}`}
            disabled={status === 'loading' || !url.trim()}
          >
            {status === 'loading' ? 'Procesando...' : 'Convertir'}
          </button>
        </form>

        {status !== 'idle' && (
          <div className={`status ${status}`}>
            {status === 'loading' && <div className="spinner"></div>}
            <p>{message}</p>
            {status === 'success' && downloadUrl && (
              <button className="btn-download" onClick={handleDownload}>
                Descargar archivo
              </button>
            )}
          </div>
        )}
      </main>
    </div>
  )
}

export default App
