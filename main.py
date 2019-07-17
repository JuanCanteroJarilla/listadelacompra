from flask import Flask
from flask import Request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    xuxu = 'xuxi'
    return render_template('index.html', xuxu = xuxu)

if __name__== '__main__':
    app.run(debug=True, port=8000)
