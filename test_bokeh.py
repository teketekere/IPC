import banpei
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.plotting import figure
from datetime import datetime
from math import radians
from pytz import timezone
import psutil

data = []
results = []


def get_new_data():
    global data
    # ここでデータ取得（例：new_data = psutil.cpu_percent()）
    new_data = psutil.cpu_percent()
    data.append(new_data)


def update_data():
    global results
    get_new_data()
    ret = model.stream_detect(data)
    results.append(ret)
    now = datetime.now(tz=timezone("Asia/Tokyo"))
    new_data = dict(x=[now], y=[data[-1]], ret=[results[-1]])
    source.stream(new_data, rollover=500)


# Create Data Source
source = ColumnDataSource(dict(x=[], y=[], ret=[]))
# Create Banpei instance
model = banpei.SST(w=30)
# Draw a graph
fig = figure(x_axis_type="datetime",
             x_axis_label="Datetime",
             plot_width=950,
             plot_height=650)
fig.title.text = "Realtime monitoring with Banpei"
fig.line(source=source, x='x', y='y', line_width=2, alpha=.85, color='blue', legend='observed data')
fig.line(source=source, x='x', y='ret', line_width=2, alpha=.85, color='red', legend='change-point score')
fig.circle(source=source, x='x', y='y', line_width=2, line_color='blue', color='blue')
fig.legend.location = "top_left"
# Configuration of the axis
'''
format = "%Y-%m-%d-%H-%M-%S"
fig.xaxis.formatter = DatetimeTickFormatter(
    seconds=[format],
    minsec =[format],
    minutes=[format],
    hourmin=[format],
    hours  =[format],
    days   =[format],
    months =[format],
    years  =[format]
)
'''
fig.xaxis.formatter = DatetimeTickFormatter(formats=dict(microseconds=["%f"],
                                                         milliseconds=["%f"],
                                                         seconds=["%F"],
                                                         minsec=["%f"],
                                                         minutes=["%f"],
                                                         hourmin=["%f"],
                                                         hours=["%Y/%m/%d %H"],
                                                         days=["%Y/%m/%d"],
                                                         months=["%Y/%m"],
                                                         years=["%Y"]))
fig.xaxis.major_label_orientation = radians(90)
# Configuration of the callback
curdoc().add_root(fig)
curdoc().add_periodic_callback(update_data, 1000)
