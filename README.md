# Bianco / Nero — Zero Token

![Copertina](docs/cover.png)

**La stessa immagine, in scala di grigi. Nessuna API. Nessun token. Nessun costo per conversione.**

Web app statica client-side curata e firmata da **Emanuele BDC**: carica una foto, visualizza il bianco e nero e scaricalo. Elaborazione 100% sul tuo dispositivo in memoria grafica locale, senza account, senza cookie traccianti e senza backend.

---

## 🚀 Novità Versione 2.0 (Design System BDC)

- **Armonizzazione con lo Stile BDC & Ideas**: Interfaccia tattile conforme a `ideas.emanuelebdc.com` (fondo caldo `#f7f7f5`, bordi netti `2.5px solid #000000`, card arrotondate tattili).
- **Accessibilità emaf205 (Visione Monoculare)**: Testi sempre `>= 16px`, contrasto elevatissimo (WCAG AAA), pulsanti Icone-First con testo ridotto all'essenziale.
- **Caricamento Demo Istantaneo in 1-Click**: Pulsante per generare un'immagine di test ad alta risoluzione senza dover caricare file personali.
- **Incolla da Appunti (Cmd+V / Ctrl+V)**: Riconoscimento immediato di screenshot o immagini copiate nella clipboard.
- **Copia Negli Appunti in 1-Click**: Pulsante *Copia* per salvare il PNG direttamente negli appunti di sistema.
- **Preset Tonalità**: Scelta tra *Neutro Standard (BT.709)*, *Alto Contrasto (Deep Black)* e *Argento Morbido*.
- **Confronto Dinamico**: Switch rapido tra anteprima bianco e nero e originale a colori.
- **Pronto per Cloudflare Pages**: Configurazione `wrangler.toml` e file `_headers` inclusi e verificati.

---

## ⚡ Avvio Immediato

### Modalità 1: Cloudflare Pages (Deploy o Anteprima Locale)

L'applicazione è nativamente pronta per Cloudflare Pages.

Per testare localmente tramite Wrangler:
```sh
npx wrangler pages dev .
```

Per pubblicare direttamente su Cloudflare Pages:
```sh
npx wrangler pages deploy . --project-name=bianco-nero-zero-token
```

### Modalità 2: Server Locale Python

```sh
python3 start.py
```
Apre automaticamente `http://localhost:8765/index.html`.

### Modalità 3: File Standalone

Fai doppio clic su `index.html` per aprirlo in qualsiasi browser moderno (Chrome, Safari, Firefox, Edge).

---

## 🛠️ Funzioni & Caratteristiche

- **Drag & Drop Reattivo**: Trascina le immagini nell'area dedicata o in qualsiasi punto della finestra.
- **Piena Risoluzione**: Mantiene il 100% delle dimensioni e dei pixel originali (fino a 24 megapixel e 16.384 pixel per lato).
- **Esportazione Duplice**:
  - **PNG**: Preserva il canale alfa di trasparenza.
  - **JPG**: Applica sfondo bianco puro e qualità al 95%.
- **Cruscotto Metadati**: Mostra dimensioni in pixel, megapixel effettivi, peso del file e formato.
- **PWA & Offline**: Dotata di `manifest.webmanifest` e `sw.js` per essere installata su desktop e smartphone.
- **Nativamente Silenziosa**: Nessun suono o bloop sintetico.

---

## 📐 Formati e Limiti

| Voce | Supporto |
|---|---|
| **Input** | JPEG, PNG, WebP |
| **Output** | PNG (con trasparenza), JPEG (qualità 95%) |
| **Peso massimo** | 30 MiB |
| **Dimensioni massime** | 24 megapixel; 16.384 pixel per lato |
| **Algoritmo di Luminanza** | Formula ITU-R BT.709: `0.2126*R + 0.7152*G + 0.0722*B` |
| **Animazioni** | Un singolo fotogramma (nessun export GIF/APNG) |
| **Privacy** | 100% locale, zero upload su server |

---

## 📁 Struttura della Repository

```
bianco-nero-zero-token/
├── assets/
│   ├── css/
│   │   └── theme.css          # Design System BDC Suite (Ideas style)
│   └── img/
│       └── emanuele-bdc.jpg   # Avatar autore
├── docs/                      # Copertina e documentazione visiva
│   ├── cover.png
│   ├── screenshot-home.jpg
│   └── screenshot-result.jpg
├── _headers                   # Regole di sicurezza e MIME-types per Cloudflare Pages
├── CHANGELOG.md               # Storico versioni e modifiche
├── icon-192.png               # Icona PWA 192x192
├── icon-512.png               # Icona PWA 512x512
├── index.html                 # Applicazione web autonoma
├── manifest.webmanifest       # Configurazione Web App Manifest PWA
├── README.md                  # Documentazione ufficiale
├── start.py                   # Server locale facoltativo
├── sw.js                      # Service Worker offline
├── VERSION.txt                # Versione corrente (2.0.0)
└── wrangler.toml              # Configurazione Cloudflare Pages
```

---

## 🔒 Riservatezza & Conformità

Le immagini selezionate o incollate vengono lette e manipolate unicamente nella memoria volatile del browser tramite Canvas 2D. Non viene effettuata alcuna chiamata esterna o invio di telemetria. Nessun dato lascia mai il dispositivo dell'utente. Conforme a GDPR e ai principi di minimizzazione dei dati.

---

## 👤 Autore & Crediti

Curato e firmato da **Emanuele BDC** — *Consulente Strategico & Formatore AI*.  
Milano, Italia — [emanuelebdc.com](https://emanuelebdc.com)
