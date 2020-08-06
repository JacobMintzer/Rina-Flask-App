import board
import neopixel
class Board():
	def __init__(self, size):
		self.pixels = neopixel.NeoPixel(board.D18, size) #should be 64 atm
	
	def fill(self, color):
		
		if color == 'Red':
			colorTuple = (255, 0, 0)
		elif color == 'Blue':
			colorTuple = (0, 0, 255)
		elif color == 'Green':
			colorTuple = (0, 255, 0)
		elif color == 'Pink':
			colorTuple = (238, 64, 175)
		else:
			colorTuple = (0, 0, 0)
		self.pixels.fill(colorTuple)
