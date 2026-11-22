# Bianco / Nero — Zero Token // PWA di Conversione Locale

<p align="center">
  <img src="assets/social-preview.jpg" alt="Bianco / Nero Zero Token Cover Artwork" width="100%">
</p>

> **«Perché consumare token API e inviare immagini personali a server esterni quando il browser può convertire un file in scala di grigi in 2 millisecondi con totale privacy locale?»**  
> Web application e Progressive Web App (PWA) 100% client-side concepita da Emanuele BDC: trascina un'immagine, ottieni istantaneamente la conversione in scala di grigi ad alta fedeltà e scarica il file. Zero chiamate cloud, zero account, zero token, zero tracciamento.

[![GitHub Repo](https://img.shields.io/badge/GitHub-emanuelebdc%2Fbianco--nero--zero--token-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/emanuelebdc/bianco-nero-zero-token)
[![Live Web Tool](https://img.shields.io/badge/Live_Tool-emanuelebdc.com%2Fideas%2Fbianco--nero--zero--token-dfff00?style=for-the-badge&logo=googlechrome&logoColor=000000)](https://emanuelebdc.com/ideas/bianco-nero-zero-token/)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-emanuelebdc.github.io%2Fbianco--nero--zero--token-dfff00?style=for-the-badge&logo=github&logoColor=000000)](https://emanuelebdc.github.io/bianco-nero-zero-token/)
[![Zero Token](https://img.shields.io/badge/Costo-Zero_Token_%2F_Zero_API-10b981?style=for-the-badge)](https://github.com/emanuelebdc/bianco-nero-zero-token)
[![Offline PWA](https://img.shields.io/badge/PWA-100%25_Offline_Ready-0284c7?style=for-the-badge)](https://github.com/emanuelebdc/bianco-nero-zero-token)
[![Privacy](https://img.shields.io/badge/Privacy-100%25_Sandbox_Locale-black?style=for-the-badge)](https://github.com/emanuelebdc/bianco-nero-zero-token)

---

## ✦ La Visione del Progetto: L'Ingegneria della Sobrietà

Nel pieno della rivoluzione dell'intelligenza artificiale, stiamo assistendo a una pericolosa distorsione tecnologica: **l'uso sconsiderato di modelli linguistici e API cloud costose per compiti banali e deterministici**.

Molti sviluppatori integrano chiamate API cloud a pagamento e richiedono registrazione o abbonamenti solo per applicare filtri cromatici a una fotografia. Questo approccio comporta:
1. **Lentezza e Latenza di Rete**: Upload di file pesanti, attesa della risposta server e nuovo download.
2. **Violazione della Riservatezza**: Invio di immagini private o sensibili su server cloud di terze parti.
3. **Spreco Energetico e Finanziario**: Consumo ingiustificato di token e risorse di calcolo su data center remoti.

Ho progettato **Bianco / Nero — Zero Token** a Milano per ristabilire un principio fondamentale dell'ingegneria software: **usare l'intelligenza artificiale per il pensiero critico e lasciare alla matematica nativa del browser l'elaborazione deterministica dei pixel.**

L'applicazione carica l'immagine nella memoria grafica locale del browser, applica la formula standard di luminanza Rec. 709 su Canvas HTML5 in pochi millisecondi, e produce un file pronto per il download senza che un singolo byte lasci il dispositivo dell'utente.

---

## ✦ Interfaccia & Screenshot Reali

<p align="center">
  <img src="assets/screenshot-home.jpg" alt="Schermata di Caricamento Iniziale" width="49%">
  <img src="assets/screenshot-result.jpg" alt="Schermata del Risultato in Scala di Grigi" width="49%">
</p>

*Nota: La copertina artistica concettuale è generata per la documentazione visiva; la conversione all'interno della web app opera tramite matematica deterministica su Canvas e non fa uso di AI.*

---

## ✦ Funzionalità Distintive

- **Elaborazione 100% In-Memory**: Drag & drop istantaneo o selezione tramite pulsante; nessun upload HTTP.
- **Precisione Cromatica Rigorosa**: Conversione tramite somma pesata standard di luminanza:  
  $$\text{Luminanza} = \text{round}(0.2126 \cdot R + 0.7152 \cdot G + 0.0722 \cdot B)$$  
  Il canale Alpha viene preservato integralmente nei file PNG.
- **Geometria Integrale Garantita**: Risoluzione e proporzioni originali preservate al 100%; nessun ritaglio arbitrario o ridimensionamento forzato.
- **Doppio Canale di Esportazione**:
  - **PNG Lossless**: Con conservazione totale della trasparenza alpha.
  - **JPG ad Alta Qualità**: Qualità 95% su fondo bianco puro per documenti e stampa.
- **Architettura PWA Offline**: Service Worker con caching intelligente e Web Manifest per installazione a pieno schermo su macOS, Windows, iOS e Android.

---

## ✦ Scheda Tecnica // Technical Specifications

| Parametro | Specifica Tecnica |
|:---|:---|
| **Piattaforma di Esecuzione** | 100% Client-Side Web App & Progressive Web App (PWA) |
| **Tecnologie Frontend** | HTML5 Canvas 2D, Modern CSS Grid/Flexbox, ES6+ Vanilla JavaScript |
| **Dipendenze Esterne** | **0** (Nessun framework, nessuna libreria npm, zero build step) |
| **Algoritmo di Conversione** | ITU-R BT.709 Luminance Weighting su pixel buffer RGBA |
| **Formati Input Accettati** | JPEG, PNG, WebP (fino a 24 megapixel / 16.384px per lato) |
| **Formati Output Generati** | PNG (con trasparenza) / JPEG (95% qualità, sfondo bianco) |
| **Limite Dimensione File** | Fino a 30 MiB gestiti fluidamente in RAM del browser |
| **Sicurezza e Privacy** | Zero dati inviati in rete, zero cookie, zero telemetria, zero database |
| **Accessibilità** | Rispetta i canoni di visione monoculare di Emanuele BDC (testo >=16px, focus visibile) |
| **Installabilità** | Standalone PWA con `manifest.webmanifest` e `sw.js` per uso senza connessione |

---

## ✦ Struttura del Progetto

```text
bianco-nero-zero-token/
├── index.html               # Interfaccia utente, layout e motore di conversione Canvas
├── manifest.webmanifest     # Descrittore Progressive Web App e icone applicative
├── sw.js                    # Service Worker per il funzionamento completamente offline
├── icon-192.png             # Icona applicativa per schermata home (192x192)
├── icon-512.png             # Icona ad alta risoluzione (512x512)
├── start.py                 # Server HTTP Python locale facoltativo per test PWA
├── docs/                    # Asset di documentazione e anteprime
│   ├── cover.png            # Copertina editoriale ufficiale
│   ├── screenshot-home.jpg  # Cattura interfaccia di caricamento
│   └── screenshot-result.jpg # Cattura interfaccia risultato
└── README.md                # Documentazione ufficiale e manifesto
```

---

## ✦ Avvio Immediato & Esecuzione

### Uso Standalone Diretto (Nessuna Installazione)
1. Scarica o clona la repository:
   ```bash
   git clone https://github.com/emanuelebdc/bianco-nero-zero-token.git
   cd bianco-nero-zero-token
   ```
2. Fai doppio clic su `index.html` per aprirlo direttamente nel tuo browser preferito.
3. Trascina l'immagine ed esporta il risultato in PNG o JPG.

### Installazione come PWA Locale
Per abilitare l'installazione PWA su desktop o mobile tramite `localhost`:
```bash
python3 start.py
```
Apri `http://localhost:8765` e clicca sull'icona **Installa applicazione** nella barra degli indirizzi del browser.

---

## ✦ Autore & Filosofia del Progetto

Ideato, progettato e sviluppato da **[Emanuele BDC](https://emaf205.com)** a Milano.  
Pubblicato all'interno dell'osservatorio e laboratorio di idee **[EmaF205 Ideas Hub](https://emanuelebdc.com/ideas/)**.

Rilasciato sotto licenza open-source **[MIT License](LICENSE)**. Libero per utilizzi personali, didattici e professionali.
