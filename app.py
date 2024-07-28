from flask import Flask, render_template, request, send_from_directory
from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'

class UploadForm(FlaskForm):
    image = FileField('Upload an Image')
    submit = SubmitField('Upload')

def extract_colors(image_path, num_colors=10):
    image = Image.open(image_path)
    image = image.convert('RGB')
    image_np = np.array(image)
    pixels = image_np.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_
    colors = colors.round(0).astype(int)
    return colors

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    colors = None
    image_filename = None
    if form.validate_on_submit():
        file = form.image.data
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        colors = extract_colors(filepath)
        color_hex = ['#{:02x}{:02x}{:02x}'.format(*color) for color in colors]
        image_filename = filename
        return render_template('index.html', form=form, colors=color_hex, image_filename=image_filename)
    return render_template('index.html', form=form, colors=colors, image_filename=image_filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
