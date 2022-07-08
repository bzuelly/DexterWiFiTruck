'''
Parts of this Code created by Matt Richardson 
for details, visit:  http://mattrichardson.com/Raspberry-Pi-Flask/inde...
'''

from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO

IN1 = 25
IN2 = 24
ENA = 23
IN3 = 17
IN4 = 27
ENB = 22

GPIO.setmode(GPIO.BCM)

def startup():
    # Create a dictionary called pins to store the pin number, name, and pin state:
    pins = {
        25 : {'name' : 'GPIO 25: IN1', 'state' : GPIO.LOW},
        24 : {'name' : 'GPIO 24: IN2', 'state' : GPIO.LOW},
        23 : {'name' : 'GPIO 23: ENA', 'state' : GPIO.HIGH},
        17 : {'name' : 'GPIO 17: IN3', 'state' : GPIO.LOW},
        27 : {'name' : 'GPIO 27: IN4', 'state' : GPIO.LOW},
        22 : {'name' : 'GPIO 22: ENB', 'state' : GPIO.LOW}
        }

       # Set each pin as an output and make it low:
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    return pins

app = Flask(__name__)
@app.route("/")
#def hello():
#   now = datetime.datetime.now()
#   timeString = now.strftime("%Y-%m-%d %H:%M")
#   templateData = {
#      'time': timeString,
#      }
#   return render_template('index.html', **templateData)

@app.route("/forward")
def forward():
    startup()
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(ENA,GPIO.HIGH)
    #GPIO.cleanup()
    return render_template('index.html')

@app.route("/reverse")
def reverse():
    startup()
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(ENA,GPIO.HIGH)
    #GPIO.cleanup()
    return render_template('index.html')

@app.route("/stop")
def stop():
    GPIO.output(ENA,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    #GPIO.cleanup()
    return render_template('index.html')

@app.route("/left")
def left():
    startup()
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
    GPIO.output(ENB,GPIO.HIGH)
    #GPIO.cleanup()
    return render_template('index.html')

@app.route("/right")
def right():
    startup()
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    GPIO.output(ENB,GPIO.HIGH)
    #GPIO.cleanup()
    return render_template('index.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
