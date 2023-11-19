import numpy as np
from tqdm import tqdm

class LifDelta:
    def __init__(self, array_data):
        self.array_data = np.array(array_data)
        self.rows_len = len(self.array_data[0]['image'])
        self.cols_len = len(self.array_data[0]['image'][0])
        self.time_len = len(self.array_data)

    def get_all_area_avg_of_all_frames (self, width = 1, height = 1, color = 0, min_row = 0, min_col = 0, max_row = 512, max_col = 512):
        area_avg_array = []

        time_len = self.time_len
        all_steps = (max_row - min_row + 1) * (max_col - min_col + 1)
        current_step = 0
        min_step = 65000
        max_step = 65010

#         # Call the function to process the data with a progress bar
#         progress_bar = tqdm(total=all_steps, desc="Processing data")

        with tqdm(total=all_steps, desc="Processing data", leave=True) as progress_bar:
            for row_index in range(self.rows_len):
                if row_index < min_row:
                    continue
                if row_index > max_row:
                    break
                for col_index in range(self.cols_len):
                    if col_index < min_col:
                        continue
                    if col_index > max_col:
                        break

                    current_step = current_step + 1
                    progress_bar.update(1)
    #                 tqdm.write(str(current_step) + " of " + str(all_steps) + " row: " + str(row_index) + " col: " + str(col_index))


                    area_avg_of_all_frames = self.get_area_avg_of_all_frames(row_index, col_index, width, height, color)
                    if len(area_avg_of_all_frames) > 0:
                        area_avg_array.append({
                            "row": row_index,
                            "col": col_index,
                            "area_avg_of_all_frames": area_avg_of_all_frames
                        })

            progress_bar.close()
            return area_avg_array

    def get_area_avg_of_all_frames (self, row = 0, col = 0, width = 1, height = 1, color = 0):
        avg_array = []
        time_len = self.time_len

        point_in_range = self.is_point_in_range(row, col, width, height)
        if not point_in_range:
            return avg_array

        for time in range(time_len):
            area_color_avg = self.get_area_color_avg(row, col, width, height, color, time)
            avg_array.append(area_color_avg)

        return avg_array

    def get_area_color_avg (self, row = 0, col = 0, width = 1, height = 1, color = 0, time = 0):
        width_list_index = self.get_list_index_by_range(col, width)
        height_list_index = self.get_list_index_by_range(row, height)

        sum = 0
        counter = 0
        for row_index in height_list_index:
            for col_index in width_list_index:
                point_color = self.get_point_color(row_index, col_index, color, time)
                sum += point_color
                counter += 1


        return sum / counter

    def is_point_in_range (self, row, col, width, height):
        is_row_in_range = self.is_in_range(row, self.rows_len, height)
        is_col_in_range = self.is_in_range(col, self.cols_len, width)
        return is_row_in_range and is_col_in_range

    def get_list_index_by_range (self, target, range):
        range_margin = self.get_margin(range)
        start_range_range = target - range_margin
        end_range_range = target + range_margin

        return self.get_range_list(int(start_range_range), int(end_range_range))

    def get_point_color (self, row = 0, col = 0, color = 0, time = 0):
        return self.get_frame_image(time)[row][col][color]

    def is_in_range (self, target_index, array_len, range):
        # check margin
        margin = self.get_margin(range)
        if margin is False:
            return False

        # check start of list
        if target_index < margin:
            return False

        # check end of list
        remain_to_end_of_array = array_len - target_index
        if remain_to_end_of_array < margin:
            return False

        return True

    def get_range_list(self, start, end):
        return list(range(start, end))


    def get_frame_image (self, time = 0):
        return self.array_data[time]['image']

    def get_margin (self, range):
        if range < 1:
            return False
        if (range % 2 == 0) and not range == 1:
            return False
        return (range - 1) / 2


    ############################################################################

    def get_normalized_all_area_avg_of_all_frames (self, all_area_avg_of_all_frames, time_range = 1, delta_range = 0.3):
        def filter_function (item):
            return self.is_area_avg_frames_normalized(item["area_avg_of_all_frames"], time_range, delta_range)

        return list(filter(filter_function, all_area_avg_of_all_frames))

    def is_area_avg_frames_normalized (self, area_avg_array, time_range = 3, delta_range = 1.3):
        area_avg_array_len = len(area_avg_array)
        area_avg_array_sum = sum(area_avg_array)
        average_of_area_avg_array = area_avg_array_sum / area_avg_array_len
        is_normalized = False
        for time, avg in enumerate(range(area_avg_array_len)):
            sliced_area_avg_array = area_avg_array[time:(time+time_range)]
            average_of_sliced_array = sum(sliced_area_avg_array) / len(sliced_area_avg_array)

            if average_of_sliced_array > average_of_area_avg_array * delta_range:
                is_normalized = True
                break

        return is_normalized
