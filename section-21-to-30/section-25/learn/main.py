import os 
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data) 

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
# avg_temp = data["temp"].mean()
# print(round(avg_temp, 3))

# # max_temp = data["temp"].max()
# # print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# print(monday.temp * 9/5 + 32)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
print(data_dict)
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")