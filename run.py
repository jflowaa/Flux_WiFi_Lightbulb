#!/usr/bin/env python
from flask import Flask, render_template, url_for, request, flash
from flask.ext.bootstrap import Bootstrap
from light import LightControl


app = Flask(__name__)
bootstrap = Bootstrap()
bootstrap.init_app(app)
app.secret_key = "alkja234lkl234asdufasf"
lightcontrol = LightControl("192.168.35.184", 5577)
status, color = lightcontrol.get_status(), "#9788FF"


@app.route('/', methods=['GET', 'POST'])
def index():
    global color
    if request.method == 'POST':
        if request.form.get("power"):
            change_power_state()
            flash("Turning the Light {}".format(status))
        if request.form.get("update"):
            change_color(request.form.get("color"))
            flash("Applying Color Settings")
        else:
            if request.form.get('red'):
                change_color("#FF0000")
                flash("Changing to Red")
            if request.form.get('green'):
                change_color("#00FF00")
                flash("Changing to Green")
            if request.form.get('blue'):
                change_color("#0000FF")
                flash("Changing to Blue")
            if request.form.get('warm'):
                change_color("#000000")
                flash("Changing to Warm")
                color = "#FFFFFF"
    print(status)
    return render_template("index.html", status=status, color=color)


def change_power_state():
    global status
    if lightcontrol.get_status() == "On":
        lightcontrol.turn_off()
    else:
        lightcontrol.turn_on()
    status = lightcontrol.get_status()



def change_color(c, br=0):
    global color
    color = c
    c = c.replace("#", "")
    red = _to_hex(c[:2])
    green = _to_hex(c[2:4])
    blue = _to_hex(c[-2:])
    lightcontrol.change_color(red, green, blue)


def _to_hex(value):
    return int(value, 16)


if __name__ == "__main__":
    app.run(debug=True)
