#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyme.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# -- COMANDOS --
# py -m venv
# py manage.py runserver
# python manage.py createsuperuser
# python manage.py makemigrations core
# python manage.py migrate core
# py manage.py flush
# -- PARA COMERTAR RAPIDO EN HTML: ctrl k c

# -- COMANDOS GIT --

# git init
# git config --global user.name "Tu nombre"
# git config --global user.email "tu@ejemplo.com"
# git add --all
# git commit -m "algun comentario"
# git remote add origin "raiz de tu git"
# git push -u origin master
# pa_autoconfigure_django.py --python=3.6 "rais de tu git" --nuke (esto en el dash de paw)
# git config core.autocrlf true

# ----- API ----

# https://rodrigopablo293.pythonanywhere.com// 
# https://rodrigopablo293.pythonanywhere.com//

#http://127.0.0.1:8000/