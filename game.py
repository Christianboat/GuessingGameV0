print("WELCOME TO THE GUESSING GAME!!!")
print("Guess the correct number between 0 and 100")

from flask import Flask, render_template, request
import random

app = Flask(__name__)
correct_number = random.randint(1, 100)
attempts = 10

@app.route('/', methods=["POST", "GET"])
def home():
    global correct_number, attempts
    message= None
    if request.method=="POST":
        if "try-again-btn" in request.form:
            correct_number = random.randint(1, 100)
            attempts = 10
            return render_template("index.html", message=None)
        if attempts!=0:
            try:
                guess = int(request.form["guess"])
                if guess == correct_number:
                    message=f"Correct!!! {guess} is the correct number"
                    correct_number = random.randint(1, 100)
                    attempts=10
                elif guess < correct_number:
                    message = f"Too low!!!! {attempts} attempts left"
                    attempts-=1
                else:
                    message=f'Too high {attempts} left'
                    attempts-=1
            except ValueError:
                message = 'Enter a valid number'
        else:
            return render_template("gameover.html")
    return render_template("index.html", message=message)

@app.route("/try-again", methods=["POST"])
def try_again():
    global correct_number, attempts
    correct_number = random.randint(1, 100)
    attempts = 10
    return render_template("index.html", message=None)

if __name__=="__main__":
    app.run(debug=True)