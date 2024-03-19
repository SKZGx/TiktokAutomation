# TiktokAutomation
This Flask web application allows users to upload a video and cut it into multiple equal parts. It uses the MoviePy library to perform the video editing operations.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using pip: ```pip install -r requirements.txt```

## Usage
1. Run the Flask application: ```python app.py```
2. Open your web browser
3. You'll see a form where you can upload a video file and specify the number of parts to cut the video into.
4. Select a video file and enter the desired number of parts.
5. Click the "Cut Video" button to process the video.
6. The processed video parts will be saved in the output folder.

## Configuration
You can configure the following parameters in the app.py file:

* input_folder: Path to the folder containing input videos.
* output_folder: Path to the folder where processed video parts will be saved.
