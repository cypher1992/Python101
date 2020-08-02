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

if __name__ == "__main__":
    app.run(debug=True)