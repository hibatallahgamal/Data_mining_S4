from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
      return render_template('index.html')

@app.route("/login")
def login():
      return render_template('login.html')

@app.route("/logout")
def logout():
     return render_template('logout.html')

@app.route("/game")
def game():
     return render_template('game.html')


if __name__ == "__main__":
    app.run (debug=True, port=5008)

