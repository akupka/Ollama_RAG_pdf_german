import streamlit as st
from ollama import Ollama

# Initialisiere Ollama
ollama = Ollama()

# Seitentitel
st.set_page_config(page_title="Ollama Chat")

# Seitenüberschrift
st.title("Ollama Chat")

# Auswahl des Ollama-Modells
model = st.selectbox("Wähle ein Ollama-Modell aus:", ollama.list_models())

# Eingabefeld für Benutzernachricht
user_input = st.text_area("Deine Nachricht:", height=100)

# Sende-Button
if st.button("Senden"):
    # Generiere Antwort mit Ollama
    response = ollama.show(model, user_input)
    
    # Zeige Antwort an
    st.markdown(f"**Ollama:** {response}")