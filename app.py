from flask import Flask,render_template,request,flash,session,redirect,url_for,abort

app = Flask(__name__)

@app.route('/home')
def hello():
    return "<h1>Hello World!<h1>"
if __name__ == "__main__":
    app.run()