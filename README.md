 # Prueba Analytics Django with Streamlit

Este proyecto es una aplicación web que utiliza Django para el backend y Streamlit para el frontend.

## Estructura del Proyecto
┣ 📂backend
┃ ┣ 📂core
┃ ┃ ┣ 📂api
┃ ┃ ┃ ┗ 📜urls.py
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┣ 📜asgi.py
┃ ┃ ┣ 📜settings.py
┃ ┃ ┣ 📜urls.py
┃ ┃ ┗ 📜wsgi.py
┃ ┣ 📂customers
┃ ┃ ┣ 📂api
┃ ┃ ┃ ┣ 📜serializers.py
┃ ┃ ┃ ┣ 📜urls.py
┃ ┃ ┃ ┗ 📜views.py
┃ ┃ ┣ 📂migrations
┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃ ┗ 📜0001_initial.py
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┣ 📜admin.py
┃ ┃ ┣ 📜apps.py
┃ ┃ ┣ 📜choices.py
┃ ┃ ┣ 📜models.py
┃ ┃ ┣ 📜tests.py
┃ ┃ ┗ 📜views.py
┃ ┣ 📜db.sqlite3
┃ ┗ 📜manage.py
┣ 📜.gitignore
┣ 📜app.py
┗ 📜requirements.txt


## Preview

![Preview](img/preview.png)

## Requisitos

- Python 3.x
- Django
- Streamlit

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tintayadev/Analytics-Django-with-Streamlit
    cd Analytics-Django-with-Streamlit
    ```

2. Crea un entorno virtual:
    ```sh
    python -m venv venv
    ```

3. Activa el entorno virtual:
    - En Windows:
        ```sh
        venv\Scripts\activate
        ```
    - En macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

5. Aplica las migraciones de Django:
    ```sh
    cd backend
    python manage.py migrate
    ```

6. Ejecuta el servidor de desarrollo de Django:
    ```sh
    python manage.py runserver
    ```

7. Ejecuta la aplicación de Streamlit:
    ```sh
    cd ..
    streamlit run app.py
    ```

## Uso

1. Abre tu navegador y ve a `http://127.0.0.1:8000/` para acceder al backend de Django.
2. Abre tu navegador y ve a `http://127.0.0.1:8501/` para acceder al frontend de Streamlit.

