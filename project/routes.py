from project import app
from flask import Flask ,render_template, flash ,redirect,url_for,request
from project.model import Detect
import cv2
import os

#MAIN ROUTE
@app.route('/',methods=['POST','GET'])
def home():

	t  =' '

	if(request.method  == 'POST'):

		if(request.files):

			try:

				img = request.files['image']
				
				if(img == None):
					flash(f'Please choose a file','danger')

				else:

					img.save(os.path.join(app.config["IMAGE_UPLOADS"], img.filename))
					test_img = cv2.imread(os.path.join(app.config['IMAGE_UPLOADS'], img.filename))

					detect_text = Detect(test_img)

					if(detect_text.detect_text() ==  False):
						flash(f'Some Error Occured','danger')
					else:
						t  = detect_text.detect_text()

			except(FileNotFoundError):
				flash(f'File Not Found','danger')


	return render_template('index.html',text = t)