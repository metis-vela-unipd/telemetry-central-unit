# Telemetry Central Unit
Central unit for acquisition, communication and memorization of data coming from sensors mounted in different places of the sailboat.
Actual sensors:
- GPS
- Wind sensor

# Usage
Every time the system boots a simple window is opened with a speed and heading indicators meaning that the GPS daemon is started.
In order to start the logging process of GPS data you need just to type into the terminal the following command:
```
startlog
```
New logs are stored into `~/logs/gpx/START_TIME.gpx` where START_TIME is the log start date. Every log is divided into different GPX tracks, and a new track is created when there is no FIX from the GPS module for more than 5 seconds.
To stop the logging process, run:
```
stoplog
```
All the saved logs can be simply mapped with some online visualizer, like [GPS Visualizer](https://www.gpsvisualizer.com).
More information about the behaviour of the system can be found in the [Central Wiki](https://github.com/metis-vela-unipd/telemetry-documentation/wiki).

# Installation Instructions (Raspbian)
First of all, you need to install a daemon to communicate with the GPS module.
We use [gpsd](https://gpsd.gitlab.io/gpsd/index.html), it can be installed with the following line:
```
sudo apt-get install gpsd gpsd-clients
```
If you have problem with the installation of gpsd please refer [here](https://gpsd.gitlab.io/gpsd/installation.html).

The folder structure of this repos maps each folder to a folder on the Raspberry Pi following this pattern:
```
<pi-folder>/filename
```
Where `<pi-folder>` is the last folder of the file path.

To install the files in the appropiate folder copy the folders accordingly to the following scheme:

Repo Folder | R-Pi Folder
------------|------------
autostart/  | /home/pi/.config/autostart
bin/        | /home/pi/bin
default/    | /etc/default
system/     | /etc/systemd/system/
