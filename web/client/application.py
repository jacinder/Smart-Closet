from flask import Flask, render_template, Response, request, redirect, url_for
import sys
import os
import cv2

import camera

application = Flask(__name__, static_folder='static')
# @application.route("/")
# def hello():
#     return render_template("home.html")

# @application.route("/")
# def hello():
#     return render_template("closet.html")

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/closet")
def closet():
    return render_template("closet.html")

@application.route("/closet_1")
def closet_1():
    filenames = os.listdir('static/images/c1')
    return render_template("closet_1.html", items = filenames )

@application.route("/camera")
def camera_test():
    return render_template("camera.html")

@application.route('/video_feed')
def video_feed():
    return Response(camera.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@application.route('/',methods=['POST','GET'])
def tasks():
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            camera.setCapture(1) 
        elif  request.form.get('stop') == 'Stop/Start':
            if(camera.getSwitch() == 1):
                camera.setSwitch(0)
                camera.getCam().release()
                cv2.destroyAllWindows()    
            else:
                camera.getCam().cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                camera.setSwitch(0)
    elif request.method=='GET':
        camera.getCam().release()
        cv2.destroyAllWindows()     
        return render_template('index.html')
    return render_template('index.html') 


# @application.route("/closet_detail")
# def closet_detail():
#     return render_template("closet_detail.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0')

camera.getCam().release()
cv2.destroyAllWindows() 