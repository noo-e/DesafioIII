from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/quem-somos')
def quemSomos():
    return render_template('quem-somos.html')

app.run(debug = True)