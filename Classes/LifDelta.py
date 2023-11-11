import numpy as np

class LifDelta:
    def __init__(self, array_data):
        self.array_data = np.array(array_data)
        self.time_len = len(self.array_data)


    def get_normalized_delta (self, all_area_avg, time_range = 1, delta_range = 0.3):
        normalized_array = []
        all_area_avg_len = len(all_area_avg)
        for index, avg in enumerate(range(all_area_avg_len)):
            if self.is_normalized_avg_for_delta(all_area_avg, index, time_range, delta_range):
                normalized_array.append(index)

        return normalized_array

    def is_normalized_avg_for_delta (self, all_area_avg, target_index, time_range = 3, delta_range = 0.3):
        time_range_list_index = self.get_list_index_by_range(time_range)
        sliced_array = all_area_avg[time_range_list_index[0]:(time_range_list_index[1]+1)]
        # find the maximum value in the array
        max_value = max(sliced_array)
        # find the minimum value in the array
        min_value = min(sliced_array)
        return ((max_value - min_value)< delta_range)

    def get_all_area_avg_of_all_frames (self, row = 0, col = 0, width = 1, height = 1, color = 0):
        avg_array = []
        time_len = self.time_len

        for time in range(time_len):
            avg_array.append(self.get_area_color_avg(row, col, width, height, color, time))

        return avg_array

    def get_all_area_delta_of_all_frames (self, row = 0, col = 0, width = 1, height = 1, color = 0):
        delta_array = []
        old_area_color_avg = 0
        time_len = self.time_len

        for time in range(time_len):
            new_area_color_avg = self.get_area_color_avg(row, col, width, height, color, time)
            calc_area_color_avg = new_area_color_avg - old_area_color_avg
            old_area_color_avg = new_area_color_avg
            delta_array.append(calc_area_color_avg)

        return delta_array

    def get_area_color_avg (self, row = 0, col = 0, width = 1, height = 1, color = 0, time = 0):
        point_in_range = self.is_point_in_range(row, col, width, height, time)
        if not point_in_range:
            return None

        width_list_index = self.get_list_index_by_range(width)
        height_list_index = self.get_list_index_by_range(height)

        sum = 0
        counter = 0
        for row_index in height_list_index:
            for col_index in width_list_index:
                sum += self.get_point_color(row_index, col_index, color, time)
                counter += 1


        return sum / counter

    def get_list_index_by_range (self, range):
        range_margin = self.get_margin(range)
        start_range_range = range - range_margin
        end_range_range = range + range_margin + 1

        return self.get_range_list(int(start_range_range), int(end_range_range))

    def get_range_list(self, start, end):
        return list(range(start, end))


    def get_frame_image (self, time = 0):
        return self.array_data[time]['image']

    def get_point_color (self, row = 0, col = 0, color = 0, time = 0):
        return self.get_frame_image(time)[row][col][color]


    def is_point_in_range (self, row, col, width, height, time):
        is_row_in_range = self.is_in_range(row, len(self.get_frame_image(time)), height)
        is_col_in_range = self.is_in_range(col, len(self.get_frame_image(time)[row]), width)
        return is_row_in_range and is_col_in_range

    def is_in_range (self, target_index, array_len, range):
        # check margin
        margin = self.get_margin(range)
        if margin is False:
            print('margin == False')
            return False

        # check start of list
        if target_index < margin:
            return False

        # check end of list
        remain_to_end_of_array = (target_index + 1) - array_len
        if remain_to_end_of_array > margin:
            return False

        return True

    def get_margin (self, range):
        if range < 1:
            return False
        if (range % 2 == 1) and not range == 1:
            return False
        return (range - 1) / 2


