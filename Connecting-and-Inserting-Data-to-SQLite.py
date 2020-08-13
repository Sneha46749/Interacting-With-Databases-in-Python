import sqlite3

def create_table():    
    con = sqlite3.connect("lite1.db")  #Connecting database 
    cur = con.cursor()  #Position of cursor
    cur.execute("CREATE TABLE IF NOT EXISTS shop (item TEXT, quantity INTEGER, price REAL)")
    con.commit()  #Committing changes to database
    con.close()

def insert(item, quantity, price):
    con = sqlite3.connect("lite1.db")
    cur = con.cursor()
    cur.execute("INSERT INTO shop VALUES(?,?,?)", (item, quantity, price))
    con.commit()
    con.close() 

def view():
    con = sqlite3.connect("lite1.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM shop")
    rows = cur.fetchall()
    con.close()
    return rows

print(view())  
insert("Tea Mug", 10, 50)    



