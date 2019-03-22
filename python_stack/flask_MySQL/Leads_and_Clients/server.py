from flask import Flask, render_template, request, redirect
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('leadsdb')
# now, we may invoke the query_db method
print("all the users", mysql.query_db("SELECT * FROM customers;"))

@app.route('/')
def index():
    all_customers = mysql.query_db("SELECT * FROM customers")
    print("Fetched all customers", all_customers)
    return render_template('index.html', customers = all_customers)

if __name__ == "__main__":
    app.run(debug=True)

