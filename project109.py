import pandas as pd
import statistics
import csv

df = pd.read_csv("data.csv")
data_list = df[""].to_list()

data_mean = statistics.mean(data_list)

data_median = statistics.median(data_list)

data_mode = statistics.mode(data_list)


print("Mean, Median and Mode of height is {}, {} and {} respectively".format(data_mean, data_median, data_mode))

data_std_deviation = statistics.stdev(data_list)

data_first_std_deviation_start, data_first_std_deviation_end = data_mean-data_std_deviation, data_mean+data_std_deviation
data_second_std_deviation_start, data_second_std_deviation_end = data_mean-(2*data_std_deviation), data_mean+(2*data_std_deviation)
data_third_std_deviation_start, data_third_std_deviation_end = data_mean-(3*data_std_deviation), data_mean+(3*data_std_deviation)

data_list_of_data_within_1_std_deviation = [result for result in data_list if result > data_first_std_deviation_start and result < data_first_std_deviation_end]
data_list_of_data_within_2_std_deviation = [result for result in data_list if result > data_second_std_deviation_start and result < data_second_std_deviation_end]
data_list_of_data_within_3_std_deviation = [result for result in data_list if result > data_third_std_deviation_start and result < data_third_std_deviation_end]

print("{}% of data for lies within 1 standard deviation".format(len(data_list_of_data_within_1_std_deviation)*100.0/len(data_list)))
print("{}% of data for  lies within 2 standard deviations".format(len(data_list_of_data_within_2_std_deviation)*100.0/len(data_list)))
print("{}% of data for  lies within 3 standard deviations".format(len(data_list_of_data_within_3_std_deviation)*100.0/len(data_list)))


