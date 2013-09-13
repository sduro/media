#!/bin/bash

# Change directory to where your media is
cd /home/pi/usb/torrent/completed

# Show instructions to play choosen media
echo ===============================================
echo --- Enter a number to choose a file to play---
echo ===============================================
# Displays a list of files in current directory and prompt for which
# file to play

# Set the prompt for the select command
PS3="Enter a number or 'q' to quit: "

OLD_IFS=${IFS}; #ifs space seperator
IFS=$'\t\n' #change ifs seperator from spaces to new line, dont mangle file names

# Create a list of files to display
fileList=$(find . -maxdepth 10 -type f | sort | grep -i '\.avi$\|\.mp4$\|\.mkv$\|\.mpg$\|\.mpeg$\|\.flv$')

# Show a menu and ask for input. If the user entered a valid choice,
# then invoke the program on that file
select fileName in $fileList; do
        if [ -n "$fileName" ]; then
                #omxplayer -o hdmi ${fileName} #para sacar HDMI
                omxplayer --win "00 105 1280 620" ${fileName}
        fi
IFS=${OLD_IFS}
        break
done
