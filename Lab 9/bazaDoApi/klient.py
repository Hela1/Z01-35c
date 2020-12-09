import sqlite3
import requests

class Client:
    def __init__(self):
        self.conn = sqlite3.connect('serwerBD.db')
        self.c = self.conn.cursor()
        self.create_database()
    
    def logIn(self):
        login = input("Login: ")
        password = input("Password: ")
        return requests.get("http: // 127.0.0.1: 5000/user/{login}/{password}/").status_code == 200


