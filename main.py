from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Word : %s" %request.method

@app.route("/shetu",methods=['GET', 'POST'])
def shetu():
    if request.method =='POST':
        return "You are using POST"
    else:
        return "You are probably using GET"
@app.route('/profile/<username>')
def profile(username):
    return "Hey it is  % s" % username

if __name__ == "__main__":
    app.run( host='0.0.0.0',debug=True)