import json
from random import shuffle
from app import app, db
from app.model.scoreboard import Score
from flask import render_template, request

with open("quiz.json", encoding="utf-8") as json_file:
    quiz = json.load(json_file)
    for entry in quiz:
        entry["all_answers"] = entry.get("incorrect_answers")
        entry["all_answers"].append(entry.get("correct_answer"))
        shuffle(entry["all_answers"])


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", quiz=quiz)


@app.route("/result", methods=["POST"])
def result():
    name = request.form.get("name")
    score_list = []
    for i in range(10):
        if request.form.get(f"question-{i+1}") == quiz[i].get("correct_answer"):
            score_list.append(True)
        else:
            score_list.append(False)
    score = sum(score_list)

    new_score = Score(name, score)
    db.session.add(new_score)
    db.session.commit()

    return render_template(
        "result.html",
        quiz=quiz,
        score_list=score_list,
        score=score,
        name=name,
    )


@app.route("/scoreboard", methods=["GET"])
def scoreboard():
    scoreboard = Score.query.all()
    for score in scoreboard:
        score.date = score.created_at.strftime("%d/%m/%Y %H:%M")
    scoreboard.sort(key=lambda x: x.score, reverse=True)
    return render_template("scoreboard.html", scoreboard=scoreboard)
