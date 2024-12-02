Crear el virtual environment

`python -m venv .venv`

Activar el virtual environment
`source .venv/bin/activate` # Linux
`.venv\Scripts\activate` # Windows
`source .venv/Scripts/activate` # Windows (Git Bash)

Desactivar el virtual environment
`deactivate`

Crear un archivo de requerimientos
`pip freeze > requirements.txt`

Instalar las dependencias
`pip install -r requirements.txt`