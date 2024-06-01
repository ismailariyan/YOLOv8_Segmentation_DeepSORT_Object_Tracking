from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
PROCESSED_FOLDER = 'processed/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(PROCESSED_FOLDER):
    os.makedirs(PROCESSED_FOLDER)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        process_video(filepath, filename)
        return redirect(url_for('uploaded_file', filename=filename))
    return

def process_video(filepath, filename):
    output_path = os.path.join(app.config['PROCESSED_FOLDER'], filename)
    command = f'python predict.py source="{filepath}"'
    subprocess.run(command, shell=True)
    # Assuming predict.py saves the processed video in a folder named 'runs'
    processed_file_path = f'runs/{os.path.splitext(filename)[0]}.mp4'
    os.rename(processed_file_path, output_path)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
