# Vodafone Reconnector

It's a selenium-based reconnection script that solves the problem of multiple uninterrupted downloads on JDownloader.

Every part of the whole file is blocked from time to time and you have to wait (also 1 hour) to restart the download. JDownloader offers automatic reconnection, but his scripts doesn't work for Vodafone Station Revolution.


## Installation

Simply you have to find "reconnection method" in JDownloader and select "external reconnection tool". So, you can create an .exe with PyInstaller and directly select the reconnector.exe to launch in reconnection method. 

## Usage
First, you have to set your vodafone station admin password here:
```python
password = ""  # put here your vodafone station password
```
-> It isn't your internet connection password! 

Then, you can create an .exe with PyInstaller, work correcly also with warnings.
```bash
pip install PyInstaller
PyInstaller --onefile reconnect.py
```
The .exe will be generated in dist folder.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This software is free.
[GPL](http://www.gnu.org/licenses/gpl.html)
