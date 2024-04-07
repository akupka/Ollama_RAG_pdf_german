# Ollama_RAG_pdf

## Eine weiterer Chat Client für Ollama mit RAG

### Dies Projekt ist zum Auspobieren

Das "chunken" von Texten wie Matt Williams das macht ist Cool, er Teilt die Texte nach Sätzen und nicht nach Zeichen oder Token

Der RAG Teil wurde von https://github.com/technovangelist/videoprojects/tree/main/2024-04-04-build-rag-with-python übernommen

1. Installation der requirements: pip install -r requirements.txt
1a. evtl.noch nltk runterladen https://www.nltk.org/data.html mit impnltk.py
3. Starten der ChromaDB in einer eigenen Terminal Sitzung: chroma run --host localhost --port 8000 --path ../vectordb-stores/chromadb
4. pdf Umwandeln mit dem Skript pdf2text
5. offen ist noch das die txt Dateien in diese Liste aufgeführt werden müssen sourcedocs.txt
6. Die Text mit python3 import.py in die Chroma DB importieren
7. Suchen auf der Konsole mit: python3 search.py <yoursearch>
8. Alternativ dazu ein Chat mit streamlit run app.py 

Bei der import.py muss man die Zeile 7
chroma.delete_collection("buildragwithpython")
beim ersten start deaktivieren oder auch sonst wenn man die Daten nicht löschen möchte

Bei der Streamlit kann man verschiedene Ollama Modelle ausprobieren
