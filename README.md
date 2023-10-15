# AirTagBattery

Apple removed the battery status of AirTags from the FindMy app. This script reads the battery status from the FindMy cache for all AirTags and displays battery level.


## Usage

Make sure the terminal has full disk access:
System Settings > Privacy & Security > Full Disk Access > allow for Terminal (or iTerm)

The FindMy app may need to be opened to receive the battery status of the AirTags before this script is run.

### Python script

1. Make sure all requirements are installed by running `pip3 install -r requirements.txt`.

2. Run `python3 airtag-bat.py`

### Executable

A compiled executable is also located under `dist`.
Simply run `./airtag-bat` from this directory or link/move the executable to `/usr/local/bin`.

![image](docs/output.png)
