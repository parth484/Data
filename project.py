import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff

#student performance
df = pd.read_csv("StudentsPerformance.csv") 

reading_list = df["reading score"].to_list()

mean = statistics.mean(reading_list)
median = statistics.median(reading_list)
mode = statistics.mode(reading_list)
std_deviation = statistics.stdev(reading_list)

print("Mean = ", mean)
print("Median = " , median)
print("Mode = ", mode)
print("Standard Deviation = ", std_deviation)

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)
list_of_data_1 = [result for result in reading_list if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_2 = [result for result in reading_list if result > second_std_deviation_start and result < second_std_deviation_end]

print("{}% of data lies between one standard deviation".format(len(list_of_data_1)*100.0/len(reading_list)))
print("{}% of data lies between two standard deviation".format(len(list_of_data_2)*100.0/len(reading_list)))

fig = ff.create_distplot([reading_list],["Result"],show_hist=False)
fig.show()
