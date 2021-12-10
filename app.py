from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = '123'

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/login')    
def login():
    return render_template('signin.html')

@app.route('/register')
def register():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return render_template('signout.html')

@app.route('/essaytopic')
def essaytopic():
    return render_template('essaytopic.html')

@app.route('/howto')
def howto():
    return render_template('howto.html')

@app.route('/gandhi')
def gandhi():
    return render_template('gandhi.html')

@app.route('/aids')
def aids():
    return render_template('aids.html')

@app.route('/alcoholism')
def alcoholism():
    return render_template('alcoholism.html')

@app.route('/ambedkar')
def ambedkar():
    return render_template('ambedkar.html')

@app.route('/anna')
def anna():
    return render_template('anna.html')

@app.route('/apj')
def apj():
    return render_template('apj.html')

@app.route('/bharathiyar')
def bharathiyar():
    return render_template('bharathiyar.html')

@app.route('/computer')
def computer():
    return render_template('computer.html')

@app.route('/differentlyabled')
def differentlyabled():
    return render_template('differentlyabled.html')

@app.route('/discipline')
def discipline():
    return render_template('discipline.html')

@app.route('/radhakrishnan')
def radhakrishnan():
    return render_template('dr.radhakrishnan.html')

@app.route('/evdevelopment')
def evdevelopment():
    return render_template('evdevelopment.html')

@app.route('/girlsedu')
def girlsedu():
    return render_template('girlsedu.html')

@app.route('/globalization')
def globalization():
    return render_template('globalization.html')

@app.route('/globalwarming')
def globalwarming():
    return render_template('globalwarming.html')

@app.route('/internet')
def internet():
    return render_template('internet.html')

@app.route('/kaithemillath')
def kaithemillath():
    return render_template('kaithemillath.html')

@app.route('/kalpanachawla')
def kalpanachawla():
    return render_template('kalpanachawla.html')

@app.route('/kamarajar')
def kamarajar():
    return render_template('kamarajar.html')

@app.route('/kumaran')
def kumaran():
    return render_template('kumaran.html')

@app.route('/narayanamoorthi')
def narayanamoorthi():
    return render_template('narayanamoorthi.html')

@app.route('/nehru')
def nehru():
    return render_template('nehru.html')

@app.route('/periyar')
def periyar():
    return render_template('periyar.html')

@app.route('/press')
def press():
    return render_template('press.html')

@app.route('/rainwaterharvesting')
def rainwaterharvesting():
    return render_template('rainwaterharvesting.html')

@app.route('/roleoftn')
def roleoftn():
    return render_template('roleoftn.html')

@app.route('/space')
def space():
    return render_template('space.html')

@app.route('/tamilpatriot')
def tamilpatriot():
    return render_template('tamilpatriot.html')

@app.route('/technology')
def technology():
    return render_template('technology.html')

@app.route('/terasa')
def terasa():
    return render_template('terasa.html')

@app.route('/transcend')
def transcend():
    return render_template('transcend.html')

@app.route('/uniteddivided')
def uniteddivided():
    return render_template('uniteddivided.html')

@app.route('/signup', methods = ["POST", "GET"])
def signup():
  
    if request.method == "POST":
        Username = request.form["Username"]
        EmailId = request.form["EmailId"]
        Password = request.form["Password"]
        try:
            with sqlite3.connect('user.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT into Users (Username, EmailId, Password) values (?, ?, ?)",(Username, EmailId, Password))
                flash('Registered successfully!', 'success')
                
                return render_template('signin.html')        
        except sqlite3.IntegrityError:
            flash("Username/EmailId already exist...", 'warning')
            return render_template('signup.html')
    return render_template('signin.html')

@app.route('/signin', methods = ["POST", "GET"])
def signin():
    
    if request.method == "POST":
        Username = request.form["Username"]
        Password = request.form["Password"]
        with sqlite3.connect('user.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT * from Users where Username = ? and Password = ?", (Username, Password))
            data = cur.fetchone()
            if data:
                session['logged_in'] = True
                for data in cur:
                    session[Username] = data['Username']
                    session[Password] = data['Password']
                return render_template('home.html')
            else:
                session['logged_in'] = False
                flash("Invalid Username / Password...", 'warning')
                return render_template('signin.html')
    return render_template('signin.html')

                    
@app.route('/signout', methods = ["POST"])
def signout():
    Username = request.form['Username']
    EmailId = request.form['EmailId']
    Password = request.form['Password']
    with sqlite3.connect('user.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT * from Users where Username = ? and Password = ?", (Username, Password))
            data = cur.fetchone()            
            if data:
                session['logged_in'] = False
                cur.execute("DELETE from Users where Username = ? and EmailId = ? and Password = ?", (Username, EmailId, Password))
                flash('You logged out!!', 'warning')
                return render_template('signup.html')
            else:
                flash("Invalid Username / Password...", 'warning')
                return render_template('signout.html')
    return render_template('signout.html')

if __name__ == '__main__':
    app.run(debug = True)