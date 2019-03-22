#                      [ Assignment: Dojo Survey  ]
'''
Objectives:
===================================================
<>  Shall building a server with Flask from scratch
<>  Shall pass paas information to the routes
<>  Shall generate different http responses url requests:
========================================================='''

# import the Flask libray
#    module       Class     Method         Method    object
from flask import Flask, render_template, redirect,  request, session

languages = ['Ruby','Python','JavaScript','PHP','HTML','CSS','C++','SQL']
locations = ['Dallas','San Jose','Seattle','Colorado','L.A.']

# Backend server setup
# Object
app = Flask (__name__)
app.secret_key = 'ThisIsSecret'

# index route shall handle form rendering
@app.route ('/')
def index ():
    return render_template("index.html", language=languages, location=locations)

@app.route ('/profile', methods = ['POST'])
def profile ():
    underline = "\n"
    underline = "-" * 13
    session['index'] = request.form['username']
    # Terminal print-debugginh
    print (session['index'])
    print ('Got Post Indo:\n%s\n' % underline)
    print ('Requested user     named: ', request.form['username'])  # Print first name in terminal
    print ('Requested user  location: ', request.form['location'])  # Print email in terminal
    return render_template ('profile.html')                         # Redirects back to index '/'

if __name__ == '__main__':                                          # Run the server applicatin
    app.run (debug = True)
