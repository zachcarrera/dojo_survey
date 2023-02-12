from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = "password"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def submit_form():
    for key in request.form.keys():
        print(key)
        session[key] = request.form[key]
    return redirect("/result")


@app.route("/result")
def show_result():
    print(session)
    return render_template("results.html")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
