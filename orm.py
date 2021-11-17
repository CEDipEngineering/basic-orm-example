#!/usr/bin/env python
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
app = Flask('main')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'cloud'
app.config['MYSQL_DATABASE_DB'] = 'tasks'
app.config['MYSQL_DATABASE_HOST'] = '<DB IP ADDRESS>'
mysql = MySQL(app)
mysql.init_app(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("SELECT nome, saldo FROM user", None)
    data = cur.fetchall()
    cur.close()
    out = f"<main><ul>{''.join([f'<li>{i[0]} has U${i[1]:.02f} in their account</li>' for i in data])}</ul></main>"
    return out
if __name__ == '__main__':
    app.run(host='0.0.0.0')