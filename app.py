from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/on")
def open():
    subprocess.Popen(["python", "tmp.py", "on"])
    return "<p>Opened!</p>"

@app.route("/off")
def close():
    subprocess.Popen(["python", "tmp.py", "off"])
    return "<p>Closed!</p>"

@app.route("/strong")
def strong():
    subprocess.Popen(["python", "tmp.py", "strong"])
    return "<p>Strong!</p>"

@app.route("/16")
def tmp16():
    subprocess.Popen(["python", "tmp.py", "16"])
    return "<p>tmp16!</p>"

@app.route("/22")
def tmp22():
    subprocess.Popen(["python", "tmp.py", "22"])
    return "<p>tmp22!</p>"

@app.route("/26")
def tmp26():
    subprocess.Popen(["python", "tmp.py", "26"])
    return "<p>tmp26!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=False)
    # for i in range(10):
    # send_ir_signal(opencom)
        # time.sleep(50)
        # send_ir_signal(closecom)
        # time.sleep(4)

