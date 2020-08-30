from flask import Flask, render_template, redirect, url_for, request, make_response
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

@app.route('/resultTicker',methods =['POST','PUT'])
def tickerrequestpage():
    app.logger.debug("TESt")
    permitted_Tickers = ['BX', 'JPM', 'WFC', 'GS', 'SG']
    notPermitted_Tickers = ['IRAN', 'BB', 'COKE', 'JB']
    lt = ListTicker(tickersPermitted=permitted_Tickers, tickersNotPermitted=notPermitted_Tickers)
    results = request.form.to_dict()
    dictOfValues = request.form.to_dict()
    listOfValues = dictOfValues.keys()
    app.logger.info(listOfValues)
    for ticker in listOfValues:
         app.logger.debug(ticker)
         isNotValid = lt.isNotValidTicker(results[ticker])
         if(isNotValid):
            app.logger.debug(str(isNotValid))
            app.logger.warn("REMOVING TICKER " + ticker + "WITH VALUE " + results[ticker])
            del results[ticker]
         else:
            app.logger.debug(str(isNotValid))
    return render_template('tickerpage.html',result =results)

@app.route('/loginpagecookie')
def loginpagecookie():
    return render_template('loginpagecookie.html')

@app.route('/setcookie',methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        pw = request.form['pw']
        admin = 'admin'
        password = 'password'
        if(user == admin and password == pw ):
            resp = make_response(render_template('readcookie.html'))
            resp.set_cookie('userID',user)
            return resp
        else:
            return None

@app.route('/getcookie',methods=['POST','GET'])
def getcookie():
    name = request.cookies.get("userID")
    return '<h1>Hello + name + </h1>'

if __name__ == "__main__":
    #app.run(debug=True) - inorder for logger to work need to turn off debug
    app.run()