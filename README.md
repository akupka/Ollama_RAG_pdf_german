# Ollama_RAG_pdf

## Eine weiterer Chat Client für Ollama mit RAG

### Dies Projekt ist zum Auspobieren

Das "chunken" von Texten wie Matt Williams das macht ist Cool, er Teilt die Texte nach Sätzen und nicht nach Zeichen oder Token

Der RAG Teil wurde von https://github.com/technovangelist/videoprojects/tree/main/2024-04-04-build-rag-with-python übernommen

1. Instalation der requirements: pip install -r requirements.txt
1a. evtl.noch nltk runterladen https://www.nltk.org/data.html mit impnltk.py
2. Starten der ChromaDB in einer eigenen Terminal Sitzung: chroma run --host localhost --port 8000 --path ../vectordb-stores/chromadb
3. pdf Umwandeln mit dem Skript pdf2text
4. offen ist noch das die txt Dateien in diese Liste aufgeführt werden müssen sourcedocs.txt
5. Die Text mit python3 import.py in die Chroma DB importieren
6. Suchen auf der Konsole mit: python3 search.py <yoursearch>
7. ALternativ dazu ein Chat mit streamlit run app.py 

Bei der import.py muss man die Zeile 7
chroma.delete_collection("buildragwithpython")
beim ersten start deaktivieren oder auch sonst wenn man die Daten nicht löschen möchte

# Start der App
1. in einer Shell die Chroma DB mit:
chroma run --host localhost --port 8000 --path ../vectordb-stores/chromadb
2. in einer anderen Shell die Streamlit APP
streamlit run app.py 

Bei der Streamlit kann man verschiedene Ollama Modelle ausprobieren

ToDo:
* PDF besser in Text umwandeln mit https://github.com/VikParuchuri/marker
* Embedding mit ollama snowflake-arctic-embed ausprobieren
* phi3 mini als Model testen
* Prompt optimieren