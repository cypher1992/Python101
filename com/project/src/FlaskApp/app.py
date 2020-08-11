from flask import Flask, render_template, redirect, url_for, request

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

@app.route('/profile/admin')
def admin():
    return '<h1>admin page</h1>'

@app.route('/profile/<user>')
def determine_User(user):
    if(user == 'admin' or user == 'Admin'):
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('profile',name=user))

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['usrn']
        password = request.form['password']
        return redirect(url_for('determine_User',user=username))
    else:
        username = request.args.get('usrn')
        password = request.args.get('password')
        return redirect(url_for('determine_User', user=username))

@app.route('/loginpage')
def loginPage():
    return render_template('loginpage.html')

@app.route('/welcomepage/<username>')
def welcomePage(username):
    if (username == "admin" or username == "Admin"):
        return render_template('welcomepage.html',name = "BIGBOSSADMIN")
    else:
        return render_template('welcomepage.html',name = username)

@app.route('/alertpage')
def alertpage():
    return render_template('alertpage.html')

@app.route('/student')
def studentpage():
    return render_template('student.html')

@app.route('/results')
def resultpage():
    return render_template('student.html')

if __name__ == "__main__":
    app.run(debug=True)