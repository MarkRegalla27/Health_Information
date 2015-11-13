#Outside modules
from flask import Flask, request
from flask import request
from flask import render_template

#My module
from Analyzer import do_my_func  

app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template("Condition_temp.html")

@app.route("/echo")
def echo(): 
    theString = request.args.get('text', '')
    
    if theString.lower() != 'heart attack':
        return 'Sorry, works for Heart Attack only right now!'
    else:
        theString = do_my_func(theString)
        return theString

app.run(debug=True)
if __name__ == "__main__":
    app.run()
