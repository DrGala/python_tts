#!/usr/bin/python

# Code base on Python 3.4.3

import urllib, pycurl, os

def downloadFile(url, fileName):
    fp = open(fileName, "wb")
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEDATA, fp)
    curl.perform()
    curl.close()
    fp.close()

def getGoogleSpeechURL(phrase):
    googleTranslateURL = "http://translate.google.com/translate_tts?tl=en&"
    parameters = {'q': phrase}
    data = urllib.parse.urlencode(parameters)
    googleTranslateURL = "%s%s" % (googleTranslateURL,data)
    return googleTranslateURL

def play_mp3(filename):
    command = '%s %s %s' % ('mplayer', filename, ' -af extrastereo=0 &')
    # os.system("mplayer "+filename+"-af extrastereo=0 &")
    print(command)

def speakSpeechFromText(phrase):
    mp3_filename = 'tts.mp3'
    googleSpeechURL = getGoogleSpeechURL(phrase)

    print(googleSpeechURL)
    
    downloadFile(googleSpeechURL, mp3_filename)
    play_mp3(mp3_filename)




speakSpeechFromText("testing, testing, 1 2 3.")
