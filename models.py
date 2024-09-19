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

def createLot(userID, name_lot, lot_description, min_price_lot, step, price_for_buy):
    cursor.execute(f"INSERT INTO Active_lots(user_id, name_lot, lot_description, min_price_lot, step, price_for_buy) VALUES({userID}, '{name_lot}', '{lot_description}', {min_price_lot}, {step}, {price_for_buy})")
    con.commit()
    return True

def addBid(id_lot, userID, amount, created_at):
    cursor.execute(f"INSERT INTO Bids_table(id_lot, userID, amount, created_at) VALUES({id_lot}, {userID}, {amount}, {created_at})")
    con.commit()
    return True

def addLotHistory(id_lot, status, current_price, buyer):
    cursor.execute(f"INSERT INTO Lots_history(id_lot, status, current_price, buyer) VALUES({id_lot}, '{status}', {current_price}, {buyer})")
    con.commit()
    return True

def getLots():
    cursor.execute(f"SELECT * FROM Active_lots WHERE NOT EXISTS (SELECT * FROM Lots_history WHERE Lots_history.id_lot = Active_lots.id_lot AND Lots_history.status = 'Не завершен')")

# createUser('Stanislaw', '1234')
# checkUser('Stanislaw', '')