import psycopg2

def create_table():    
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port'5432'")  
    cur = con.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS shop (item TEXT, quantity INTEGER, price REAL)")
    con.commit()  
    con.close()

def insert(item, quantity, price):
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port'5432'")
    cur = con.cursor()
    cur.execute("INSERT INTO shop VALUES(%s,%s,%s)", (item, quantity, price))
    con.commit()
    con.close() 

def view():
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port'5432'")
    cur = con.cursor()
    cur.execute("SELECT * FROM shop")
    rows = cur.fetchall()
    con.close()
    return rows

def delete(item):
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port'5432'")
    cur = con.cursor()
    cur.execute("DELETE from shop where item = %s", (item,))
    con.close()

def update(quantity, price, item):
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port'5432'")
    cur = con.cursor()
    cur.execute("UPDATE shop SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    con.commit()
    con.close()   

create_table
delete("orange")
update(20, 15, "orange")
insert("orange", 10, 20)
print(view())
    



