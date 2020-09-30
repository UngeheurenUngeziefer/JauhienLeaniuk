import pandas as pd
import glob
import os
import pygal
from pygal.style import Style
from datetime import datetime, timedelta

# Открываем все json файлы и делаем из них один
# path = 'C:/Users/sewer/OneDrive/Рабочий стол/export-20200911-000/Sport-sessions'
# for filename in glob.glob(os.path.join(path, '*.json')):
# 	with open(os.path.join(os.getcwd(), filename), 'r') as f:
# 		print(f.read())


# экспортируем всё как эксель таблицу
# with open('json_info.json', 'r', encoding='utf-8') as json:
# 	table = pd.read_json('C:/Users/sewer/MyPython/JauhienLeaniuk/resourses/json_info.json', lines=True)
# table.to_excel('table.xlsx')

# таблица эксель
table = pd.read_excel('table.xlsx', index_col=0)
# print(list(table.columns.values))
# ['start_time', 'end_time', 'distance', 'duration', 'average_speed', 
# 'calories', 'pause_duration', 'duration_per_km', 'elevation_gain', 
# 'elevation_loss', 'longitude', 'latitude', 'max_speed', 'temperature', 
# 'max_step_frequency', 'avg_step_frequency', 'total_steps', 'weather_condition_id',
# 'surface_id', 'subjective_feeling_id']

################################## START TIME ############################################
# time_list = []
# ymd_list = []
# end_time_list = []

# for i in table['start_time']:
#  	str_i = str(i)
#  	year = str_i[0:4]
#  	month = str_i[5:7]
#  	day = str_i[8:10]
#  	hour = str_i[11:13]
#  	minute = str_i[14:16]
#  	sec = str_i[17:19]
#  	time = int(hour + minute + sec)
#  	ymd = str(year + '-' + month + '-' + day)
#  	time_list.append(time)
#  	ymd_list.append(ymd)

# date_chart = pygal.Line(x_label_rotation=90)
# date_chart.title = 'Start Time of trainings'
# date_chart.x_labels = ymd_list
# date_chart.y_labels = [{'label': '6:00:00', 'value': 60000},
#   {'label': '8:00:00', 'value': 80000},
#   {'label': '10:00:00', 'value': 100000},
#   {'label': '12:00:00', 'value': 120000},
#   {'label': '14:00:00', 'value': 140000},
#   {'label': '16:00:00', 'value': 160000},
#   {'label': '18:00:00', 'value': 180000},
#   {'label': '20:00:00', 'value': 200000},
#   {'label': '22:00:00', 'value': 220000}]
# date_chart.add("Start Time", time_list)
# date_chart.render_to_file('start_time_running.svg', width=1200, height=400, explicit_size=True)
# 2019-09-25 12:03:53


# CustomStyle = Style(colors=['green'])
# line_chart = pygal.StackedLine(fill=True, style=CustomStyle)
# line_chart.title = 'Distance of my Runnings (km)'
# line_chart.y_labels = [{'label': '2', 'value': 2000},
#   {'label': '4', 'value': 4000},
#   {'label': '6', 'value': 6000},
#   {'label': '8', 'value': 8000},
#   {'label': '10', 'value': 10000},
#   {'label': '12', 'value': 12000},
#   {'label': '14', 'value': 14000},
#   {'label': '16', 'value': 16000},
#   {'label': '18', 'value': 18000},
#   {'label': '20', 'value': 20000}]


# CustomStyle = Style(colors=['blue'])
# line_chart = pygal.Bar(fill=True, style=CustomStyle)
# line_chart.title = 'Duration time of my runnings'
# line_chart.y_labels = [{'label': '01:45:00', 'value': 7000000},
#   {'label': '01:30:00', 'value': 6000000},
#   {'label': '01:15:00', 'value': 5000000},
#   {'label': '01:00:00', 'value': 4000000},
#   {'label': '00:45:00', 'value': 3000000},
#   {'label': '00:30:00', 'value': 2000000},
#   {'label': '00:15:00', 'value': 1000000}]
# line_chart.add('Duration', table['duration'])
# line_chart.render_to_file('duration_running.svg', width=1000, height=400, explicit_size=True)



# CustomStyle = Style(colors=['#b39239'])
# line_chart = pygal.Bar(stroke=False, style=CustomStyle)
# line_chart.title = 'Average speed (km/h)'
# line_chart.add('Average Speed', table['average_speed'])

# line_chart.render_to_file('average_speed.svg', width=1000, height=400, explicit_size=True)

# CustomStyle = Style(colors=['#673b8f', '#478f3b', '#8f8f3b', '#8f433b', '#3b458f', '#8f3b85'])
# gauge = pygal.SolidGauge(inner_radius=0.70, style=CustomStyle)
# calorie_formatter = lambda x: '{:10,g} cal'.format(x)
# steps_formatter = lambda x: '{:10,g} steps'.format(x)
# distance_formatter = lambda x: '{:10,g} m'.format(x)
# duration_formatter = lambda x: '{:10,g} days'.format(x)
# gauge.value_formatter = calorie_formatter

# gauge.add('Calories burned', [{'value': sum(table['calories']), 'max_value': 100000}])
# gauge.add('Total Steps', [{'value': sum(table['total_steps']), 'max_value': 1000000}], formatter=steps_formatter)
# gauge.add('Total Distance', [{'value': sum(table['distance']), 'max_value': 1000000}], formatter=distance_formatter)
# gauge.add('Total Duration', [{'value': sum(table['duration']), 'max_value': 3}], formatter=duration_formatter)
# gauge.add('Elevation Gained', [{'value': sum(table['elevation_gain']), 'max_value': 2000}], formatter=distance_formatter)
# gauge.add('Elevation Loss', [{'value': sum(table['elevation_loss']), 'max_value': 2000}], formatter=distance_formatter)

# gauge.render_to_file('calories_steps.svg')


# table = table.drop_duplicates(['elevation_loss', 'elevation_gain'])
# CustomStyle = Style(colors=['#913c65', '#3c914e'])
# line_chart = pygal.StackedBar(fill=True, style=CustomStyle)
# line_chart.title = 'Elevation gained/lost'
# line_chart.x_labels = table['start_time']
# line_chart.add('Loss', -table['elevation_loss'])
# line_chart.add('Gained', table['elevation_gain'])
# line_chart.render_to_file('gain_loss.svg', width=1000, height=400, explicit_size=True)


# CustomStyle = Style(colors=['#32a89d'])
# line_chart = pygal.StackedBar(fill=True, style=CustomStyle)
# line_chart.title = 'Maximum speed (km/h)'
# line_chart.x_labels = table['max_speed']
# line_chart.add('Speed', table['max_speed'])
# line_chart.render_to_file('max_speed.svg', width=1000, height=400, explicit_size=True)


CustomStyle = Style(colors=['#8779e0'])
line_chart = pygal.StackedBar(fill=True, style=CustomStyle)
line_chart.title = 'Average Step Frequency'
line_chart.x_labels = table['avg_step_frequency']
line_chart.add('Step Frequency', table['avg_step_frequency'])
line_chart.render_to_file('avg_step_frequency.svg', width=1000, height=400, explicit_size=True)