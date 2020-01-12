import socketio as socket
import eventlet
import cv2
import numpy as np
import time
import asyncio
from PIL import Image 

print("client")
client = socket.Client()

client.connect('http://ip_addr:port')


def arr_to_buffer_str(image):               #İstemci için 
		reshape_img = image.reshape((230400))
		return reshape_img.tostring()

def buffer_str_to_arr(string_image):       #sunucu için
		img_array = np.frombuffer(string_image,count=230400,dtype=np.uint8)
		return img_array.reshape((360,640))


dim_count = 0
start_count = 0
image = np.zeros((360,640,3),"uint8")

def listen():
	@client.on('ProcessReturn')
	def Set(data):
		global image,dim_count
		print("came data")
		image[:,:,dim_count] = buffer_str_to_arr(data["img"])
		dim_count += 1
		if dim_count == 3:	# array dimension
			img = Image.fromarray(image, 'RGB')
			img.save("img.jpg")
			Image.open("img.jpg")
			dim_count = 0
			send_data()

	@client.on('StartControlReturn')
	def Set(data):
		global image,dim_count,start_count
		print("came data")
		
		if data["start"] and start_count<=3:
			start_count += 1
			print("++parked++")
		elif not data["start"] and start_count>0:
			start_count -= 1
			print("--parked--")
		if start_count == 3:   # array dimension
			print("\n\nStartControl Passed\n\n")
			send_data()
		else:
			start_control()

def send_data():
	print("sending_data")
	global image
	image = cv2.imread("img.jpg")
	img_r = arr_to_buffer_str(image[:,:,0])
	img_g = arr_to_buffer_str(image[:,:,1])
	img_b = arr_to_buffer_str(image[:,:,2])
	client.emit("Process",{'img':img_r})
	time.sleep(0.02)
	client.emit("Process",{'img':img_g})
	time.sleep(0.02)
	client.emit("Process",{'img':img_b})
	print("sended")



def start_control():
	print("start_control")
	image = cv2.imread("img.jpg")
	img_r = arr_to_buffer_str(image[:,:,0])
	img_g = arr_to_buffer_str(image[:,:,1])
	img_b = arr_to_buffer_str(image[:,:,2])
	client.emit("StartControl",{'img':img_r})
	time.sleep(0.01)
	client.emit("StartControl",{'img':img_g})
	time.sleep(0.01)
	client.emit("StartControl",{'img':img_b})

listen()


send_data()
	

#client.disconnect()