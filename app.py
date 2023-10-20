from flask import Flask, abort, flash, redirect, render_template, request, session, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = "ayush"  



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    flash("you are successfuly logged in")  
    return render_template('login.html')


@app.route('/success', methods=['GET', 'POST'])
def success():   
    return render_template('success.html')


@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('session',None)
        return render_template('logout.html')
    else:
         return '<p>user already logged out</p><a href = "/login">Login</a>'


@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('profile.html', name=email)
    else:  
        return '<p>Please login first</p><br><a href = "/login">Login</a>' 


@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST' and request.form['pass'] == '111':  
        session['email'] = request.form['email']
        f = request.files['file'] 
        f.save(f.filename)
        return redirect(url_for("success"))  
    else:  
        abort(401)