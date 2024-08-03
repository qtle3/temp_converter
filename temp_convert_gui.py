# convert_gui.py
# Program to convert Celsius to Fahrenheit using a simple
#   graphical interface.

from graphics import *


def main():
    # Create a window with the title
    win = GraphWin("Celsius Converter", 300, 200)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw the interface
    Text(Point(1, 3), "   Celsius Temperature:").draw(win)
    Text(Point(1, 1), "Fahrenheit Temperature:").draw(win)

    # input field for celsius
    input = Entry(Point(2.1, 3), 5)
    input.setText("0.0")
    input.draw(win)

    # output field for fahrenheit
    output = Text(Point(2.1, 1), "")
    output.draw(win)

    button_convert = Text(Point(1.5, 2.0), "Convert It")
    button_convert.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    # quit button
    button_quit = Text(Point(2.5, 0.5), "Quit")
    button_quit.draw(win)
    Rectangle(Point(2, 0.25), Point(3, 0.75)).draw(win)

    # wait for a mouse click
    win.getMouse()

    # convert input
    celsius = float(input.getText())
    fahrenheit = 9.0 / 5.0 * celsius + 32

    # display output and change button
    output.setText(str(fahrenheit))
    button.setText("Quit")

    # wait for click and then quit
    win.getMouse()
    win.close()


main()
