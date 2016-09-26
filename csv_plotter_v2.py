#Sensity Carrier Pigeon CSV Plotter!
#This program will accept a csv file in the Carrier Pigeon data format and plot the data.
#Written by James Gouveia 9.20.16
import matplotlib.pyplot as plt
import pylab as pl
import csv
import numpy as np
import yaml

def main():
	title = "Pigeon Stats"
	x_label= "Timestamp"
	y_label= "Value"

	file_path = "csv_plotter_config.yml"
	global data
	data = yaml_loader(file_path)

	global h
	if data.get('bar_chart').get('use_this_chart') == 'yes':
		h = len(data.get('bar_chart').get('columns'))
	if data.get('Time_series_plot').get('use_this_chart') == 'yes':
		h = len(data.get('Time_series_plot').get('columns'))

	g = globals()

	for i in range(0, h + 1):
		g['col_{0}'.format(i)] = []

	for t in range(0, h + 1) :
		with open(data.get('Source_file_name'),'r') as csvfile:
			plots = csv.reader(csvfile, delimiter=',')
			for col in plots :
				if t == 0:
					g['col_{0}'.format(t)].append(col[t])
				else:
					try:
						if float(col[t]):	
							g['col_{0}'.format(t)].append(float(col[t]))
					except:
						eof =0
					
	del(col_0[0])

	if data.get('Time_series_plot').get('use_this_chart') == 'yes':
		x_label = data.get('Time_series_plot').get('x')
		y_label = data.get('Time_series_plot').get('y').get('y_access_label')
		line_graph(title, x_label, y_label)
	if data.get('bar_chart').get('use_this_chart') == 'yes':
		title = data.get('bar_chart').get('title')
		x_label = data.get('bar_chart').get('x')
		y_label = data.get('bar_chart').get('y').get('y_access_label')
		graph_time_bar(title, x_label, y_label)

def line_graph(title, x_label, y_label):
	#x axis settings
	xTicks = col_0
	pl.xticks(range(len(col_1)), xTicks, rotation=90) 
	plt.xlabel(x_label)

	y_pos = np.arange(len(col_0))

	#y axis settings
	plt.ylabel(y_label)
	plt.ylim([0,data.get('Time_series_plot').get('y_range')])
	
	plt.title(data.get('Time_series_plot').get('title'))

	for v in range(0,h + 1):
		if data.get('Time_series_plot').get('columns').get('column%d' % v) == 'yes':
			pl.plot(y_pos, eval('col_%d' % v), '-', color=data.get('Time_series_plot').get('color').get('color_column%d' % v), label=data.get('Time_series_plot').get('y').get('label%d' % v))

	pl.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25),
			  fancybox=True, shadow=True, ncol=5)
	plt.subplots_adjust(left=0.1, bottom=.3, right=0.90, top=0.80, wspace=0.2, hspace=0)
	plt.savefig(data.get('Time_series_plot').get('chart_file_name'))
	pl.show()

def graph_time_bar(title, x_label, y_label):
	y_pos = np.arange(len(col_0))
	plt.xlim([0,data.get('bar_chart').get('x_range')])
	error = np.random.rand(len(col_0))

	for v in range(0,h + 1):
		if data.get('bar_chart').get('columns').get('column%d' % v) == 'yes':
			plt.barh(y_pos, eval('col_%d' % v), xerr=error, align='center', alpha=0.4, color=data.get('bar_chart').get('color').get('color_column%d' % v) ,label=data.get('bar_chart').get('y').get('label%d' % v))

	pl.legend(loc='upper center', bbox_to_anchor=(0.5, 1.3),
			  fancybox=True, shadow=True, ncol=5)

	plt.subplots_adjust(bottom=0.1, right=0.9, left=0.3, top=0.75)
	plt.yticks(y_pos, col_0)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.title(title)
	plt.savefig(data.get('bar_chart').get('chart_file_name'))
	plt.show()



def yaml_loader(file_path):
	with open(file_path, 'r') as file_descriptor:
		data = yaml.load(file_descriptor)

	return data

main()
