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
        - startapp
        - collectstatic
        - --help

    These processes do not run well, with Django internal changes at the same time.

    :return: `True` if this process is running any predefined "vulnerable" management process, `False` otherwise

    @see https://docs.djangoproject.com/en/5.1/ref/django-admin/#django-admin-and-manage-py
    """
    return any(arg in ('makemigrations', 'migrate', 'startapp', 'collectstatic', '--help') for arg in sys.argv)
