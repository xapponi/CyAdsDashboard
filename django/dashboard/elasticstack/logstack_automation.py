import MySQLdb
import pandas as pd
import os
from datetime import datetime
import subprocess

db = MySQLdb.connect(os.getenv('DATABASE_HOST'),os.getenv('DATABASE_USER'), os.getenv('DATABASE_PASSWORD'), os.getenv('DATABASE'))
cursor = db.cursor()

cursor.execute("SHOW TABLES")

data = cursor.fetchall()

for record in data:
    record = record[0]
    print(record)

command = "C:\\Users\\xapponi\\logstash.lnk -f mysql.conf"  # the shell command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
output = process.communicate()

print output[0]

db.close()
