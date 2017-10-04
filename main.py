from flask import Flask, request, render_template

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/', methods=['POST'])
def validation():
    username=request.form['username']
    password=request.form['password']
    ver_password=request.form['verify']
    email=request.form['email']
    name_error=''
    pass_error=''
    email_error=''

    if username=='':
        name_error='Please insert a username.'
    elif len(username)<3 or len(username)>20:
        name_error='Username must be between 3-20 characters.'
    elif ' ' in username:
        name_error='Username may not contain spaces.'

    if password=='':
        pass_error='Please insert a password.'
    elif len(password)<3 or len(password)>10:
        pass_error='Password must be between 3-10 characters.'
    elif ' ' in password:
        pass_error='Password may not contain spaces.'
    elif ver_password != password:
        pass_error='Passwords do not match.'

    if email !='':    
        if len(email)<3 or len(email)>20:
            email_error='Email address must be between 3-20 characters.'
        elif email.count('@') !=1 or email.count('.') !=1:
            email_error='Please insert a valid email address.'

    if name_error=='' and pass_error=='' and email_error=='':
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html',
            username=username, email=email,
            name_error=name_error, pass_error=pass_error, email_error=email_error)

@app.route('/')
def index():
    return render_template('index.html')

app.run()