from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def home():
    return 'Simple message'

if __name__ == '__main__':
    app.run(debug=True)