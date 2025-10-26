from flask import Flask
app = Flask(__name__)

@app.route('/')
def INDEX():
    return '<H1>mandhi kazhikkan povam ? jk the image is running yey</H1>'

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)