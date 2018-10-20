from flask import Flask, render_template, request
from data import Faculties

app = Flask(__name__)

myFaculties=Faculties()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/send', methods=['GET', 'POST'])
def send():

    if (request.method=='POST'):

        getname=request.form['name']
        getemail=request.form['emailid']
        return render_template('contact.html', name=getname, emailid=getemail)


@app.route('/faculties')
def faculties():
    return render_template('faculties.html', sendfact=myFaculties)

if(__name__=='__main__'):
    app.run(debug=True)