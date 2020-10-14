import sqlite3
import datetime

conn = sqlite3.connect('web_app.sqlite')
cur = conn.cursor()
cur.execute('Select * From users')

for row in cur:
    print ('Id: ', row[0])
    print ('Email: ', row[1])
    print('Password Hash: ', row[2])
    print ('Email Confirmation: ', row[3])
    print('Email Confirmed: ', row[4])
    print('Email Confirmed On: ', row[5])
    print('Temp Password: ', row[6])
    print('Temp Password Confirmed: ', row[7])
    print('Temp Password Sent: ', row[8])
    print('')

# print(cur.description)
cur.execute('Select * From users Where id = 2')
rows = cur.fetchall()

temp_confirmed_on = float(rows[0][7])
temp_sent_on = float(rows[0][8])
delta = temp_confirmed_on - temp_sent_on
print(temp_confirmed_on)
print(temp_sent_on)
print(delta/60)
