from distutils.log import debug
from flask import Flask

app=Flask(__name__)

@app.route("/",methods=(['Get','Post']))
def index():
    return "1st Machine Learning Project"

if __name__ == "__main__":
    app.run(debug=True)