# - *- coding: utf- 8 - *-
#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3


# Opens Google Maps to given address
# Cody King
# 7/14/2017


import sys, webbrowser, pyperclip

def main():
    openMap()


def openMap():
    url = ''
    address = ''

    if len(sys.argv) < 2:
        address = pyperclip.paste().replace(' ', '+')

    elif sys.argv[1] == 'help':
        print('Usage: mapit.py [address]')

    else:
        address = '+'.join(sys.argv[1:])


    url = 'https://www.google.com/maps/place/' + address

    webbrowser.open(url)


if __name__ == '__main__':
    main()
