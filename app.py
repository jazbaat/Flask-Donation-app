from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.secret_key = "Pakistan"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app2.sqlite3"
db = SQLAlchemy(app)



class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(80))
    donation = db.Column(db.Integer, nullable=False)
    contact = db.Column(db.String(80), nullable=False)
    time = db.Column(db.DateTime, default=datetime.now())







@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        todo = request.form["todo"]
        session["todo"] = todo
        contact = request.form["contact"]
        session["contact"] = contact
        donation = request.form["donate"]
        session["donate"] = donation
        x = Data(todo=todo, contact=contact, donation=donation)
        db.session.add(x)
        db.session.commit()
        return redirect(url_for("user"))
        
    return redirect(url_for("user"))


@app.route("/account")
def account():
    return render_template("account.html")



@app.route("/humanity")
def humanity():
    return render_template("humanity.html")



@app.route("/user")
def user():
    y = Data.query.all()
    return render_template("todo.html", y=y)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)