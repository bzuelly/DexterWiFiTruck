'''
Parts of this Code created by Matt Richardson 
for details, visit:  http://mattrichardson.com/Raspberry-Pi-Flask/inde...
'''

from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

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



app = Flask(__name__)
@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   left = 'left'
   templateData = {
      'time': timeString,
      }
   return render_template('index.html', **templateData)

@app.route("/forward")
def forward():
    GPIO.output(pins[25],GPIO.HIGH)
    GPIO.output(pins[24],GPIO.LOW)
    GPIO.output(pins[23],GPIO.HIGH)
    GPIO.cleanup()     
    return render_template('index.html')

@app.route("/reverse")
def reverse():
       
    return render_template('index.html')

@app.route("/stop")
def stop():
    GPIO.output(pins[23],GPIO.LOW)
    GPIO.output(pins[24],GPIO.LOW)
    GPIO.cleanup()       
    return render_template('index.html')

@app.route("/left")
def left():
    
    GPIO.cleanup()       
    return render_template('index.html')

@app.route("/right")
def right():
    
    GPIO.cleanup()   
    return render_template('index.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)