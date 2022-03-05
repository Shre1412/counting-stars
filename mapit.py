#! python3
# mapit.py - Launches a map in the browser using an address from the command line or clipboard

import webbrowser, sys, pyperclip as pc

# Get address from command line
if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])

# Get address from clipboard
else:
    address = pc.paste()

webbrowser.open('https://www.google.co.in/maps/search/' + address)


# Get the street address from the command line arguments or clipboard
# Open the web browser to the Google Maps page for the address
# Read the command line arguments from sys.argv
# Read the clipboard contents
# Call the webbrowser.open() function to open the web browser