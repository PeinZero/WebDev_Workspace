from flask import Flask, render_template, request

app = Flask( __name__ )
logged_in = False
# @app.route('/')
# def checker():
#     return render_template("checker.html")
@app.route('/')
def homepage():
    email = request.args.get('email')
    password = request.args.get('password')
    if email == 'mahadzx@gmail.com' and password =='12345':
        global logged_in
        logged_in = True
    return render_template("homepage.html" , logged_in = logged_in)

@app.route('/pageOne')
def pageOne():
    return render_template("one.html", logged_in = logged_in)

@app.route('/pageTwo')
def pageTwo():
    return render_template("two.html", logged_in = logged_in)

@app.route('/pageThree')
def pageThree():
    return render_template("three.html", logged_in = logged_in)

@app.route('/login')
def login():
    return render_template("login.html", logged_in = logged_in)

@app.route('/signup')
def signup():
    return render_template("signup.html", logged_in = logged_in)

# @app.route('/')
# def checker():
#     return render_template("checker.html")


if __name__ == '__main__':
    app.run( debug = True)
