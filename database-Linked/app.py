
import mysql.connector
import difflib
from difflib import get_close_matches

con = mysql.connector.connect(
    username="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)
cursor = con.cursor()


def check(value):
    query = cursor.execute(
        "SELECT * FROM Dictionary WHERE Expression='%s'" % value)
    result = cursor.fetchall()
    if len(result) > 1:
        for res in result:
            print(res[1])
    elif len(result) == 1:
        print(result[0][1])
    else:
        print("Sorry This word not in our database")


while True:
    name = input("Enter your word: ")
    check(name.lower())
