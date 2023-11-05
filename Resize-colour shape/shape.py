import tkinter
import customtkinter
from customtkinter import CTkCanvas
from tkinter.ttk import *
from CTkColorPicker import *


# Shape Class
class clsShapes():
    def __init__(self, root):
        self.root = root
        self.root.title("Shapes")
        # Initialize Variables
        self.x1 = self.y1 = 150
        self.x2 = self.y2 = 350

        # Create Frames        
        self.canvas_frame = customtkinter.CTkFrame(master=self.root)
        self.canvas_frame.grid(row=0,column=0,padx = 10, pady=10)
        self.widget_frame = customtkinter.CTkFrame(master=self.root)
        self.widget_frame.grid(row=1,column=0, pady=10, padx=10)
        # Create canvas
        self.canvas = tkinter.Canvas(self.canvas_frame, height=500, width=500)
        self.canvas.grid(row=0,column=0,padx=10,pady=10)

        # Add Shapes
        self.rect_shape = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                outline = "black", fill ="#0000FF",
                                width = 2)
        
        # Add Widgets
        self.size_label = customtkinter.CTkLabel(self.widget_frame, text=f"Size: {125}", text_color="white", width=190)
        self.size_label.grid(padx=10, pady=10, row=1,column=0, sticky="NW")
        self.colour_label = customtkinter.CTkLabel(self.widget_frame, text=f"Colour: #0000FF", text_color="white",width=190)
        self.colour_label.grid(padx=10, pady=10, row=1,column=3, sticky= "NE")
        self.shape_slider = customtkinter.CTkSlider(self.widget_frame, from_=0, to=250, number_of_steps=250, command=self.slider_update, width=190)
        self.shape_slider.grid(padx = 10, pady = 10, row=2, column=0,sticky="W")
        self.shape_slider.set(125)
        self.colour_button = customtkinter.CTkButton(self.widget_frame,text="Choose Colour", text_color="white", width=190, command=self.chooseColour)
        self.colour_button.grid(padx=10, pady=10, row=2,column=3, sticky= "E")

    # Increases the size of the rectangle based on the size of the slider. Also updates the coords displayed in the label
    def slider_update(self, event):
        self.x1 = self.y1 = 250 - event
        self.x2 = self.y2 = 250 + event

        self.canvas.coords(self.rect_shape, self.x1,self.y1, self.x2,self.y2)
        self.size_label.configure(self.root, text=f"Size: {int(event)}")
        self.size_label.update()

    def chooseColour(self):
        colour = AskColor(title="Please choose a colour")
        chosen_colour = colour.get()
        self.canvas.itemconfigure(self.rect_shape, fill=chosen_colour)
        self.colour_label.configure(text=f"Colour: {chosen_colour}")

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = clsShapes(root)
    customtkinter.set_appearance_mode("Dark")
    root.mainloop()