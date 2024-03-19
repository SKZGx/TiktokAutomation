import os
from flask import Flask, render_template, request
from moviepy.video.io.VideoFileClip import VideoFileClip

app = Flask(__name__)

# Create input and output folders if they don't exist
input_folder = 'input'
output_folder = 'output'
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    video = request.files['video']
    num_parts = int(request.form['num_parts'])

    # Save the uploaded video to the input folder
    video_path = os.path.join(input_folder, video.filename)
    video.save(video_path)

    # Use moviepy to cut the video into equal parts
    clip = VideoFileClip(video_path)
    duration = clip.duration
    part_duration = duration / num_parts

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for i in range(num_parts):
        start_time = i * part_duration
        end_time = (i + 1) * part_duration
        part = clip.subclip(start_time, end_time)
        
        # Save each part with the specified naming convention
        part_filename = f"{os.path.splitext(video.filename)[0]}_{i + 1}.mp4"
        part_path = os.path.join(output_folder, part_filename)
        part.write_videofile(part_path)

    return "Video has been cut into equal parts!"

if __name__ == '__main__':
    app.run(debug=True)
