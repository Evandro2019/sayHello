from flask import Flask, render_template, request, flash
#>>pip install  gunicorn
#>>echo > Procfile
#edit Procfile>>web: gunicorn app:app
#>>pip freeze > requirements.txt
#>>pip install MarkupSafe
#edit requirements>>MarkupSafe==2.0.1
#deploy to a github repo

app = Flask(__name__)
app.secret_key = "mahavakya"

@app.route("/hello")
def index():
    flash("yupiii, Whats your name?")    
    return render_template("index.html")

@app.route("/greet",methods=["POST", "GET"])
def greet():
    #request.form['name_input']
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    flash("What are you thinking right now?")
    return render_template("index.html")

app.run(host='localhost', port=5000)
    

