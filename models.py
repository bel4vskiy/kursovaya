import pyodbc

con = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Auction;Trusted_Connection=yes;")
cursor = con.cursor()



def createUser(login, psw):
    cursor.execute(f"INSERT INTO Users(login, password) VALUES('{login}', '{psw}')")
    con.commit()
    return True

def checkUser(login, psw):
    cursor.execute(f"SELECT login, password FROM Users WHERE login='{login}' AND password='{psw}'")
    print(cursor.fetchall()) 
    if cursor.fetchall() == []:
        return False
    return True

# createUser('Stanislaw', '1234')
# checkUser('Stanislaw', '')