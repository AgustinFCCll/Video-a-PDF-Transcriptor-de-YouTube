import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/convert': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path
      },
      '/download': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path
      },
      '/health': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path
      },
    }
  }
})
