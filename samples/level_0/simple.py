from bokeh.plotting import figure, output_file, show


def plot_simple():
    output_file("bokeh.html")

    x = [0, 1, 2, 3, 4, 5, 6]
    y = [4, 5, 6, 7, 8, 9, 10]

    p = figure(
        plot_width=1000,
        plot_height=800,
        tools="pan, hover"
    )
    p.line(x, y)
    show(p)


if __name__ == '__main__':
    plot_simple()

