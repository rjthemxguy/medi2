
from os import system
from colorama import Fore, Back, Style
import time
import sqlite3


class database_class:
    def __init__(self):

        try:
            self.conn = sqlite3.connect("db/vernon.db")
        except sqlite3.Error as e:
            print(e)
            print("Database Error")
            exit(1)

    def getCPT(self, emgCode):
        self.code = emgCode

        cur = self.conn.cursor()
        cur.execute("SELECT CPT FROM codes WHERE code=?", (self.code,))

        rows = cur.fetchall()

        return rows[0]

    def getPrice(self, CPT):

        cur = self.conn.cursor()
        cur.execute("SELECT price FROM comp WHERE hcpcs=? LIMIT 1", (CPT,))

        rows = cur.fetchone()
        if len(rows) == 1:
            price = rows[0]
            print(CPT)
            print(price)
        else:
            price = rows

        return price





    def deleteAccession(self):

        while True:
            system("clear")
            print()
            print(Fore.YELLOW + "Enter the Accession number to delete from the database")

            accessionNumber = str(input())
            system("clear")
            print(Fore.YELLOW + "Is this the accession number you wish to delete: " + Fore.WHITE + accessionNumber)
            y = str(input())
            if y == "y":
                sql = "DELETE FROM accessionRan WHERE accession=" + "'" + accessionNumber + "'"
                self.mycursor.execute(sql)
                print(Fore.RED + "Accession number deleted!")
                time.sleep(3)
                while True:
                    system("clear")
                    print(Fore.YELLOW + "Do you want to delete another accession code?")
                    x = input()
                    if x == "y":
                        break
                    if x == "n":
                        break
                if x == "y":
                    continue
                if x == "n":
                    break
            if y == "n":
                continue

    def insertAccession(self, _accession):
        pass



    def didRun(self, accession):

        sql = "SELECT accession FROM accessionRan WHERE accession=" + "'" + accession + "'"

        self.mycursor.execute(sql)
        self.myresult = self.mycursor.fetchone()
        try:
            x = len(self.myresult)
            return True
        except:
            return False


