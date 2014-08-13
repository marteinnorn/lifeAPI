#!/usr/bin/python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------------------------------------------------------
# DESCRIPTION
# --------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
# --------------------------------------------------------------------------------------------------------------------------------------------
# AUTHORS
# --------------------------------------------------------------------------------------------------------------------------------------------

__authors__ = ['marteinn']

# --------------------------------------------------------------------------------------------------------------------------------------------
# IMPORTS
# --------------------------------------------------------------------------------------------------------------------------------------------

import os
import random
import treeSpeaker
import urllib2
from flask import Flask

# --------------------------------------------------------------------------------------------------------------------------------------------
# PATHS
# --------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------
# GLOBAL VARIABLES/OBJECTS
# --------------------------------------------------------------------------------------------------------------------------------------------

app = Flask(__name__)
basePath = __file__.rstrip(__name__+'.py')
soundFiles = basePath + 'static/sounds'
imageFiles = basePath + 'static/images'

# --------------------------------------------------------------------------------------------------------------------------------------------
# CODE
# --------------------------------------------------------------------------------------------------------------------------------------------


def getRandomImage():

    allFiles = []
    for path, dirs, files in os.walk(imageFiles):
        for eachFile in files:
            if 'jpg' in eachFile:
                allFiles.append(path+'/'+eachFile)

    randomImage = allFiles[random.randint(1,(len(allFiles))-1)]
    randomImage = randomImage.split('images/')[-1].split('.j')[0]

    return randomImage


# --------------------------------------------------------------------------------------------------------------------------------------------
# FLASK CODE
# --------------------------------------------------------------------------------------------------------------------------------------------


@app.route('/instagram')
def instagram():

    images = 45 # how many images do you want
    page =  '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <title>instagram images</title>
            </head>
            <body style="background-color:#FFFFFF;color:#FFFFFF;clear:both;text-align:center;">
                <div style="height:50px;"></div>
            '''
    for eachImage in range(1,images+1):
        page += '<iframe height="200" width="200" src="image" allowTransparency="true" scrolling="no" frameborder="0" ></iframe>'
    page += '</body>\n</html>'

    return page



@app.route('/image')
def image():

    page =  '''
            <!DOCTYPE html>
            <html lang="en">
                <head>
                <meta name="pics", charset="UTF-8", http-equiv="refresh" content="'''+ str(random.randint(16,32)) +'''">
                <title>Image with fade in</title>
                <style type="text/css">
                    body{
                        color:#FFFFFF;
                    }
                </style>
                    <script src="http://www.google.com/jsapi"></script>
                    <script> google.load("jquery", "1"); google.load("jqueryui", "1");</script>
                    <script>
                        $(document).ready(function(){
                            $('body').hide().fadeIn(7000);
                        });
                    </script>
                </head>
            <body style="background-color:#FFFFFF;color:#FFFFFF;clear:both;text-align:center;">
                <div    class="backstretch"
                        style="left: 0px; top: 0px; overflow: hidden; margin: 0px;
                        padding: 0px; height: 200px; width: 200px; z-index: -999999;
                        position: fixed;">
                    <img    style="position: absolute; margin: 0px; padding: 0px; border: none;
                            width: 200px; height: 200px; max-width: none; z-index: -999999;
                            left: 0px; top: 0px;" src="static/images/'''+getRandomImage()+'''.jpg">
                </div>
            </body>
            </html>
            '''

    return page



@app.route('/imageSpeak')
def imageSpeak():

    randomImage = getRandomImage()
    print randomImage
    urllib2.

    # use the name of the file to generate a sound file
    imageTalk = randomImage.split('static/')[-1].split('.j')[0]
    # removes the "by <user>" that instagram adds to posted pics
    imageTalk = imageTalk.split('by ')[0]
    # then generate the soundfile
    treeSpeaker.textToFile(imageTalk,path=soundFiles)

    return  '''
            <!DOCTYPE html>
            <html lang="en">
                <head>
                <meta name="pics", charset="UTF-8", http-equiv="refresh" content="'''+ str(random.randint(16,32)) +'''">
                <title>Image with fade in and speech</title>
                <style type="text/css">
                    body{
                        font-family:Sans-serif;
                        color:#FFFFFF;
                    }
                </style>
                    <script src="http://www.google.com/jsapi"></script>
                    <script> google.load("jquery", "1"); google.load("jqueryui", "1");</script>
                    <script>
                        $(document).ready(function(){
                            $('body').hide().fadeIn(7000);
                        });
                    </script>
                </head>
            <body style="background-color:#FFFFFF;color:#FFFFFF;clear:both;text-align:center;">
                <div    class="backstretch"
                        style="left: 0px; top: 0px; overflow: hidden; margin: 0px;
                        padding: 0px; height: 200px; width: 200px; z-index: -999999;
                        position: fixed;">
                    <img    style="position: absolute; margin: 0px; padding: 0px; border: none;
                            width: 200px; height: 200px; max-width: none; z-index: -999999;
                            left: 0px; top: 0px;" src="static/images/'''+str(randomImage)+'''.jpg">
                    <div></div>
                    <audio src="static/sounds/text.mp3" autoplay></audio>
                </div>
            </body>
            </html>
            '''

def runServer():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    runServer()