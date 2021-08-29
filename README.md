# Network Scanner

     _   _      _                      _          _____                                 
    | \ | |    | |                    | |        / ____|                                
    |  \| | ___| |___      _____  _ __| | __    | (___   ___ __ _ _ __  _ __   ___ _ __ 
    | . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /     \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
    | |\  |  __/ |_ \ V  V / (_) | |  |   <      ____) | (_| (_| | | | | | | |  __/ |   
    |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\    |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                                                                                                                                        

This is a simple network scanner used to scan any range of IP Address to get their MAC Address.

The code is written completely in Python (currently, python v3.10).

This program is supported for Linux, Windows and Mac OS X.

# Installation

Before starting to use this tool you must install some important python packages. You can manually install them one by on or you can use requirements.txt file to install all packages all at once. Use anyone way you want to install required packages.

## Use requirements.txt

    pip install -r requirements.txt

## Install manually

    pip install scapy
    pip install termcolor
    pip install optparse
    
# Usage

### Options to use this Network Scanner
> **This will display the help message**

    python3 network_scanner.py --help

> **This command will scan range of IP Address and show their MAC Address**

    python3 network_scanner.py -t 192.168.29.1/24

![Image of Scanning](https://i.ibb.co/f4bPRsh/scanning.png)

