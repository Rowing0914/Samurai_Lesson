import sqlite3
from contextlib import closing
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)
dbname = 'db1.db'

@app.route('/')
def index():
    return "hello world!"

@app.route('/insertdata')
def insertdata():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    username = request.args.get('username')
    password = request.args.get('password')
    print((username, password))
    sql = 'insert into user_master (username, password) values (?, ?)'
    c.execute(sql, (username, password))
    conn.commit()
    return redirect('/')

@app.route('/showdata')
def showdata():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    select_sql = 'select * from user_master'
    result = []
    for row in c.execute(select_sql):
        result.append(row)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')