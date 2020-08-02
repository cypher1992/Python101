from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

@app.route('/anotherpage')
def anotherPage():
    return render_template('anotherpage.html')

@app.route('/profile/<name>')
def profile(name):
    return 'This profile belows to %s' %name

@app.route('/profileID/<int:id>')
def profileID(id):
    return 'This profile ID is %d' %id

if __name__ == "__main__":
    app.run(debug=True)