import os
from urllib import request
from flask import Flask, url_for, redirect, render_template
from forms import formSplineImageVisualization
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename


SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = formSplineImageVisualization()
    
    if form.validate_on_submit():
        filename = secure_filename(form.image_file.data.filename)
        form.image_file.data.save('uploads/' + filename)
        return redirect(url_for('home'))
    
    return render_template('home.html', form=form)
