import sys

__UVICORN_RUNNER = False

def set_uvicorn_runner(uvicorn_runner: bool):
    global __UVICORN_RUNNER
    __UVICORN_RUNNER = uvicorn_runner


def get_uvicorn_runner() -> bool:
    global __UVICORN_RUNNER
    return __UVICORN_RUNNER


def management_is_in_process() -> bool:
    """
    Determines if certain manage.py processes are running within this execution:
        - makemigrations
        - migrate
        - delete_old_migrations
        - startapp
        - collectstatic
        - --help
        - backup_migrations

    These processes do not run well, with Django internal changes at the same time.

    :return: `True` if this process is running any predefined "vulnerable" management process, `False` otherwise

    @see `Django documentation - django-admin and manage.py <https://docs.djangoproject.com/en/4.2/ref/django-admin/#django-admin-and-manage-py>`__

    @see `Django documentation - Migrations <https://docs.djangoproject.com/en/4.2/topics/migrations/#module-django.db.migrations>`__
    """
    return any(arg in ('makemigrations', 'migrate', 'delete_old_migrations', 'startapp', 'collectstatic', '--help', 'backup_migrations') for arg in sys.argv)