from flask import Flask, render_template
import not_db


app = Flask(__name__)


@app.get("/", endpoint="index_page")
def index_page():
    return render_template("index.html")


@app.get("/users/", endpoint="users_page")
def users_page():
    return render_template("users.html", users=not_db.USERS)


@app.get("/questions/", endpoint="question_page")
def quest_page():
    return render_template("quest.html", questions=not_db.QUEST, answers=not_db.ANSW)


@app.get("/tests/", endpoint="tests_page")
def tests_page():
    return render_template("tests.html")


@app.get("/temp/", endpoint="temp_page")
def temp_page():
    return render_template("temp.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, use_debugger=False)
