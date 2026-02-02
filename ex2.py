import cv2
img = cv2.imread("image.jpg")
height, width, channels = img.shape
size = img.size
datatype = img.dtype
print("width:",width )
print("height:",height )
print("channels",channels )
print("image size",size )
print("data type:",datatype )
