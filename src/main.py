from flask import Flask, render_template, request, redirect,flash
from flask.helpers import url_for
import string
import random


# initlizing the flask app
app= Flask(__name__)

#default routing for the app
@app.route("/")
def home():
    return render_template("index.html")
   
@app.route("/generatePassword", methods=['POST'])
def generate_password():
    length = int(request.form['passwordlength'])
    print(length)
    # length = 16
    lowerletters= string.ascii_lowercase
    upperletters =string.ascii_uppercase
    numbers =string.digits
    special_char = string.punctuation

    complete_password =lowerletters+upperletters+numbers+special_char
    password ="".join(random.sample(complete_password,length))
    
    return render_template("index.html", value =password) 


#main function
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0') #for debugging purpose
    #app.run()
    
