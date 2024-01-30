import tkinter as tk

# Function to move the circle
def move_circle(event):
    key = event.keysym
    x1, y1, x2, y2 = canvas.coords(circle)

    if key == "w":
        if y1 > 60:
            canvas.move(circle, 0, -10)
    elif key == "s":
        if y2 < 240:
            canvas.move(circle, 0, 10)
    elif key == "a":
        if x1 > 60:
            canvas.move(circle, -10, 0)
    elif key == "d":
        if x2 < 240:
            canvas.move(circle, 10, 0)

# Function to move the circle to the center when no keys are pressed
def center_circle(event):
    x1, y1, x2, y2 = canvas.coords(circle)
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    canvas.move(circle, 150 - center_x, 150 - center_y)

# Create the main window
root = tk.Tk()
root.title("Joystick")

# Create a canvas
canvas = tk.Canvas(root, width=300, height=300, bg= "#16191c")
canvas.pack()

# Create a rectangle as the background
canvas.create_oval(50, 50, 250, 250, outline="#ffffff", fill="#16191c")


# Create a circle
circle = canvas.create_oval(120, 120, 180, 180, fill="#7835e5")

# Bind keys to move the circle
root.bind("<KeyPress>", move_circle)
root.bind("<KeyRelease>", center_circle)  # Return to center when key is released

root.mainloop()
