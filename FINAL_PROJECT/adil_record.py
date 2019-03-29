import pyaudio
import wave
import numpy as np
import soundfile as sf
from python_speech_features import mfcc
import os
import bluetooth


WAVE_OUTPUT_FILENAME = "testab.wav"
nIn = 4043
nOut = 5
c = WAVE_OUTPUT_FILENAME

def record():
	os.system('arecord -d 2 testab.wav');
	data, samplerate = sf.read(c)
	x= len(data)
	p = 25000-x
	l = 0
	tests = np.empty([200,4043])
	new_data = np.empty([25000,])
	y1 = np.empty([25000,])	

	y = p/2;

	for i in range(0,y-1):
		new_data[i] = y1 [i]
	for i in range(y,25000-p+y-1):
		new_data[i] = data[i-y]
	for i in range(25000-y,24999):
	    new_data[i] = y1[i]
	data1 = mfcc(new_data,samplerate)
	data = data1
	data = data.reshape(4043,)
	x = data

	return x	


def sigmoid(x):
    x = np.array(x,dtype=np.float128)
    x = x.reshape(nOut,1)
    x = x
    for  i in range (0,5):
	if x[i] < -700:
	    x[i]=0
	else:
	    x[i] = 1/(1+np.exp(-x[i]))	
    x=x.reshape(-1,nOut)
    return x


def nn_forward(X, W1, b):
    x = X.reshape(-1, nIn)
    #print x.shape
    layer2 = np.dot(x,W1) + b
    out = sigmoid(layer2)
    #losses1.append(loss)
    return out

W1 = np.loadtxt('W1.out',delimiter = ',')
b = np.loadtxt('b.out',delimiter = ',')
q = np.empty([5,])

def prediction():
	data = record()
	pred = np.argmax(nn_forward(data, W1, b))

	q[pred] +=1 
	 
	print("Prediction: Type {}".format(pred))

	if(pred==0):
		print pred,'back'
	if(pred==1):
		print pred,'forward'
	if(pred==2):
		print pred,'left'
	if(pred==3):
		print pred,'right'
	if(pred==4):
		print pred,'stop'

	return pred

			
