import pdfplumber
import os

def pdf_to_text(pdf_file, output_folder):
    # Extrahiere den Dateinamen der PDF-Datei ohne Erweiterung
    pdf_filename = os.path.splitext(os.path.basename(pdf_file))[0]
    
    with pdfplumber.open(pdf_file) as pdf:
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            text = page.extract_text()
            
            # Erzeuge den Dateinamen für die Textdatei
            output_filename = f'{pdf_filename}_page_{page_num + 1}.txt'
            output_file = os.path.join(output_folder, output_filename)
            
            # Schreibe den extrahierten Text in die Textdatei
            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(text)

# Beispielaufruf des Skripts
if __name__ == "__main__":
    input_folder_path = './pdf'
    output_folder_path = './txt'
    
    # Überprüfe, ob das Ausgabeverzeichnis existiert, andernfalls erstelle es
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    # Durchlaufe alle PDF-Dateien im Eingabeverzeichnis
    for filename in os.listdir(input_folder_path):
        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(input_folder_path, filename)
            pdf_to_text(pdf_file_path, output_folder_path)