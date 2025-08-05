from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

IMAGE_FOLDER = os.path.join('static', 'images')
images = os.listdir(IMAGE_FOLDER)
index = 0

@app.route('/', methods=['GET', 'POST'])
def index_page():
    global index
    if request.method == 'POST':
        index = (index + 1) % len(images)
        return redirect(url_for('index_page'))

    image_file = images[index]
    return render_template('index.html', image_file=image_file)

if __name__ == '__main__':
    app.run(debug=True)
