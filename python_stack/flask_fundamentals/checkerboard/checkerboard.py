from flask import Flask, render_template   
app = Flask(__name__)    

@app.route('/')
def basic8x8(x = 8,y = 8):
    return render_template("checkerboard.html",x = x, y = y)

@app.route('/<x>/<y>')
def size(x,y):
    return render_template("checkerboard.html", x = int(x), y = int(y))

app.run(debug=True)
