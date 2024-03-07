from flask import Flask,render_template,request,url_for,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/',methods=["POST"])
def homepage():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signupform.html')

@app.route('/signup',methods=["POST"])
def signup_post():
    if request.method=='POST':
        First_Name = request.form.get('first_name')
        Last_Name = request.form.get('last_name')
        Email_id= request.form.get ('email')
        Contact = request.form.get ('contact')
        Password = request.form.get ('password')
        Confirm_Password=request.form.get('confirm_password')
        if all([First_Name, Last_Name, Email_id, Contact, Password, Confirm_Password]):
            # Form submission is successful, redirect to login page
            return redirect(url_for('login_page'))
        else:
            # Form submission failed, render the signup form again
            return redirect(url_for('signup'))
    return render_template('signupform.html')


@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login_page',methods=["POST","Get"])
def login_post():
    if request.method=='POST':
        Email = request.form.get('email')
        Password = request.form.get('password')
        if Email=='Email_id' and Password=='Password':
           return redirect(url_for('owner'))
        else:
            # Username or Password is incorrect, try again
            return redirect(url_for('login_page'))
    return render_template('login.html')

    
@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/owner',methods=["GET","POST"])
def owner():
    return render_template('owner.html')

if __name__ == '__main__':
    app.run(debug=True)
