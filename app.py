from flask import Flask, redirect, url_for, request, render_template, session
import pg8000


def get_db_connection():
    con = pg8000.connect(
        database="Tests_DB",
        user="Paloonya",
        password="01012003",
        host="127.0.0.1",
        port="5432",
    )
    cur = con.cursor()
    cur.execute("SELECT ques from quest_raw")
    rows = cur.fetchall()
    for row in rows:
        print("Question: ", row[0])
    con.close()


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    get_db_connection()
    return render_template("index.html")
