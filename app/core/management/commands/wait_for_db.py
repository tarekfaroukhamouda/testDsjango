''''
Django command to wait for database to be avilabale
'''
import time
from psycopg2 import OperationalError as Pyscopg2Error
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    '''Django command to wait fro database'''

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write("Waittig for database ...")
        dp_up = False
        while dp_up is False:
            try:
                self.check(databases=['default'])
                dp_up = True
            except (Pyscopg2Error, OperationalError):
                self.stdout.write(
                    "Database is unavilable waitting for 1 secand ....")
                time.sleep(1)
        self.stdout.write(
            self.style.SUCCESS(
                'Database available!'
                )
            )
