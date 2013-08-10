import numpy
import scipy
from math import pow
from itertools import product
from scipy.io.wavfile import read
from scipy.spatial.distance import cosine
from scipy.signal import decimate
from pylab import plot, show

class MusicData:
    def __init__(self):
        self.positions = list(product(range(width), range(height)))
        self.size = self.positions.__len__()
        self.bufferSize = 2**12 #for getting audio frames
   
    def readwav(self, file):
        self.rate, self.data = read(file)
        self.n = len(data)
        self.time = n / rate
  	sample = fft(self.data[:bufferSize]
	def e(self, data, mono=False):
		#computes the instantaneous energy of a sample of n frames
		if mono:
			for i in range(len(data)):
				return pow(data[i], 2)
		#assuming stereo input
		else:
			return (pow(data[0], 2 + pow(data[1], 2))
		return y
	def sound_buffer(self, data):
		x = []
		for i in range(len(data)):
			x.append(e(data[i])
		E = numpy.average(x)
		C = (-0.0025714 * numpy.var(x) + 1.5142857)
		return x, E, C 
		#list of instantaneous sound, average sound, variance coefficiant
	
	def subband(self, data, multi=32):
		#divide the data into n different arrays, or subbands
		x = []
		for i in range(int(len(data)+1)): # n+1 as to not truncate values
			x[i] = data[(i*muti):((i+1)*muti)]
		#average the results
		for i in range(len(x)):
			x[i] = numpy.average(x[i])
		return x
		
	def window(self, data, window=256):
		return data[::window]
        
    def D(self, data):
		#create a list of the cosine distances of the vectors
        x = []
        for i in range(len(data)-1):
            y = numpy.dot(data[i], data[i+1]) / (numpy.linalg.norm(data[i]) * numpy.linalg.norm(data[i+1]))
            x.append(y)
        return x
        
    def downsample(self, data, mult):
        #Given 1d array of data, return the binned average
        overhang=len(data)%mult
        if overhang: 
            data=data[:-overhang]
        data=numpy.reshape(data,(len(data)/mult,mult))
        data=numpy.average(data,1)
        return data
        
    def fft(self, data, trimBy=10, logscale=False, divBy=100):
        #take absolute value of fft of data, then split it into two arrays
        left,right = numpy.split(numpy.abs(numpy.fft.fft(data)),2)
        y = numpy.add(left,right[::-1])#y axis is both channels added
        if logscale:
            y = numpy.multiply(20,numpy.log10(y))
        x = numpy.arange(self.buffer/2)#x value is n frames
        if trimBy:
            i = int((self.buffer/2)/trimby)
            #assign new trimmed arrays
            y = y[:i]
            x = x[:i] * self.rate / self.buffer
        if divBy:
            y = y / divBy
        return x, y
    def beatSpectrum(self, data):
        self.beat_s = []
            
