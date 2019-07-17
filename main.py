from flask import Flask
from flask import Request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    xuxu = ['xuxi','xuxu','xuxaki']
    return render_template('index.html', list = xuxu)

if __name__== '__main__':
    app.run(debug=True, port=8000)
