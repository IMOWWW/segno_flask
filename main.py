from flask import Flask, render_template, request
import segno

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form['data']
    qr = segno.make(data) 
    return render_template('generated.html', qrcode=qr)



if __name__ == '__main__':
    app.run(debug=True)
