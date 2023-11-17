import cv2
import json
import numpy as np
from PIL import Image, ImageOps, ImageChops
from readlif.reader import LifFile

class LifFileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cached_directory = './cached_data/'

    def get_array_data (self):
        new = LifFile(self.file_path)
        # Access a specific image directly
        img_0 = new.get_image(0) # 0 - 1

        # # Create a list of images using a generator
        # img_list = [i for i in new.get_iter_image()]
        #
        # # Access a specific item
        # # z -> 0
        # # t -> 0, 171
        # # c -> 0, 1, 2
#         specificItem = img_0.get_frame(z=0, t=0, c=0)
#         specificItem.show()
        # # Iterate over different items
#         frame_list   = [i for i in img_0.get_iter_t(c=0, z=0)]
        frame_list   = [{'image':self.get_rgb_array(x), 'frame':i} for i,x in enumerate(img_0.get_iter_t(c=0, z=0))]
#         frame_list_len = len(frame_list)
#         images_array = []

        # z_list       = [i for i in img_0.get_iter_z(t=0, c=0)]
        # channel_list = [i for i in img_0.get_iter_c(t=0, z=0)]

        # # specificItem.show()
        # # frame_list[1].show()
        # print(specificItem)
        # # print(frame_list)
        # # print(z_list)
        # # print(channel_list)

        return frame_list

    def get_specific_item_image (self, z=0, t=0, c=0):
        new = LifFile(self.file_path)
        # Access a specific image directly
        img_0 = new.get_image(0) # 0 - 1
        # # Access a specific item
        # # z -> 0
        # # t -> 0, 171
        # # c -> 0, 1, 2
        specificItem = img_0.get_frame(z, t, c)
        return specificItem

    def get_rgb_array (self, image):
        # Convert the image to RGB format
        rgb_image = image.convert('RGB')

        # Convert the image to a NumPy array
        array = np.array(rgb_image)

        # Get the shape of the array
        height, width, channels = array.shape

        # Convert the array to RGB data
        rgb_array = array.reshape((height, width, 3))

        return rgb_array

    def write_to_file (self, data, file_name):
        # Convert the data to JSON
        json_data = json.dumps(data)

        # Write the JSON data to a file
        with open(self.cached_directory + file_name + ".json", "w") as f:
            f.write(json_data)

    def read_from_file (self, data, file_name):
        # Read JSON data from a file
        with open(self.cached_directory + file_name + ".json", "r") as f:
            json_data = f.read()

        # Convert the JSON data to a Python dictionary
        data = json.loads(json_data)
        return data

