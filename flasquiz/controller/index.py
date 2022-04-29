from flasquiz import app


@app.route("/")
def index():
    return "Flasquiz"
