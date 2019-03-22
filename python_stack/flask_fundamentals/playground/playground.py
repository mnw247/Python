from flask import Flask, render_template   
app = Flask(__name__)    

@app.route('/')
def home():
    return "Main Page"  

@app.route('/play')
def play():
    return render_template("index.html", num = int(3))

@app.route('/play/<x>')
def play_x(x):
    return render_template("index.html", num = int(x))

@app.route('/play/<x>/<color>')
def play_x_color(x,color):
    return render_template("index.html", num = int(x), color = color )  
                      
app.run(debug=True)    
