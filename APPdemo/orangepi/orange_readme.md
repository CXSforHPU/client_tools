# OrangePi.GPIO

This is a modified version of **RPi.GPIO** for Orange Pi Boards.

It is based on the original [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO).

## Manual Installation

    sudo apt-get update
    sudo apt-get install python-dev git
    git clone https://github.com/Pako2/OrangePi.GPIO.git
    cd OrangePi.GPIO
    sudo python setup.py install 
    OR (for H6 boards Lite2, One Plus and "3"): 
    sudo python setup.py install --force-h6

## Supported Boards

* OPi Zero (as ZERO)
* OPi Zero Plus (as ZEROPLUS)
* OPi Zero Plus2 H3 (as ZEROPLUS2H3)
* OPi Zero Plus2 H5 (as ZEROPLUS2H5)
* OPi R1
* OPi PC & PC Plus (as PCPCPLUS)
* OPi One (as ONE)
* OPi Lite (as LITE)
* OPi PC2
* OPi Prime (as PRIME)
* OPi Lite2 (as LITE2)
* OPi One Plus (as ONEPLUS)
* OPi 3 (as THREE)

## Usage

Same as RPi.GPIO but with a new function to choose OrangePi Board.

    import OPi.GPIO as GPIO
    GPIO.setboard(GPIO.ZEROPLUS)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, 1)

Many demo is on the example folder
