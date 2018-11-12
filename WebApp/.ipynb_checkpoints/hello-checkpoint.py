"""A simple "Hello, World" application using Flask."""

from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import redirect, url_for, request

@app.route('/')
def hello():
    return render_template('webform.html')

@app.route('/hello/<name>')
def helloTemplate(name=None):
    return render_template('hello.html', name=name)

@app.route('/success/<name>-<AGE>')
def success(name, AGE):
    Age = AGE
    return render_template('welcome.html', name=name, Age=Age)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['firstname']=='':
            return render_template('Error.html')
        elif request.form['lastname']=='': 
            return render_template('Error.html')
        elif request.form['Age']=='': 
            return render_template('Error.html')
        elif request.form['Ninja']=='': 
            return render_template('Error.html')
        else:
            user = request.form['firstname']
            AGE = request.form['Age']
            return redirect(url_for('success', name = user, AGE=AGE))
    else:
        if request.args.get('firstname')=='': 
            return render_template('Error.html')
        elif request.args.get('lastname')=='': 
            return render_template('Error.html')
        elif request.args.get('Age')=='': 
            return render_template('Error.html')
        elif request.args.get('Ninja')=='': 
            return render_template('Error.html')
        user = request.args.get('firstname')
        AGE= request.args.get('Age')
        return redirect(url_for('success', name = user, AGE=AGE))

if __name__ == '__main__':
    app.run()
