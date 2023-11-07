# import cv2
# import numpy as np
# # from PIL import Image, ImageOps
# from readlif.reader import LifFile
#
# new = LifFile('/home/ali/Downloads/Project001.lif')
# # Access a specific image directly
# img_0 = new.get_image(0) # 0 - 1
#
# # # get the height and width of the image
# # height, width = img_0.shape[:2]
# # get the size of the image
# height, width = img_0.get_size()
#
# # reshape the image data to have shape (height, width, 3)
# image_data = image_data.reshape((height, width, 3))
# # print the image data as a numpy array
# print(np.array(image_data))

# # # Create a list of images using a generator
# # img_list = [i for i in new.get_iter_image()]
#
# # Access a specific item
# # z -> 0
# # t -> 0, 171
# # c -> 0, 1, 2
# specificItem = img_0.get_frame(z=0, t=0, c=0)
# # Iterate over different items
# frame_list   = [i for i in img_0.get_iter_t(c=0, z=0)]
# z_list       = [i for i in img_0.get_iter_z(t=0, c=0)]
# channel_list = [i for i in img_0.get_iter_c(t=0, z=0)]
#
# # specificItem.show()
# # frame_list[1].show()
# # print(specificItem)
# # print(frame_list)
# # print(z_list)
# # print(channel_list)
#
# # Remove the alpha channel from the image
# # specificItem = ImageOps.remove_transparency(specificItem)
# # Convert the image to a numpy array
# img_array = np.asarray(specificItem)
#
# # # Convert the image to a numpy array
# # img_array = np.array(specificItem)
# #
# # Reshape the array to have a shape of (height, width, 3)
# img_array = img_array.reshape((img_array.shape[0], img_array.shape[1], 3))
# #
# # Print the array
# print(img_array)

import pylif
import numpy as np

pile_path = '/home/ali/Downloads/Project001.lif'

# Read the LIF file
with pylif.File(pile_path, 'r') as lif:
    image_data = lif.get_image_data()

# Get the shape of the image data
shape = image_data.shape

# Print the shape of the image data
print(shape)
