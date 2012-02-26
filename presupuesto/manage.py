from sys import stderr

from django.core.management import execute_manager


try:
    import settings
except ImportError:
    stderr.write(
        "Can't find the file 'settings.py' in the directory containing %r",
        __file__,
        )


if __name__ == "__main__":
    execute_manager(settings)
