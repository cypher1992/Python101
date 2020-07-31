from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

@app.route('/AnotherPage')
def anotherPage():
    return render_template('anotherPage.html')

if __name__ == "__main__":
    app.run()