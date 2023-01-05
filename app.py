from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'gustavo'
app.config['MYSQL_HOST'] = 'http://34.176.51.200/'
app.config['MYSQL_DB'] = 'mysql'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# mysql.init_app(app)

@app.route('/')
def CONNECT_DB():
    CS = mysql.connection.cursor()
    CS.execute('''CREATE TABLE Empleados (id INTEGER, name VARCHAR(20))''')

    CS.execute('''INSERT INTO Empleados VALUES (1, 'Gustavo')''')
    CS.execute('''INSERT INTO Empleados VALUES (2, 'Victor')''')
    mysql.connection.commit()
    return 'Executed successfully'

if __name__ == "__main__":
    app.run(debug=True)
