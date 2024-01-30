#____________Libraries______________________

import tkinter as tk
import cv2
from PIL import Image, ImageTk
from tkinter import PhotoImage
from tkinter import ttk
import os

#----- joystick function____-----------
def move_circle(event):
    if joystick_enabled.get() == 1:  # Check if the joystick is enabled
        key = event.keysym
        x1, y1, x2, y2 = canvas.coords(circle)

        if key == "w" and y1 > 60:
            canvas.move(circle, 0, -10)
        elif key == "s" and y2 < 240:
            canvas.move(circle, 0, 10)
        elif key == "a" and x1 > 60:
            canvas.move(circle, -10, 0)
        elif key == "d" and x2 < 240:
            canvas.move(circle, 10, 0)

def center_circle(event):
    if joystick_enabled.get() == 1:  # Check if the joystick is enabled
        x1, y1, x2, y2 = canvas.coords(circle)
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        canvas.move(circle, 150 - center_x, 150 - center_y)

def toggle_frame_state():
    if canvas.winfo_ismapped():  # Check if canvas is currently visible
        canvas.pack_forget()  # Hide canvas
    else:
        canvas.pack()  # Show canvas

def toggle_joystick_state():
    if joystick_enabled.get() == 1:  # If the joystick is enabled
        joystick_enabled.set(0)  # Disable the joystick
    else:
        joystick_enabled.set(1)  # Enable the joystick



#____________ main page__________________



root = tk.Tk()
root.title("Background Image")
root.configure(bg="black")

#--------main code---------------

# -------------------------------------WEBCAM--------------------------
# Create a label to display the webcam feed
webcam = tk.Label(root, bg="black")
webcam.place(x=20, y=10) 

# Initialize the webcam using OpenCV
cap = cv2.VideoCapture(0)

def update_webcam():
    ret, frame = cap.read()
    if ret:
        # Resize the frame to 861x564
        frame = cv2.resize(frame, (900, 500))
        
        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Convert the frame to a tkinter-compatible format
        img = Image.fromarray(frame_rgb)
        img_tk = ImageTk.PhotoImage(image=img)
        
        # Update the label with the new frame
        webcam.img = img_tk
        webcam.config(image=img_tk)
        
        # Repeat the update every 10 milliseconds 
        webcam.after(10, update_webcam)
    else:
        cap.release()

# Start updating the webcam feed
update_webcam()


                                # -------------main camera label ---------------------------------
main_cam = tk.Label(root, text="Main Cam", fg="white", bg="red", font=("Arial", 12, "bold"))
main_cam.place(x=30, y=20)

#-----------data panel----------------------------------
                                                            # Create the "weapon view" frame
weapon = tk.Frame(root, width=190, height=150, bg="#16191c")
weapon.place(x=20, y=530)
weapon.pack_propagate(0)

# Load the icon image and resize
icon_path = r"C:\Users\boyre\Desktop\miet_defece\weapon.png"
icon_image = Image.open(icon_path)
icon_image = icon_image.resize((32, 32))  # Resize the image using the resize method
icon_photo = ImageTk.PhotoImage(icon_image)

# Create the icon label within the "weapon view" frame
icon_label = tk.Label(weapon, image=icon_photo, bg="#16191c")
icon_label.image = icon_photo  # Keep a reference to prevent it from being garbage collected
icon_label.pack(padx=0, pady=10)

# Create and place the text label within the "weapon view" frame
text_label = tk.Label(weapon, text="Weapons", font=("Helvetica", 12), fg="#837C91", bg="#16191c")
text_label.pack(padx=0, pady=0)

 #Create and place the additional label "2" within the "weapon view" frame @arjun_charak
additional_label = tk.Label(weapon, text="2", font=("Helvetica", 24), fg="#FFFFFF", bg="#16191c")
additional_label.pack(padx=0, pady=10)

                                                # Create the "human view" frame
human = tk.Frame(root, width=190, height=150, bg="#16191c")
human.place(x=220, y=530)
human.pack_propagate(0)

# Load the icon image and resize
icon_path = r"C:\Users\boyre\Desktop\miet_defece\human.png"
icon_image = Image.open(icon_path)
icon_image = icon_image.resize((32, 32))  # Resize the image using the resize method
icon_photo = ImageTk.PhotoImage(icon_image)

# Create the icon label within the "human view" frame
icon_label = tk.Label(human, image=icon_photo, bg="#16191c")
icon_label.image = icon_photo  # Keep a reference to prevent it from being garbage collected
icon_label.pack(padx=0, pady=10)

# Create and place the text label within the "human view" frame
text_label = tk.Label(human, text="Human", font=("Helvetica", 12), fg="#837C91", bg="#16191c")
text_label.pack(padx=0, pady=0)

 #Create and place the additional label "2" within the "human view" frame @arjun_charak
additional_label = tk.Label(human, text="6", font=("Helvetica", 24), fg="#FFFFFF", bg="#16191c")
additional_label.pack(padx=0, pady=10)

                                                    #-----------distance-------

# Create the "distance view" frame
distance = tk.Frame(root, width=190, height=150, bg="#16191c")
distance.place(x=420, y=530)
distance.pack_propagate(0)

# Load the icon image and resize
icon_path = r"C:\Users\boyre\Desktop\miet_defece\distance.png"
icon_image = Image.open(icon_path)
icon_image = icon_image.resize((32, 32))  # Resize the image using the resize method
icon_photo = ImageTk.PhotoImage(icon_image)

# Create the icon label within the "distance view" frame
icon_label = tk.Label(distance, image=icon_photo, bg="#16191c")
icon_label.image = icon_photo  # Keep a reference to prevent it from being garbage collected
icon_label.pack(padx=0, pady=10)

# Create and place the text label within the "distance view" frame
text_label = tk.Label(distance, text="distance", font=("Helvetica", 12), fg="#837C91", bg="#16191c")
text_label.pack(padx=0, pady=0)

 #Create and place the additional label "2" within the "distance view" frame @arjun_charak
additional_label = tk.Label(distance, text="900m", font=("Helvetica", 24), fg="#FFFFFF", bg="#16191c")
additional_label.pack(padx=0, pady=10)


#------------------semi-auto-manual code------------------------------

# Variable to store joystick state (0 for disabled, 1 for enabled)
joystick_enabled = tk.IntVar(value=1)  # Set default value to 1 for enabled state

# Button to toggle showing/hiding the canvas
toggle_button = tk.Button(root, text="Toggle Mode", command=toggle_frame_state, bg="#7835e5", fg="white")
toggle_button.place(x=950, y=20)


# Create a controller frame
controller_frame = tk.Frame(root, width=305, height=340, bg="#16191c")
controller_frame.place(x=950, y=60)

# Create a canvas inside the controller frame
canvas = tk.Canvas(controller_frame, width=300, height=300, bg="#16191c")

# Initially hide the canvas
canvas.pack_forget()

# Create a rectangle as the background on the canvas
canvas.create_oval(50, 50, 250, 250, outline="#ffffff", fill="#16191c")

# Create a circle on the canvas
circle = canvas.create_oval(120, 120, 180, 180, fill="#7835e5")

# Bind keys to move the circle on canvas
root.bind("<KeyPress>", move_circle)
root.bind("<KeyRelease>", center_circle)  # Return to center when key is released

#----------------"Fire" button ------------------------------
custom_font = ("Helvetica", 14)
fire_button = tk.Button(root, text="FIRE", bg="#7835e5", foreground="white",height=1, width=27, font= custom_font)
fire_button.place(x=950, y=430)



#----------------tool box-------------------

toolbox_frame = tk.Frame(root, width=230, height=460, bg="#16191c")
toolbox_frame.place(x=1280, y=20)

 # Create a text label inside the blue widget
text_label = tk.Label(toolbox_frame, text="Tools", font=("Helvetica", 18), fg="#7835e5", background="#16191c")
text_label.place(x=20, y = 10) 


                #-----------------------------intruder checkbox----------------------------------
    # Create an IntVar to control the state of the checkbox (0 for unchecked, 1 for checked)
checkbox_var = tk.IntVar()

    # Create a modern ttk Style
style = ttk.Style()

    # Configure the style for the modern checkbox
style.configure("TCheckbutton", background="#16191c", foreground="white")

    # Create a modern ttk Checkbutton with a default value of 0 (unchecked)
modern_checkbox = ttk.Checkbutton(
        toolbox_frame,
        text="Intruder Box",
        style="TCheckbutton",  # Apply the configured style
        variable=checkbox_var  # Use the IntVar to control the state
    )
modern_checkbox.place(x=20, y=60)

    # Set the initial state of the checkbox to 0 (unchecked)
checkbox_var.set(0)

                            #------------------------weapon checkbox-----------------------

        # Create an IntVar for the second checkbox (Weapon Box)
weapon_checkbox_var = tk.IntVar()

    # Create the second modern ttk Checkbutton (Weapon Box)
weapon_checkbox = ttk.Checkbutton(
        toolbox_frame,
        text="Weapon Box",
        style="TCheckbutton",       # Apply the configured style
        variable=weapon_checkbox_var  # Use the IntVar to control the state
    )
weapon_checkbox.place(x=20, y=90)

    # Set the initial state of the second checkbox to 0 (unchecked)
weapon_checkbox_var.set(0)

                           #-----------------------------auto capture image----------------------------
        # Create a function to capture an image when Auto Capture Image is checked
auto_capture_var = tk.IntVar()

def capture_image_auto():
        if auto_capture_var.get() == 1:  # Check if Auto Capture Image is checked (1)
            print("Auto capturing image...")

    # Create the third modern ttk Checkbutton (Auto Capture Image)
auto_capture_checkbox = ttk.Checkbutton(
        toolbox_frame,
        text="Auto Capture Images",
        style="TCheckbutton",          # Apply the configured style
        variable=auto_capture_var,     # Use the IntVar to control the state
        command=capture_image_auto    # Call the capture_image_auto function when checked
    )
auto_capture_checkbox.place(x=20, y=120)

                #-------------------alarm------------------------
def trigger_alarm():
        print("Alarm triggered!")

        # Create a function to trigger an alarm when Alarm is checked
alarm_var = tk.IntVar()

def trigger_alarm_auto():
        if alarm_var.get() == 1:  # Check if Alarm is checked (1)
            print("Alarm triggered!")

    # Create the fourth modern ttk Checkbutton (Alarm)
alarm_checkbox = ttk.Checkbutton(
        toolbox_frame,
        text="Auto Alarm",
        style="TCheckbutton",       # Apply the configured style
        variable=alarm_var,         # Use the IntVar to control the state
        command=trigger_alarm_auto  # Call the trigger_alarm_auto function when checked
    )
alarm_checkbox.place(x=20, y=150)

    # Set the initial state of Alarm checkbox to unchecked (0)
alarm_var.set(0)

#---------------------nightvision checkbox---------------------------
    # Create an IntVar for the fifth checkbox (Night Vision)
night_vision_var = tk.IntVar()

    # Create the fifth modern ttk Checkbutton (Night Vision)
night_vision_checkbox = ttk.Checkbutton(
        toolbox_frame,
        text="Night Vision",
        style="TCheckbutton",         # Apply the configured style
        variable=night_vision_var,    # Use the IntVar to control the state
        command=None  # Call the activate_night_vision function when checked
    )
night_vision_checkbox.place(x=20, y=180)

    # Set the initial state of Night Vision checkbox to unchecked (0)
night_vision_var.set(0)

    #----------------grey vision---------------------------------------

        # Create an IntVar for the sixth checkbox (Gray Vision)
gray_vision_var = tk.IntVar()

    # Create the sixth modern ttk Checkbutton (Gray Vision)
gray_vision_checkbox = ttk.Checkbutton(
        toolbox_frame,
        text="Gray Vision",
        style="TCheckbutton",         # Apply the configured style
        variable=gray_vision_var,    # Use the IntVar to control the state
        command=None  # Call the activate_gray_vision function when checked
    )
gray_vision_checkbox.place(x=20, y=210)

    # Set the initial state of Gray Vision checkbox to unchecked (0)
gray_vision_var.set(0)

    #-------distance box-----------------
        # Create an IntVar for the seventh checkbox (Distance)
distance_var = tk.IntVar()

    # Create the seventh modern ttk Checkbutton (Distance)
distance_checkbox = ttk.Checkbutton(
        toolbox_frame,
        text="Distance",
        style="TCheckbutton",        # Apply the configured style
        variable=distance_var,      # Use the IntVar to control the state
        command=None     # Call the check_distance function when checked
    )
distance_checkbox.place(x=350, y=150)

    # Set the initial state of Distance checkbox to unchecked (0)
distance_var.set(0)




                #----------------"gallery" button ------------------------------
custom_font = ("Helvetica", 10)
gallery_button = tk.Button(toolbox_frame, text="Gallery", bg="#7835e5", foreground="white",height=1, width=20, font= custom_font)
gallery_button.place(x=20, y=280)

               #----------------"logs" button ------------------------------
custom_font = ("Helvetica", 10)
logs_button = tk.Button(toolbox_frame, text="Logs data", bg="#7835e5", foreground="white",height=1, width=20, font= custom_font)
logs_button.place(x=20, y=320)






#-------------map view-----------------

# Load the image
image_path = "C:/Users/boyre/Desktop/miet_defece/map.png"
img = Image.open(image_path)

# Resize the image
new_width = 400  # Replace with your desired width
new_height = 250  # Replace with your desired height
resized_img = img.resize((new_width, new_height))

# Convert the resized image for Tkinter
tk_img = ImageTk.PhotoImage(resized_img)

# Create a label and display the resized image
label = tk.Label(root, image=tk_img)
label.place(x= 1098, y = 530 )



#----cam2-----------



webcam2 = tk.Label(root, bg="black")
webcam2.place(x=650, y=530)


cap = cv2.VideoCapture(0)

def update_webcam2():
    ret, frame = cap.read()
    if ret:
        # Resize the frame to match label dimensions
        frame = cv2.resize(frame, (400, 250))
        
        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Convert the frame to a tkinter-compatible format
        img = Image.fromarray(frame_rgb)
        img_tk = ImageTk.PhotoImage(image=img)
        
        # Update the label with the new frame
        webcam2.img = img_tk
        webcam2.config(image=img_tk)
        
        # Repeat the update every 10 milliseconds 
        webcam2.after(10, update_webcam2)
    else:
        cap.release()

# Start updating the webcam feed
update_webcam2()

                                # -------------camera 2 label ---------------------------------
label_cam = tk.Label(root, text="Cam 2", fg="white", bg="red", font=("Arial", 12, "bold"))
label_cam.place(x=660, y=540)



 







root.mainloop()
