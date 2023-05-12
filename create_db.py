import sqlite3
def create_db():
    conn=sqlite3.connect(database=r'ims.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(emp_id integer PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,password text,user_type ext,address text,salary text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice_id integer PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS categories(cat_id integer PRIMARY KEY AUTOINCREMENT,name text)")
    conn.commit()
                                                                                            #prod_id","Category","Supplier","name","price","qty","status
    cur.execute("CREATE TABLE IF NOT EXISTS product(prod_id integer PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,name text,price text,qty text,status text)")
    conn.commit()

    

create_db()
