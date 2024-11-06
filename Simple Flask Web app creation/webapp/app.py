# S1 - import flask
from flask import Flask, render_template, request

# S2 - Create flask object
app = Flask(__name__)

# S3 - Craete an endpoint/route and 
# bind each route with some functionality
@app.route("/")
def home() :
    return render_template("home.html")

@app.route("/welcome", methods=['POST'])
def welcome():
    uname = request.form.get("user_name")
    return render_template("welcome.html", uname=uname)

# S4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)