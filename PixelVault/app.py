from flask import Flask, render_template, request, redirect, send_file, url_for, flash, session
from steg import encode_text_into_image, decode_text_from_image
import os

app = Flask(__name__)
app.secret_key = 'stego_secret'  # Needed for flashing messages
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    image = request.files['image']
    text = request.form['text']
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    encoded_path = encode_text_into_image(image_path, text)
    return send_file(encoded_path, as_attachment=True)

@app.route('/decode', methods=['POST'])
def decode():
    image = request.files['image']
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    decoded_text = decode_text_from_image(image_path)
    session['decoded_text'] = decoded_text
    return redirect(url_for('result'))

@app.route('/result')
def result():
    decoded_text = session.get('decoded_text', '')
    return render_template('result.html', decoded_text=decoded_text)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
