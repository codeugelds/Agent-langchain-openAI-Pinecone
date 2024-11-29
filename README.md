# Agente 

Este proyecto es un agente diseñado para interactuar con clientes y proporcionarles información relevante de manera eficiente referente a una documentacion suministrada. Utiliza diversas herramientas y bibliotecas para procesar y presentar datos de manera clara y concisa.
Entre ellas:
Pinecone : base de datos vectorial
LangChain
openAI : debemos tener en cuenta que se puede integrar cualquier modelo de AI
langchain-community
langchain-openai
langchain-pinecone
pinecone-client
Gradio


## Instalación

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```sh
pip install -r [requirements.txt]

# USO 

python src/main.py

## Claro, aquí tienes un ejemplo de un README para tu proyecto:

```markdown
# Agente

Este proyecto es un agente diseñado para interactuar con clientes y proporcionarles información relevante de manera eficiente. Utiliza diversas herramientas y bibliotecas para procesar y presentar datos de manera clara y concisa.


## Uso

Para ejecutar el agente, utiliza el siguiente comando:

```sh
python src/main.py
```

## Archivos Principales

- `src/chunking.py`: Contiene la lógica para dividir los datos en partes manejables.
- `src/config.py`: Configuración del proyecto.
- `src/contxprom.py`: Módulo para gestionar el contexto y las promociones.
- `src/crmemo.py`: Módulo para crear y gestionar memorandos.
- `src/docloader/pdffarg.py`: Cargador de documentos PDF.
- `src/Genemb.py`: Generador de embeddings.
- `src/gra.py`: Módulo para gráficos.
- `src/imprime.py`: Módulo para impresión.
- `src/pineconeind.py`: Integración con Pinecone.
- `src/promptemplate.py`: Plantillas de prompts.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
```

Este README proporciona una visión general del proyecto, instrucciones de instalación, uso y una breve descripción de los archivos principales. Puedes ajustarlo según las necesidades específicas de tu proyecto.