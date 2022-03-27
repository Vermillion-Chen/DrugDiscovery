import numpy as np
from skimage import io
import blobfile as bf
import cv2
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask import abort
from flask import jsonify
import json
import pytesseract
import requests 
import urllib
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from io import BytesIO

matplotlib.use('TkAgg')

app = Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
# @cross_origin()
def index():
    return "Hello, World!"

@app.route("/blob", methods=['POST'])
@cross_origin()
def create_task():
     # print(json.loads(request.data))
     url = "https://res.cloudinary.com/dj3ua4rkx/image/upload/v1648361012/" +request.get_json()['link']+".png"
     # url = "https://images.hindustantimes.com/img/2021/08/07/1600x900/honey_singh_2_1628299588937_1628299595558.jpg"
     print(url)
     print("downloading %s" % (url))
     image = io.imread(url)
     print(pytesseract.image_to_string(image))
     # plt.imshow(image)
     # plt.show()
     # cv2.imshow("Correct", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
     # cv2.waitKey(0)
     # img=cv2.imread('test.png',1) 
     # plt.imshow(img) 
     return jsonify({'task':'ga'}), 201

if __name__ == '__main__':
     app.run(debug=True)