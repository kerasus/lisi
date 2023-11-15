import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from Classes.LifDelta import LifDelta
from Classes.ReadFile import LifFileReader

pile_path = '/home/ali/Downloads/Project001.lif'

lifFileReader = LifFileReader(pile_path)

array_data = lifFileReader.get_array_data()
specific_item_image = lifFileReader.get_specific_item_image(0, 0, 0)

lifDelta = LifDelta(array_data)

width = 21
height = 21
color = 0
# min_row = 120
# max_row = 130
# min_col = 290
# max_col = 300

min_row = 100
max_row = 150
min_col = 220
max_col = 320

all_area_avg_of_all_frames = lifDelta.get_all_area_avg_of_all_frames(width, height, color, min_row, min_col, max_row, max_col)
print('all_area_len', len(all_area_avg_of_all_frames))
normalized_all_area_avg_of_all_frames = lifDelta.get_normalized_all_area_avg_of_all_frames(all_area_avg_of_all_frames, 3, 1.360)
print('normalized_area_len', len(normalized_all_area_avg_of_all_frames))


# Create a drawing object
draw = ImageDraw.Draw(specific_item_image)
for i, item in enumerate(normalized_all_area_avg_of_all_frames):
    x_margin = ( width - 1 ) / 2
    y_margin = ( height - 1 ) / 2

    left = (item['col'] - x_margin)
    right = (item['col'] + x_margin)
    top = (item['row'] - y_margin)
    bottom = (item['row'] + y_margin)

    # Draw a rectangle with a red border
    draw.rectangle((left, top, right, bottom), outline='red', width=1)
#     print("Index:", i, "item->row:", item['row'], "item->col:", item['col'])

# Show the image
specific_item_image.show()



# is_area_avg_frames_normalized = lifDelta.is_area_avg_frames_normalized(area_avg_of_all_frames, 3, 1.1)
# print(is_area_avg_frames_normalized)


# area_avg_of_all_frames = lifDelta.get_area_avg_of_all_frames(40, 40, 40, 40, 0)
# area_avg_of_all_frames = lifDelta.get_area_avg_of_all_frames(135, 300, 40, 40, 0)
# print(area_avg_of_all_frames)

# area_color_avg = lifDelta.get_area_color_avg(40, 40, 40, 40, 0, 0)
# area_color_avg = lifDelta.get_area_color_avg(135, 300, 40, 40, 0, 0)
# print(area_color_avg)

# point_color = lifDelta.get_point_color(40, 40, 0, 0)
# point_color = lifDelta.get_point_color(135, 300, 0, 0)
# print(point_color)
