import pygal
import pandas as pd
from pygal.style import Style

table = pd.read_csv('projects.csv')
table = table.sort_values(by=['Number of projects'], ascending=False)


# print(table)
# line_chart = pygal.HorizontalBar()
# line_chart.title = 'Python Frameworks usage in my projects'
# for i in range(len(table['Framework'])):
# 	line_chart.add(table['Framework'][i], table['Number of projects'][i])
# line_chart.render_to_file('my_projects_stats.svg')



custom_style = Style(
  background='black',
  plot_background='#d4d4d4',
  foreground='white',
  foreground_strong='#white',
  foreground_subtle='white',
  opacity='.6',
  opacity_hover='.9',
  transition='400ms ease-in',
  colors=('#b5b359', '#ab547b', '#333170', '#59b565', '#597cb5'))



# pie_chart = pygal.Pie()
# pie_chart.title = "Spheres and tech's used in my projects"

# pie_chart.add('Games', [{'value': 4, 'label': 'PyGame'},
# 					   {'value': 3, 'label': 'PyXel'}])
# pie_chart.add('GUI', [{'value': 3, 'label': 'Tkinter'}])
# pie_chart.add('Web', [{'value': 3, 'label': 'HTML'}, {'value': 3, 'label': 'CSS'},
# 					 {'value': 2, 'label': 'Requests'},
# 					 {'value': 1, 'label': 'Django'},
# 					 {'value': 1, 'label': 'Flask'},
# 					 {'value': 1, 'label': 'JavaScript'}])
# pie_chart.add('Data Visualisation', [{'value': 3, 'label': 'PIL'},
# 					   				{'value': 2, 'label': 'MatPlotLib'},
# 									{'value': 2, 'label': 'PyGal'},
# 					   				{'value': 1, 'label': 'Seaborn'},
# 									{'value': 1, 'label': 'PyWaffle'}])
# pie_chart.add('Telegram Bot', [{'value': 2, 'label': 'Telepot'},
# 					   		  {'value': 1, 'label': 'Python-Telegram-Bot'}])
# pie_chart.add('Data Analytics', [{'value': 2, 'label': 'Pandas'}])
# pie_chart.add('Data Bases', [{'value': 2, 'label': 'SQL'}])
# pie_chart.add('Web Scraping', [{'value': 2, 'label': 'lxml'}])
# pie_chart.add('Math', [{'value': 1, 'label': 'NumPy'}])
# pie_chart.add('Web Scraping', [{'value': 1, 'label': 'Beautiful Soap'}])

# pie_chart.render_to_file('my_projects_stats2.svg')


# treemap = pygal.Treemap(font_size=20, font_family='PT Sans', fill=True, interpolate='cubic', style=custom_style)
# treemap.add('Games', [{'value': 4, 'label': 'PyGame'},
# 					   {'value': 3, 'label': 'PyXel'}])
# treemap.add('GUI', [{'value': 3, 'label': 'Tkinter'}])
# treemap.add('Web', [{'value': 3, 'label': 'HTML'}, {'value': 3, 'label': 'CSS'},
# 					 {'value': 2, 'label': 'Requests'},
# 					 {'value': 1, 'label': 'Django'},
# 					 {'value': 1, 'label': 'Flask'},
# 					 {'value': 1, 'label': 'JavaScript'}])
# treemap.add('Data Visualisation', [{'value': 3, 'label': 'PIL'},
# 					   				{'value': 2, 'label': 'MatPlotLib'},
# 									{'value': 2, 'label': 'PyGal'},
# 					   				{'value': 1, 'label': 'Seaborn'},
# 									{'value': 1, 'label': 'PyWaffle'}])
# treemap.add('Telegram Bot', [{'value': 2, 'label': 'Telepot'},
# 					   		  {'value': 1, 'label': 'Python-Telegram-Bot'}])
# treemap.add('Data Analytics', [{'value': 2, 'label': 'Pandas'}])
# treemap.add('Data Bases', [{'value': 2, 'label': 'SQL'}])
# treemap.add('Web Scraping', [{'value': 2, 'label': 'lxml'}])
# treemap.add('Math', [{'value': 1, 'label': 'NumPy'}])
# treemap.add('Web Scraping', [{'value': 1, 'label': 'Beautiful Soap'}])
# treemap.render_to_file('my_projects_stats3.svg')

line_chart = pygal.HorizontalBar(font_size=50, font_family='PT Sans', fill=True, interpolate='cubic', style=custom_style)
line_chart.add('Adobe Photoshop', 85)
line_chart.add('Python', 75)
line_chart.add('HTML', 70)
line_chart.add('CSS', 70)
line_chart.add('QGIS', 68)
line_chart.add('Adobe Illustrator', 65)
line_chart.add('Flask', 65)
line_chart.add('Django', 55)
line_chart.render_to_file('my_skills.svg')