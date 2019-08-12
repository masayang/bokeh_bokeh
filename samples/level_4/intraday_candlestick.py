import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool
from bokeh.layouts import gridplot
from datetime import date


def read_data():
    return pd.read_csv(
        "intraday.csv",
        names=["Date", "Open", "High", "Low", "Close", "Volume"],
        parse_dates=[0]
    )


def intraday_candlestick(length=100):
    df = read_data().reset_index()
    print(df)
    inc = df.Close >= df.Open
    dec = df.Close < df.Open

    w = 1000/100/2/10

    plot = figure(
        plot_width=1000,
        x_axis_type="linear",
        title="SPY Intraday",
        x_range=(df.iloc[-1*length]['index'], df.iloc[-1]['index']),
        y_range=(df.iloc[-1*length:].Low.min(), df.iloc[-1*length:].High.max())
    )

    plot.segment(df['index'], df['High'], df['index'],
                 df['Low'], color="black")
    plot.vbar(x='index', width=w, bottom='Open', top='Close',
              fill_color="#D5E1DD", line_color="black", source=df[inc])
    plot.vbar(x='index', width=w, top='Open', bottom='Close',
              fill_color="#F2583E", line_color="black", source=df[dec])
    plot.xaxis.visible = False

    plot2 = figure(
        plot_width=1000,
        plot_height=125,
        x_range=plot.x_range,
        y_range=(0, df.iloc[-1*length:].Volume.max()),
        title=None
    )

    major = {}
    tickers = []
    for i in range(1, df.shape[0]):
        if df.iloc[i].Date.date() != df.iloc[i-1].Date.date():
            major[i] = df.iloc[i].Date.date().strftime("%Y-%m-%d")
            tickers.append(i)

            plot2.vbar(x='index', width=w, bottom=0, top='Volume',
                       fill_color="#D5E1DD", line_color="black", source=df[inc])
    plot2.vbar(x='index', width=w, top='Volume', bottom=0,
               fill_color="#F2583E", line_color="black", source=df[dec])
    plot2.xaxis.ticker = tickers
    plot2.xaxis.major_label_overrides = major

    hover_tools = HoverTool(
        tooltips=[
            ("Date", "@Date{%F %H:%M}"),
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
    return gridplot([[plot], [plot2]])


if __name__ == '__main__':
    show(intraday_candlestick())
