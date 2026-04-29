import { useState } from 'react'
import './App.css'

function App() {
  const [url, setUrl] = useState('')
  const [lang, setLang] = useState('es')
  const [asHtml, setAsHtml] = useState(false)
  const [status, setStatus] = useState('idle')
  const [message, setMessage] = useState('')
  const [downloadUrl, setDownloadUrl] = useState(null)

  const API_URL = ''

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
        const filename = data.file_path.split(/[/\\]/).pop()
        setDownloadUrl(`/download/${filename}`)
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
    <>
      <div className="bg-container">
        <div className="bg-grid"></div>
        <div className="bg-glow"></div>
        <div className="bg-noise"></div>
      </div>
      <div className="container">
        <header className="header">
          <div className="header-icon">
            <svg viewBox="0 0 24 24" fill="currentColor" width="32" height="32">
              <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
            </svg>
          </div>
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
    </>
  )
}

export default App
