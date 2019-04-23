from flask import Flask, render_template, request
app = Flask(__name__)

from flask_socketio import SocketIO
socketio = SocketIO(app)

pin_red = 14 # 17 20 23
pin_gre = 15 # 18 21 24
pin_blu = 16 # 19 22 25

import pigpio
pi = pigpio.pi()

pi.set_mode(pin_red, pigpio.OUTPUT)
pi.set_mode(pin_gre, pigpio.OUTPUT)
pi.set_mode(pin_blu, pigpio.OUTPUT)

@app.route("/")
@app.route("/index")
def index(): return render_template("index.html")

@socketio.on("red")
def set_red(value): pi.set_PWM_dutycycle(pin_red, value)

@socketio.on("gre")
def set_grn(value): pi.set_PWM_dutycycle(pin_gre, value)

@socketio.on("blu")
def set_blu(value): pi.set_PWM_dutycycle(pin_blu, value)

if __name__ == '__main__':
    socketio.run(app, host = "0.0.0.0")
