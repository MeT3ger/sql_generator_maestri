from psycopg2 import sql
from scripts import *
from uuid import *
from times import *

class Searcher:
    def __init__(self, database):
        self.database = database
        
    @time
    def titles(self, word = "empty", languague="eng", fuzzy=False, similarity=0.0):
        
        if fuzzy:
            sql_query = '''
                SELECT id, {}
                FROM titles
                WHERE SIMILARITY({}, '{}') > {};
            '''.format(
                languague,
                languague,
                word,
                similarity
            )
        else:
            sql_query = '''
                SELECT id, {}
                FROM titles
                WHERE {} = '{}';
            '''.format(
                languague,
                languague,
                word
            )
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(sql_query))
        result = cursor.fetchall()
        cursor.close()
        return result
    
    @time
    def service_jsonb(self, word = "empty", languague="eng", fuzzy=False, similarity=0.0):
        if fuzzy:
            #id, alliases -> '{}'
            sql_query = '''
                SELECT id, alliases -> '{}'
                FROM jsonb_services
                WHERE SIMILARITY(alliases->>'{}', '{}') > {};
            '''.format(
                languague,
                languague,
                word,
                similarity
            )
        else:
            sql_query = '''
                SELECT id, alliases -> '{}'
                FROM jsonb_services
                WHERE alliases->>'{}'='{}';
            '''.format(
                languague,
                languague,
                word
            )
        
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(sql_query))
        result = cursor.fetchall()
        cursor.close()
        return result
    
    @time    
    def service(self, word = "empty", fuzzy=False, similarity=0.0):
        if fuzzy:
            sql_query = '''
                SELECT id, title
                FROM services
                WHERE SIMILARITY(title, '{}') > {};
            '''.format(
                word,
                similarity
            )
        else:
            sql_query = '''
                SELECT id, title
                FROM services
                WHERE title = '{}';
            '''.format(
                word
            )
            
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(sql_query))
        result = cursor.fetchall()
        cursor.close()
        return result
    