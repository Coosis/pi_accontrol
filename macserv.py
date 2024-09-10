from flask import Flask, render_template, redirect, url_for
import threading
import subprocess

app = Flask(__name__)

def run_curl(route):
    # This will execute the curl command and run in the background
    curl_command = ['curl', f'http://192.168.8.225:5000/{route}']
    process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output if not error else error

def openac():
    thread = threading.Thread(target=run_curl, args=('on',))
    thread.start()
    print('open')
    return "<p>Opened!</p>"

def closeac():
    thread = threading.Thread(target=run_curl, args=('off',))
    thread.start()
    print('close')
    return "<p>Closed!</p>"

def strong():
    thread = threading.Thread(target=run_curl, args=('strong',))
    thread.start()
    print('strong')
    return "<p>Strong!</p>"

def tmp16():
    thread = threading.Thread(target=run_curl, args=('16',))
    thread.start()
    print('tmp16')
    return "<p>tmp16!</p>"

def tmp22():
    thread = threading.Thread(target=run_curl, args=('22',))
    thread.start()
    print('tmp22')
    return "<p>tmp22!</p>"

def tmp26():
    thread = threading.Thread(target=run_curl, args=('26',))
    thread.start()
    print('down')
    return "<p>Down!</p>"

@app.route('/')
def index():
    return render_template('rac.html')

@app.route('/action/<button>')
def button_action(button):
    if button == 'on':
        openac()
    elif button == 'off':
        closeac()
    elif button == 'strong':
        strong()
    elif button == '16':
        tmp16()
    elif button == '22':
        tmp22()
    elif button == '26':
        tmp26()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9899, threaded=True, debug=False)
