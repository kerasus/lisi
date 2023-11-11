import numpy as np
import matplotlib.pyplot as plt
from Classes.LifDelta import LifDelta
from Classes.ReadFile import LifFileReader

pile_path = '/home/ali/Downloads/Project001.lif'

lifFileReader = LifFileReader(pile_path)

array_data = lifFileReader.get_array_data()
# print(array_data[0]['image'][0][0][0])

lifDelta = LifDelta(array_data)
area_avg = lifDelta.get_all_area_avg_of_all_frames(50, 50, 10, 10, 0)
normalized_index = lifDelta.get_normalized_delta(area_avg, 2, 0.3)

print(normalized_index)

# plot the data as a line graph
plt.plot(range(len(area_avg)), area_avg)

# show the plot
plt.show()

#
# def map_row(row_np_arr):
#     def map_col(col_np_arr):
#         return col_np_arr[0]
#     return list(map(map_col, row_np_arr))
#
#
# np_arr = np.array(array_data)
# red_mapped_np_arr = list(map(map_row, np_arr))
#
#
# np_red_mapped_arr = np.array(red_mapped_np_arr)
#
# def get_distinct(arr):
#     distinct_arr = []
#     for item in arr:
#         if item not in distinct_arr:
#             distinct_arr.append(item)
#     return distinct_arr
#
# distinct_red_mapped_np_arr = list(map(get_distinct, np_red_mapped_arr))
#
# print(distinct_red_mapped_np_arr)
