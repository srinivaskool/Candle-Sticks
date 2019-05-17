from pandas_datareader import data
import datetime
start = datetime.datetime(2018,1,1)
end = datetime.datetime(2019,1,1)
df = data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)

def status_decider(o,c) :
    if c > o:
         value = "Increasing"
    elif o > c:
         value = "Decreasing"
    elif c == o:
        return "Equal"  
    return value
    
df["status"] =  [ status_decider(o,c) for o,c in zip(df.Open,df.Close)]    
df["middle"] = (df.Open + df.Close)/2
df["height"] = abs(df.Open -df.Close)

from bokeh.plotting import show,output_file,figure
f = figure(x_axis_type='datetime',width=1000,height=300,sizing_mode="scale_width")
f.title.text = "Candlestick Chart"

f.grid.grid_line_alpha = 0.3

f.segment(df.index,df.High,df.index,df.Low,color="black")

hours_12 = 12*60*60*1000

f.rect(df.index[df.status == "Increasing"],df.middle[df.status == "Increasing"],hours_12,df.height[df.status == "Increasing"],fill_color="#CCFFFF",line_color="black")

f.rect(df.index[df.status == "Decreasing"],df.middle[df.status == "Decreasing"],hours_12,df.height[df.status == "Decreasing"],fill_color="#FF3333",line_color="black")

output_file("Candle Sticks Chart.html")

show(f)
