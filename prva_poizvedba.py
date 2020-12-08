import sqlite3

pov = sqlite3.connect('filmi.sqlite')
cur = pov.cursor()
sql_ukaz = 'SELECT naslov, leto, ocena FROM film LIMIT 3'
cur.execute(sql_ukaz)
print(cur.fetchone())
sql_ukaz = 'DELETE  FROM film'
cur.execute(sql_ukaz)
print(cur.fetchone())
sql_ukaz = 'SELECT naslov, leto, ocena FROM film LIMIT 3'
cur.execute(sql_ukaz)
print(cur.fetchone())