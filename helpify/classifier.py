#pip install tensorflow
#pip install keras
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import keras

class Classifier():
	model = keras.models.load_model('model.h5')#load this before hand cause it'll take some time to load

	def classify(self, image):
	    img=load_img(image, target_size=(224,224))
	    x=img_to_array(img)
	    x = x/255
	    x=np.expand_dims(x, axis=0)
	    pred = self.model.predict(x)
	    if( pred[0][0] >0.9499 or pred[0][2] > 0.9499):
	        return True
	    else:
	        return False