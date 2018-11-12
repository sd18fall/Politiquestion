
from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import redirect, url_for, request

@app.route('/')
def zipentry():
    return render_template('zipcode1.html')
    
@app.route('/ZIP', methods =['POST', 'GET'])
def ZIP():
    ZIP = request.form['ZIP']
    return redirect(url_for('questions'))

@app.route('/questions', methods = ['POST'])
def questions():
    return render_template('ZIPquestionaire1.html')

#@app.route('/questions1', methods = ['POST', 'GET'])    
#def questions1():
       # Q1 = request.form['Q1']
        #return redirect(url_for('results', Q1=Q1))
    
@app.route('/results', methods = ['POST', 'GET'])
def results():
    Q1 = request.form['Q1']
    return render_template('Results1.html', UserScore=Q1, RepScore="yes")

if __name__ == '__main__':
    app.run()
