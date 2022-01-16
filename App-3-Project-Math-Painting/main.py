from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from user
canvas_width = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas height: '))

# Make dictionary of color codes and then prompt for clor
colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

canvas = Canvas(height=canvas_height, width=canvas_width,
                color=colors[canvas_color])

while True:
    shape_type = input("What would you like to draw? Enter quit to quit. ")

    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        r = Rectangle(x=rec_x, y=rec_y, height=rec_height,
                       width=rec_width, color=(red, green, blue))
        r.draw(canvas)

    elif shape_type.lower() == 'square':
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter side of the square: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        s = Square(x=sqr_x, y=sqr_y, side=sqr_side,
                    color=(red, green, blue))
        s.draw(canvas)

    elif shape_type.lower() == 'quit':
        break

canvas.make('canvas.png')


s1 = Square(x=1, y=3, side=3, color=(0, 100, 222))
s1.draw(canvas)
