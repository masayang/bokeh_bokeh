from bokeh.io import output_file, show
from bokeh.plotting import figure


def line():
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [1, 4, 9, 16, 25, 36, 49, 64]

    plot = figure()

    plot.line(x, y)

    plot.cross(x, y, size=15)

    output_file("bokeh.html")
    show(plot)


if __name__ == '__main__':
    line()
    