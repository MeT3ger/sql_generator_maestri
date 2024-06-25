from psycopg2 import sql
from scripts import *
from uuid import *
from datetime import datetime, timezone, timedelta
from random import randint, choice
import string

def gen_rus(length):
    letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    rand_string = ''.join(choice(letters) for i in range(length))
    return rand_string

def gen_eng(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(choice(letters) for i in range(length))
    return rand_string

def gen_ger(length):
    letters = "abcdefghijklmnopqrstuvwxyzäöüß"
    rand_string = ''.join(choice(letters) for i in range(length))
    return rand_string

def gen_franch(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    rand_string = ''.join(choice(letters) for i in range(length))
    return rand_string

class Inserter:
    def __init__(self, database):
        self.database = database
    
    def address(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(ADDRESS))
        cursor.close()
    
    def appointment(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(APPOINTMENT))
        cursor.close()
    
    def client(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(CLIENT))
        cursor.close()        
    
    def contact(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(CONTACT))
        cursor.close()
    
    def customer(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(CUSTOMER))
        cursor.close()
    
    def employee(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(EMPLOYEE))
        cursor.close()
        
    def procedure(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(PROCEDURE))
        cursor.close()
    
    def professional(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(PROFESSIONAL))
        cursor.close()
    
    def salon(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(SALON))
        cursor.close()
    
    def service(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(SERVICE.format(
            uuid4(),
            datetime.now(timezone.utc) + timedelta(minutes=randint(1, 10)),
            datetime.now() + timedelta(hours=randint(1, 10)),
            "NULL",
            gen_eng(10),
            gen_eng(10),
            "nails"
        )))
        cursor.close()
    
    #TODO: realize
    
    def service_jsonb(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(SERVICE_JSON.format(
            uuid4(),
            datetime.now(timezone.utc) + timedelta(minutes=randint(1, 10)),
            datetime.now() + timedelta(hours=randint(1, 10)),
            "NULL",
            gen_eng(10),
            gen_eng(10),
            "nails",
            '{{ "rus": "{}", "eng": "{}", "ger": "{}", "franch": "{}" }}'.format(
                gen_rus(10),
                gen_eng(10),
                gen_ger(10),
                gen_franch(10)
            ) 
        )))
        cursor.close()
    
    def service_table(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(SERVICE_TABLE.format(
            uuid4(),
            gen_rus(10),
            gen_eng(10),
            gen_ger(10),
            gen_franch(10)
        )))
        cursor.close()
    
    def skill(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(SKILL))
        cursor.close()
            
    def timetable(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(TIMETABLE))
        cursor.close()
    
    def user(self):
        cursor = self.database.connect.cursor()
        cursor.execute(sql.SQL(USER))
        cursor.close()    
