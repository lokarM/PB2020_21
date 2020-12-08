import json
import sqlite3
import os

def napolni_tabelo_film(conn, filmi):
    cur = conn.cursor()
    for film in filmi:
        sql = '''
            INSERT INTO film
            (naslov,dolzina,leto,ocena,id,metascore,glasovi,zasluzek,oznaka,opis)
            VALUES (?,?,?,?,?,?,?,?)
        '''
        parametri = [
            film['naslov'],
            film['dolzina'],
            film['leto'],
            film['ocena'],
            film['id'],
            film['metascore'],
            film['glasovi'],
            film['zasluzek'],
            film['oznaka'],
            film['opis'],
        ]
