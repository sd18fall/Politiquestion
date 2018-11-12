from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import redirect, url_for, request

@app.route('/')
def hello():
    return render_template('zipcode.html')

@app.route('/success/<ZIP>')
def success(ZIP):
    return redirect(url_for('questions'))

@app.route('/findrep', methods = ['POST', 'GET'])
def zipentry():
    if request.method == 'POST':
        if request.form['ZIP']=='':
            return render_template('Error.html')
        
        else:
            ZIP = request.form['ZIP']
            return redirect(url_for('success', ZIP=ZIP))
        
@app.route('/questions', methods = ['POST', 'GET'])
def questions():
    render_template('ZIPquestionaire.html')
    if request.method == 'POST':
        if request.form['Q1']=='':
            return render_template('Error.html')
        else:
            Q1 = request.form['Q1']
            RepScore = 'Yes'
            return redirect(url_for('viewresults', RepScore = RepScore, UserScore=Q1))
    else:
        return render_template('Error.html')
    
@app.route('/results')
def results(RepScore, UserScore):
    return render_template('Results.html', RepScore = RepScore, UserScore=UserScore)

if __name__ == '__main__':
    app.run()