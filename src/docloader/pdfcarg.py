from langchain_community.document_loaders import PyPDFLoader

#cargar pdf por lotes
pdf_files = [
    "doc\\funcion_alcaldia_spa.pdf",
    "doc\\Funciones-Alcalde.pdf",
    "doc\\Funciones-de-el_ayunt.pdf"
]

# Lista para almacenar todas las páginas
all_pages = []

# Iterar sobre la lista de archivos PDF y cargar cada uno
for pdf_file in pdf_files:
    loader = PyPDFLoader(pdf_file)
    pages = loader.load_and_split()
    all_pages.extend(pages)

text_chunk = all_pages
print(text_chunk)

