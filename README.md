## Prerequisites

1. Create a virtual environment for this project
2. Install requirements:
    ```shell
    pip install -r requirements.txt
    ```
3. Make migrations
    ```shell
    python manage.py makemigrations
    ```
4. Migrate
    ```shell
    python manage.py migrate
    ```

## Run with Daphne (from your venv)
```shell
python manage.py runserver localhost:8000
```

## Run with Uvicorn (from your venv)
```shell
python run-uvicorn.py
```