from os import environ

from django.core.management import execute_manager

from presupuesto import settings


environ['DJANGO_SETTINGS_MODULE'] = "presupuesto.settings"


def main():
    execute_manager(settings)
