from django.core.management.base import BaseCommand, CommandError
import os
from models import OutCsv
import csv
from django.shortcuts import redirect, get_object_or_404, render

class Command(BaseCommand):
    help = 'Import CSV data to coursemaster'
    def handle(self, *args, **options):
        check = []
        path = os.path.abspath(r'CsvFolder\out.csv')
        with open(path, encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            for row in reader:
                OutCsv.objects.create(code=row[0],symbole=row[1],date=row[2],open=row[3],high=row[4],low=row[5],close=row[6],volume=row[7],adjclose=row[8])