"""Server facoltativo per la PWA: accessibile solo da questo computer."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
from threading import Timer
import webbrowser
folder = str(Path(__file__).resolve().parent)
try:
    server = ThreadingHTTPServer(('127.0.0.1', 8765), partial(SimpleHTTPRequestHandler, directory=folder))
except OSError:
    raise SystemExit('Porta 8765 occupata. Chiudi il server precedente oppure apri index.html con doppio clic.')
print('Bianco / Nero: http://localhost:8765/index.html — Ctrl+C per chiudere')
Timer(0.5, lambda: webbrowser.open('http://localhost:8765/index.html')).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
