from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import redirect, url_for, request
ZIPcode=0
@app.route('/')
def zipentry():
    return render_template('zipcode3.html')
    
@app.route('/ZIP', methods =['POST', 'GET'])
def ZIP():
    Zip = request.form['ZIP'] 
    global ZIPcode
    ZIPcode = Zip
    return redirect(url_for('questions'))

@app.route('/questions', methods = ['POST'])
def questions():
    
    Vote1=Votes[0]
    Vote2=Votes[1]
    Vote3=Votes[2]
    
    return render_template('ZIPquestionaire2.html')
    
@app.route('/results', methods = ['POST', 'GET'])
def results():
    Q1 = request.form['Q1']
    Score = "input variable here"
    return render_template('Results2.html', Score=Score, UserScore=Q1, RepScore="yes")
zipsaved=0
if __name__ == '__main__':
    app.run()