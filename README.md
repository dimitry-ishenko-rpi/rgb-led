# Raspberry Pi RGB LED Strip Controller

Control RGB LED Strip through a web browser.

## Getting Started

### Prerequisites

* [Raspberry Pi](https://www.raspberrypi.org/)
* [Python pip](https://pypi.org/project/pip/)
* [pigpio library](http://abyz.me.uk/rpi/pigpio/)
* [Flask](http://flask.pocoo.org/)
* [flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)

### Installation

1. Install Raspbian.
2. Install prerequisites.
```bash
sudo apt install python3-pip pigpio
sudo pip3 install flask flask-socketio eventlet pigpio
```
3. Install custom pigpiod service.
- Edit pigpiod service file:
```bash
nano /etc/systemd/system/pigpiod.service
```
- Paste the following in it:
```ini
[Unit]
Description=pigpio daemon

[Service]
ExecStart=/usr/bin/pigpiod -g

[Install]
WantedBy=multi-user.target
```
- Save and exit
- Enable and start the service:
```bash
sudo systemctl enable pigpiod.service
sudo systemctl start pigpiod.service
```
4. Download and install this repository.
```bash
```

### Usage

From within the project directory run:

```bash
python3 app.py
```

## Authors

* **Dimitry Ishenko** - dimitry (dot) ishenko (at) (gee) mail (dot) com

## License

This project is distributed under the GNU GPL license. See the
[LICENSE.md](LICENSE.md) file for details.

