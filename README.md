# Progetto di Editoria Digitale
Progetto realizzato per il corso di Editoria Digitale del prof. Ceravolo Paolo.

### Formati disponibili per il progetto
I formati che sono resi disponibili per visualizzare il progetto sono: .html, .epub, .docx

## Pagina web .html
Questo è un progetto di editoria. Puoi visualizzare la pagina principale cliccando qui:  
👉 [Apri index.html](https://htmlpreview.github.io/?https://github.com/MassimilianoGentilini/Progetto_editoria/blob/main/ProgettoEditoriaDigitale_Gentilini/index.html)

## Ebook .epub
Questo è un progetto di editoria. Puoi scaricare l'ebook cliccando qui:  
👉 [Scarica Ebook](https://github.com/MassimilianoGentilini/Progetto_editoria/raw/main/ProgettoEditoriaDigitale_Gentilini/output.epub)

## Documento .docx
Questo è un progetto di editoria. Puoi scaricare il documento cliccando qui:  
👉 [Scarica documento](https://github.com/MassimilianoGentilini/Progetto_editoria/raw/main/ProgettoEditoriaDigitale_Gentilini/output.docx)


## Struttura del Progetto
Il progetto è stato realizzato utilizzando fonti di informazioni libere e gratuite e script di Python. Il formato .html è stato realizzato utilizzando come linguaggi di programmazione HTML,Java Script e CSS. Gli altri due formati disponibili, .epub e .docx sono stati ottenuti grazie a degli script di Python dediti all'automatizzazione del processo di produzione editoriale permettendo così di velocizzare la gestione, trasformazione e pubblicazione dei documenti. All'interno della repository saranno quindi disponibili script di Python per l'automatizzazione del processo di produzione editoriale, oltre ai formati finali, i metadati,la bibliografia

## Flusso di gestione documentale

```mermaid
graph LR
    A[Tema Progetto] --> B(Estrazione informazioni dalle fonti)
    B --> C{Svolgimento operazioni sul file attraverso codici Python}
    C --> D(Estrazione metadati da fonti Wikipedia)
    C --> E(Conversione formati in .html, .docx, ePub)
    C --> F(Modifiche al file Markdown)
    C --> G(Creazione schema.org e ONIX)
    D --> H(Aggiunta dettagli estetici e funzionali)
    E --> H
    F --> H
    G --> H
    H --> I{Caricamento finale dei file}
