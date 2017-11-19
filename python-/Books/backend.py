import sqlite3

def connect():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer, checked text)")
	conn.commit()
	conn.close()
	
def insert(title, author, year, isbn, checked):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?)",(title, author, year, isbn, checked))
	conn.commit()
	conn.close()
	
def view():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book")
	rows = cur.fetchall()
	conn.close()
	return rows
	
def search(title="", author="", year="", isbn="", checked = ""):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book WHERE title=? OR author = ? OR year=? OR isbn=? OR checked=?", (title, author, year, isbn, checked))
	rows = cur.fetchall()
	conn.close()
	return rows
	
def delete(id):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM book WHERE id =?", (id,))
	conn.commit()
	conn.close()
	
def update(id, title, author, year, isbn, checked):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=?, checked=? WHERE id=?", (title, author, year, isbn, checked, id))
	conn.commit()
	conn.close()	
	
connect()