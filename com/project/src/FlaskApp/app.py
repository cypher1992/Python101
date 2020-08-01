from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

@app.route('/anotherpage')
def anotherPage():
    return render_template('templateanotherpage.html')

if __name__ == "__main__":
    app.run(debug=True)