# Import necessary libraries
from flask import Flask, render_template, Response
import numpy as np
import cv2
from pyzbar.pyzbar import decode

# Initialize Flask application
app = Flask(__name__)


class BarcodeDetector:
    """
    A class used to represent a Barcode Detector that captures video from a webcam,
    detects barcodes in the frames, decodes the text in the barcodes, and displays
    the text on the frame.

    Attributes
    ----------
    camera : cv2.VideoCapture
        A video capture object to access the webcam.
    mydata : str
        The decoded text from the detected barcode.

    Methods
    -------
    gen_frames()
        Captures video frames, detects and decodes barcodes, annotates the frames,
        and yields them for streaming.
    """

    def __init__(self):
        """
        Initializes the BarcodeDetector with a video capture object and sets the
        camera resolution.
        """
        self.camera = cv2.VideoCapture(0)
        self.camera.set(3, 640)  # Set width to 640
        self.camera.set(4, 480)  # Set height to 480

    def gen_frames(self):
        """
        Generator function that captures video frames, detects barcodes,
        decodes the text, annotates the frames with the decoded text, and
        yields the frames for streaming.

        Yields
        ------
        bytes
            The next video frame encoded as JPEG in bytes.
        """
        while True:
            success, frame = self.camera.read()  # Read the camera frame
            if not success:
                break  # Exit if there's a problem with the camera feed

            # Detect and decode barcodes in the frame
            for barcode in decode(frame):
                # Decode barcode data
                mydata = barcode.data.decode('utf-8')

                # Get barcode polygon points and draw it on the frame
                points = np.array([barcode.polygon], np.int32)
                points = points.reshape((-1, 1, 2))
                cv2.polylines(frame, [points], True, (255, 0, 255), 3)

                # Get the bounding box of the barcode and put the text on the frame
                rect = barcode.rect
                cv2.putText(frame, mydata, (rect[0], rect[1]), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (225, 0, 255), 4)

            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    """
    Renders the homepage.

    Returns
    -------
    str
        The rendered HTML of the homepage.
    """
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    """
    Provides the video feed for the client.

    Returns
    -------
    Response
        The streaming response containing the video frames.
    """
    detector = BarcodeDetector()
    return Response(detector.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    # Run the Flask app in debug mode, accessible from any host
    app.run(debug=True, host='0.0.0.0')
