# pi_accontrol
Some python code for controlling raspberry pi 4B to send ir signal to control my ac.

# Hardware
- Raspberry Pi 4B
- A computer

# Getting started:
1. Install pigpio on raspberry pi
```bash
sudo apt-get install pigpio
```

2. Enable pigpiod service on raspberry pi
```bash
sudo systemctl enable pigpiod
sudo systemctl start pigpiod
sudo systemctl status pigpiod
```

3. Move the python code to raspberry pi(`app.py` and `tmp.py`) and place them in the same directory.

4. Set cronjob for app.py to run at startup
```bash
crontab -e
```

```bash
@reboot /path/to/python3 /path/to/app.py
# Example:
@reboot /usr/bin/python3 /home/pi/pi_accontrol/app.py
```

5. Reboot raspberry pi and check if the service is running
```bash
curl http://localhost:5000/on
```

6. Change the ip in macserv.py to your raspberry pi ip, then run script on your computer
```bash
python3 macserv.py
```

7. Open browser and go to `http://{your-computer-ip}:5000/` to control your ac
