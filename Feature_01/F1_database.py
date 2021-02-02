import sqlite3


# Making Database  (db) for Category (if not exists already) Table at the Start of Program
def category_data():
    con = sqlite3.connect("./AAT_Data.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS category (id INTEGER PRIMARY KEY, Category_Name TEXT NOT NULL UNIQUE);")
    con.commit()
    con.close()


# Function to Add Data For Category
def add_category(id, Category_Name):
    con = sqlite3.connect("./AAT_Data.db")
    cur = con.cursor()
    cur.execute("INSERT INTO category(id,Category_Name) VALUES (?, ?)", (id, Category_Name,))
    con.commit()
    con.close()


# Function to View Data For Category
def view_data():
    con = sqlite3.connect("./AAT_Data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM category")
    rows = cur.fetchall()
    con.close()
    return rows


category_data()


# Making Database  (db) for Product (if not exists already) Table at the Start of Program
def product_data():
    con = sqlite3.connect("./AAT_Data.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS "product" (
                    "id" INTEGER PRIMARY KEY,
                    "Product_Name" TEXT NOT NULL UNIQUE, 
                    "Category_ID" TEXT NOT NULL, 
                    "Quantity" INTEGER, 
                    "Price" CURRENCY REAL);""")
    con.commit()
    con.close()


# Function to Add Data For Product
def add_product(id, Product_Name, Category_ID, Quantity, Price):
    con = sqlite3.connect("./AAT_Data.db")
    cur = con.cursor()
    cur.execute("INSERT INTO product(id,Product_Name,Category_ID,Quantity,Price) VALUES (?, ?, ?, ?, ?)",
                (id, Product_Name, Category_ID, Quantity, Price,))
    con.commit()
    con.close()


# Function to View Data For Product
def view_product():
    con = sqlite3.connect("./AAT_Data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM product")
    rows = cur.fetchall()
    con.close()
    return rows


product_data()


# Function for View Data for Stock
def stock_check():
    con = sqlite3.connect("./AAT_Data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM product WHERE Quantity<20")
    rows = cur.fetchall()
    con.close()
    return rows
