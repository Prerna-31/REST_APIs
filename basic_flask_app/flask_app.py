from flask import Flask

app = Flask(__name__)   ## Creates an app objet with unique name/id

@app.route('/')   ## a decorator specifies the end-point(url) i.e what has been requested. by default it is get. In
                  ## in order to accept POSt, we need to specify the same--> @app.route('/',methods=['POST'])
def home():
    return "Hello World"

app.run(port = 5000)   ## it tells flask application to run.

