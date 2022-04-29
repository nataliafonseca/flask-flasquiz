from flasquiz import app
from flask import render_template
import json
from random import shuffle


@app.route("/")
def index():
    with open("quiz.json") as json_file:
        quiz = json.load(json_file)
        for entry in quiz:
            entry["all_answers"] = entry.get("incorrect_answers")
            entry["all_answers"].append(entry.get("correct_answer"))
            shuffle(entry["all_answers"])
    return render_template("index.html", quiz=quiz)
