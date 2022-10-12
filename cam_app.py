from flask import Flask, render_template, Response
import cv2
import time
import argparse

app = Flask(__name__)
camera = cv2.VideoCapture(1)  # web camera connected to usb, argument '0' - USB port 0, '1' - USB port 1 etc.



def getFramesGenerator():
    """ Frames generator"""
    while True:
        time.sleep(0.01)    # limit of fps
        success, frame = camera.read()  # Getting frame
        if success:
            frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_AREA)  # Frame size
            _, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n') # adding header for jpeg format


@app.route('/video_feed')
def video_feed():
    """ Get frame from camera and send it to web page"""
    return Response(getFramesGenerator(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """ html page """
    return render_template('index.html')



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000, help="Running port")
    parser.add_argument("-i", "--ip", type=str, default='192.168.1.25', help="Ip address") # default IP address of raspberry pi, can be set as argument at python program run
    args = parser.parse_args()

    app.run(debug=False, host=args.ip, port=args.port) 
