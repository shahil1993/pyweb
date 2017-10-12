from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp',methods=['POST'])
def showSignUp():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

