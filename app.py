from flask import Flask, redirect, url_for, request, render_template, session
import pg8000

"""
def get_db_connection():
    con = pg8000.connect(database="Tests_DB",
                           user="Paloonya",
                           password="01012003",
                           host="127.0.0.1",
                           port="5432"
                           )
    cur = con.cursor()
    cur.execute("SELECT ques from quest_raw")
    rows = cur.fetchall()
    for row in rows:
        print("Question: ", row[0])
    con.close()
"""

app = Flask(__name__)


@app.get("/", endpoint="index_page")
def index_page():
    return render_template("index.html")


@app.get("/users/", endpoint="users_page")
def users_page():
    return render_template("users.html")


@app.get("/questions/", endpoint="question_page")
def quest_page():
    return render_template("quest.html")


@app.get("/tests/", endpoint="tests_page")
def tests_page():
    return render_template("tests.html")


@app.get("/temp/", endpoint="temp_page")
def temp_page():
    return render_template("temp.html")


if __name__ == "__main__":
    app.run(debug=True)
