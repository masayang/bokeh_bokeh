from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import column, row, gridplot
import baker


def get_vars():
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [1, 4, 9, 16, 25, 36, 49, 64]
    return x, y


def vbar():
    x, y = get_vars()

    plot = figure()

    plot.vbar(x, top=y, color="blue", width=0.5)

    output_file("bokeh.html")
    return plot


def hbar():
    x, y = get_vars()

    plot = figure()

    plot.hbar(x, right=y, color="blue", height=0.5)

    output_file("bokeh.html")
    return plot


@baker.command
def columns():
    show(column(vbar(), hbar()))


@baker.command
def rows():
    show(row(vbar(), hbar()))


@baker.command
def two_by_two():
    show(column(row(vbar(), hbar()), row(hbar(), vbar())))


baker.run()
