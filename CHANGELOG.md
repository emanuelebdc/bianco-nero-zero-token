# Cronologia Rilasci — Bianco / Nero Zero Token

## [2.0.0] — 2026-11-06

### Riprogettazione Architetturale & Design System
- **Stile BDC & Ideas**: Armonizzazione completa con la suite strumenti BDC (`ideas.emanuelebdc.com`), fondo `#f7f7f5`, bordi netti `2.5px solid #000000`, card arrotondate tattili.
- **Framework & Icone**: Integrazione Bootstrap 5.3.3 e Bootstrap Icons 1.11.3 con CDN ultra-veloce e zero dipendenze npm pesanti.
- **Accessibilità emaf205 (Visione Monoculare)**:
  - Bando totale a caratteri inferiori a 16px.
  - Contrasto elevatissimo WCAG AAA.
  - Pulsanti Icone-First con testo ridotto a 1-2 parole essenziali.
  - Zero emoji decorative a caso, solo icone vettoriali semantiche.
- **Nativamente Silenzioso**: Nessun suono o bloop sintetico.

### Nuove Funzionalità Operative
- **Caricamento Demo Istantaneo in 1-Click**: Possibilità di testare immediatamente l'app senza dover selezionare una foto personale.
- **Incolla da Appunti (Cmd+V / Ctrl+V)**: Rilevamento automatico di screenshot o immagini copiate negli appunti.
- **Copia Immagine Convertita in 1-Click**: Salvataggio diretto negli appunti di sistema tramite `ClipboardItem` PNG.
- **Preset Tonalità**: Scelta tra *Neutro Standard (BT.709)*, *Alto Contrasto (Deep Black)* e *Argento Morbido*.
- **Confronto Dinamico**: Possibilità di commutare istantaneamente tra l'anteprima in bianco e nero e l'originale a colori.
- **Cruscotto Metadati**: Visualizzazione in tempo reale di dimensioni (pixel), peso (MB), megapixel e formato sorgente.

### Cloudflare Pages & PWA
- **Configurazione Cloudflare Pages**: Aggiunti `wrangler.toml` e file `_headers` con regole di sicurezza e mime-type per manifest e worker.
- **Service Worker v2.0.0**: Caching strategico per funzionamento 100% offline.
- **Manifest PWA**: Icone e tema coerenti per installazione su desktop e dispositivi mobili.

---

## [1.0.0] — 2026-11-03
- Prima release con conversione client-side tramite Canvas API e server locale Python.
