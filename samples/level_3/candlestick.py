import pandas as pd
from bokeh.plotting import figure, show, output_file
from math import pi
from bokeh.models import HoverTool


def read_data():
    return pd.read_csv(
        "SPY.csv",
        names=["Date", "Open", "High", "Low", "Close", "Volume"],
        parse_dates=[0]
    )


def candlestick(range=100):
    df = read_data()

    inc = df.Close >= df.Open
    dec = df.Close < df.Open

    w = 12*60*60*1000 # half day in ms


    plot = figure(
        plot_width=1000,
        x_axis_type="datetime",
        title="SPY Daily",
        x_range=(df.iloc[-1*range].Date, df.iloc[-1].Date),
        y_range=(df.iloc[-1*range:].Low.min(), df.iloc[-1*range:].High.max())
    )
    plot.xaxis.major_label_orientation = pi/4
    plot.grid.grid_line_alpha=0.3
    plot.segment(df.Date, df.High, df.Date, df.Low, color="black")
    plot.vbar(x='Date', width=w, bottom='Open', top='Close', fill_color="#D5E1DD", line_color="black", source=df[inc])
    plot.vbar(x='Date', width=w, top='Open', bottom='Close', fill_color="#F2583E", line_color="black", source=df[dec])
    hover_tools = HoverTool(
        tooltips=[
            ("Date", "@Date{%F}"),
            ("Open", "@Open"),
            ("High", "@High"),
            ("Low", "@Low"),
            ("Close", "@Close"),
            ("Volume", "@Volume")
        ],
        formatters={"Date": "datetime"}
    )
    plot.add_tools(hover_tools)
    output_file("bokeh.html", title="Candle Stick Example")
    return plot
    


if __name__ == '__main__':
    show(candlestick())
