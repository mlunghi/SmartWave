import time, io, sys, smbus, os, math, firebase_admin
from firebase_admin import credentials
from picamera import PiCamera
import io
from Adafruit_IO import Client, Data
import os
import argparse

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

aio = Client('KUNJD', 'ec48fa5e5a184569a2a7d56e5d26dc52')

cred = credentials.Certificate("/home/pi/Downloads/videvision-221321-7a1fb8dbf7fa.json")
default_app = firebase_admin.initialize_app(cred)

#export GOOGLE_APPLICATION_CREDENTIALS = "/home/pi/Downloads/VideVision-42ad157fe0e6.json"

camera = PiCamera()
camera.resolution = (1024, 768)

client = vision.ImageAnnotatorClient()

def piCam():
    camera.capture('pipic.jpg')

def annotate(path):
    """Returns web annotations given the path to an image."""
    client = vision.ImageAnnotatorClient()

    if path.startswith('http') or path.startswith('gs:'):
        image = types.Image()
        image.source.image_uri = path

    else:
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

    web_detection = client.web_detection(image=image).web_detection

    return web_detection


def report(annotations):

    count = 0

    if annotations.web_entities:
        #print('\n{} Web entities found: '.format(len(annotations.web_entities)))

        for entity in annotations.web_entities:
            if count == 0:
                #print('Score      : {}'.format(entity.score))
                print('Description: {}'.format(entity.description))
                count = 1

                data = Data(value=format(entity.description))
                aio.create_data('microwave', data)


while True:
    piCam()
    parser = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    path_help = str('/home/pi/Desktop/pipic.jpg')

    report(annotate(path_help))

    time.sleep(2)

    




