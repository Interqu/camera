import cv2 
from flask import Flask, render_template, Response
import numpy as np
import urllib

app = Flask(__name__)


camera = cv2.VideoCapture("test.mov")


def gen_frames():
    count = 0

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            cv2.imwrite("./frames/frame%d.jpg" % count, frame)
            count += 1    

            # ret, buffer = cv2.imencode('.jpg', frame)
            # frame = buffer.tobytes()
            # yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            # frame = buffer.tobytes()
            # yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
   
if __name__ == '__main__':
    app.run(debug=True)


