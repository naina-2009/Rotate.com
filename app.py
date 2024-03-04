import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
	img_file = request.files['file']
	degree = int(request.form['text'])
	filename = secure_filename(img_file.filename)
	img_file.save(os.path.join('static/', filename))
	image = Image.open(img_file)
	img_rotation = image.rotate(degree)
	img_rotation.save(os.path.join('static/', 'rotated_img.jpg'))
	img_rotate = 'rotated_img.jpg'
	return render_template('upload.html', filename = img_rotate)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run()
