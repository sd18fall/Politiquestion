from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import redirect, url_for, request

@app.route('/')
def hello():
    return render_template('zipcode.html')

#@app.route('/success/<ZIP>')
#def success(ZIP):
    #render_template('ZIPquestionaire.html')
    #return redirect(url_for('questions'))

@app.route('/questions', methods = ['POST'])
def zipentry():
    if request.form['ZIP']=='':
        return render_template('Error.html')
    else:
        ZIP = request.form['ZIP']
        
        return redirect(url_for('questions', ZIP))
        
@app.route('/questions', methods = ['POST'])
def questions(ZIP):
        render_template('zipcode.html')
        if request.form['Q1']=='':
            return render_template('Error.html')
        else:
            Q1 = request.form['Q1']
            RepScore = 'Yes'
            return redirect(url_for('results', RepScore = RepScore, UserScore=Q1))
    
@app.route('/results')
def results(RepScore, UserScore):
    return render_template('Results.html', RepScore = RepScore, UserScore=UserScore)

if __name__ == '__main__':
    app.run()
