import psycopg2
from psycopg2 import sql
from scripts import *

class Database:
    def __init__(self, dbname='postgrestests', user='postgrestests', password='postgrestests', host='localhost', connect_timeout=3):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.connect_timeout = connect_timeout
        
    def connect(self):
        try:
            self.connect = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, connect_timeout=self.connect_timeout)
            self.connect.autocommit = True
        except:
            print("checkConnection")
        
    def database_creator(self):
        self.__types_creator()
        self.__tables_creator()
        self.__extansion_creator()
    
    def database_deleter(self):
        self.__tables_deleter()
    
    def __extansion_creator(self):
        cursor = self.connect.cursor()
        try:
            cursor.execute(sql.SQL(SQL_EXTANSION))
        except:
            print('EXTANSION already deleted')
        cursor.close()
        
        
    def __tables_deleter(self):
        cursor = self.connect.cursor()
        try:
            cursor.execute(sql.SQL(SQL_DELETE_TABLES))
        except:
            print('tables already deleted')
        cursor.close()
        
        
    def __types_creator(self):
        cursor = self.connect.cursor()
        try:
            cursor.execute(sql.SQL(SQL_DATA_TYPES))
        except:
            print('types already exists')
        cursor.close()
        
    def __tables_creator(self):
        cursor = self.connect.cursor()
        try:
            cursor.execute(sql.SQL(SQL_TABLES))
        except:
            print('tables already exists')
        cursor.close()