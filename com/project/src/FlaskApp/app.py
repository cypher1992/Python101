from flask import Flask, render_template, redirect, url_for, request
from com.project.src.FlaskApp.src.TickerCLS import ListTicker
import logging

app = Flask(__name__)
#filename='debug.log'
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    app.logger.info(str(dir(logging)))
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

@app.route('/result',methods =['POST','PUT'])
def resultpage():
    results = request.form
    return render_template('resultstudent.html',result =results)

@app.route('/ticker')
def tickerpage():
    return render_template('tickerrequest.html')

@app.route('/result',methods =['POST','PUT'])
def tickerrequestpage():
    permitted_Tickers = ['BX', 'JPM', 'WFC', 'GS', 'SG']
    notPermitted_Tickers = ['IRAN', 'BB', 'COKE', 'JB']
    lt = ListTicker(tickersPermitted=permitted_Tickers, tickersNotPermitted=notPermitted_Tickers)
    results = request.form
    for ticker in results:
         isNotValid = lt.isNotValidTicker(ticker)
         if(isNotValid):
            app.logger.debug(str(isNotValid))
         else:
            app.logger.debug(str(isNotValid))
    return render_template('tickerpage.html',result =results)

if __name__ == "__main__":
    #app.run(debug=True) - inorder for logger to work need to turn off debug
    app.run()