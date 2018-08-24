import sys, os
import csv

# Full path and name to your csv file
csv_filepathname="/home/rose/consultant_list/consultant_list.csv"
#  Full path to your django project directory
project_home="/home/rose/consultant_list/consultant_list/"
from consultants.models import Consultant

sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
for row in dataReader:
    if row[0] != 'Consultant Name':
    # Ignore the header row, import everything else
        consultant = Consultant()
        consultant.consultant_name = row[0]
        consultant.contact_number = row[1]
        consultant.practice = row[2]
        consultant.role = row[3]
        consultant.teams = row[4]
        consultant.skills = row[5]
        consultant.sectors = row[6]
        consultant.notes = row[7]
        consultant.save()
