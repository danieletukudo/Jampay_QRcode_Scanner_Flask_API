#Import necessary libraries
from flask import Flask, render_template, Response
import cv2
import numpy as np
import cv2
from pyzbar.pyzbar import decode

app = Flask(__name__)

class predict_barcode:

    camera = cv2.VideoCapture(0)
    camera.set(3, 640)
    camera.set(4, 480)

    def gen_frames(self):

        while True:
            success, frame = self.camera.read()  # read the camera frame
            for barcode in decode(frame):
                self.mydata = barcode.data.decode('utf-8')
                point = np.array([barcode.polygon], np.int32)
                point = point.reshape((-1, 1, 2))
                cv2.polylines(frame, [point], True, (255, 0, 255), 3)
                point2 = barcode.rect
                cv2.putText(frame, self.mydata, (point2[0], point2[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 0, 255), 4)

            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    frame = predict_barcode()
    return Response(frame.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0')