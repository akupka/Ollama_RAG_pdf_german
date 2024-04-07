# Ollama_RAG_pdf

Eine weiterer Chat Client für Ollama mit RAG

Der RAG Teil wurde von https://github.com/technovangelist/videoprojects/tree/main/2024-04-04-build-rag-with-python übernommen

1. Instalation der requirements: pip install -r requirements.txt
2. Starten der ChromaDB in einer eigenen Terminal Sitzung: chroma run --host localhost --port 8000 --path ../vectordb-stores/chromadb
3. pdf Umwandeln mit dem Skript pdf2text
4. offen ist noch das die txt Dateien in diese Liste aufgeführt werden müssen sourcedocs.txt
5. Die Text mit python3 import.py in die Chroma DB importieren
6. Suchen auf der Konsole mit: python3 search.py <yoursearch>
7. ALternativ dazu ein Chat mit streamlit run app.py 
