# property of MeteoSwiss
# written 2016 by Roger Walt (roger.walt@gmail.com)
# supervisor Daniel Leuenberger (daniel.leuenberger@meteoswiss.ch)

from rdp import rdp
import numpy as np
import sys
import glob
import os

class RdpPolygonReducer:
	def __init__(self, fInName, fOutName):
		# open files
		self.fin = open(fInName, 'r')
		self.fout = open(fOutName, 'w')

	def __exit__(self):
		# close files
		fin.close()
		fout.close()

	def readAndReduce(self,epsilon):
		headerline = ''
		first = True
		segments = []
		for line in self.fin:
			arr = line.split()
			if arr[0] == "segment":
				first = True
				self.reduceAndWriteSegments(segments, headerline, epsilon)
				headerline = line
				continue

			x = np.array(arr, dtype=np.float)
			if first:
				segments = np.array([x])
				first = False
			else:
				segments = np.vstack((segments,x))

		self.reduceAndWriteSegments(segments, headerline,epsilon)

	def reduceAndWriteSegments(self, segments, headerline,epsilon):
		if len(segments) == 0:
			return

		if len(segments) == 1:
			arr = headerline.split()
			newpoints = 1
			self.fout.write('segment {}  rank {}  points {}\n'.format(arr[1], arr[3], newpoints))
			v = segments[0]
			self.fout.write('\t{:9.6f} {:9.6f}\n'.format(v[0],v[1]))
			return

		# reduce
		# if too large, use segments[0:5000,:] etc
		reduced = rdp(segments, epsilon=epsilon)

		# write headerline
		arr = headerline.split()
		newpoints = len(reduced)
		self.fout.write('segment {}  rank {}  points {}\n'.format(arr[1], arr[3], newpoints))

		# write segments
		for v in reduced:
			self.fout.write('\t{:9.6f} {:9.6f}\n'.format(v[0],v[1]))

		# report
		print("segment {:3d} completed. reduced polygon from {:4d} points to {:4d} points".format(int(arr[1]), int(arr[5]), int(newpoints)))

