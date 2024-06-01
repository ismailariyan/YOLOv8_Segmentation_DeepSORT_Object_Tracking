from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
PROCESSED_FOLDER = 'D:/BasicProjects/YOLOv8_Segmentation_DeepSORT_Object_Tracking/runs/detect/train'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def upload_form():
    filename = request.args.get('filename')
    return render_template('upload.html', filename=filename)

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
        return redirect(url_for('upload_form', filename=filename))
    return

def process_video(filepath, filename):
    command = f'python predict.py source="{filepath}"'
    subprocess.run(command, shell=True)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename, as_attachment=True, download_name='processed-video.mp4')

if __name__ == "__main__":
    app.run(debug=True)
