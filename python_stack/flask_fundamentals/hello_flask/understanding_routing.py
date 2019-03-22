from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response.

@app.route('/dojo')
def dojo():
  return "Dojo!" # Return the string 'Dojo' as a response.


@app.route('/say/<name>') # for a route '/hi/____' anything after '/hi/' gets passed as a variable 'name'
def hi(name):
    print(name)
    return "Hi " + name.capitalize()
    
@app.route('/repeat/<num_of_repeats>/<string>') # for a route '/repeat/____/____', two parameters in the url get passed as num_of_repeats and string
def show_user_profile(num_of_repeats, string):
    print(int(num_of_repeats))
    print(string)
    return int(num_of_repeats) * (" " + string)

if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.