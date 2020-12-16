"""
Author: Alex Alvarado
Date: 12-15-20
Program: Daily_Question_Page.py
Description: Constructs the Daily Question Page
"""

from FinalGUI.Page_Class import Page
import tkinter as tk

class Page3(Page):

#will use the random question function to generate a new question every time someone logs in!!!!


   def __init__(self,*args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #------Creates the label for the page-------#
       self.label = tk.Label(self, text="No trivia for today!\nHow are you though?")
       self.label.pack(side="top", expand=True)

       #-----Creates a frame to hold the buttons-------#
       self.response_frame = tk.Frame(self)
       self.response_frame.pack(side="top")

       #-----Creates a postive and negative response button-------#
       self.answer_button = tk.Button(self.response_frame, text="Good", command =lambda : self.good_button())
       self.answer_button2 = tk.Button(self.response_frame, text="Not so good.", command = lambda : self.bad_button())
       self.answer_button.pack(side="left")
       self.answer_button2.pack(side="right")


   def good_button(self):
       self.answer_button.configure(bg = "#abfffb")
       self.answer_button2.configure(bg="white")
       self.label.configure(text="That is wonderful to hear\nYou can use the create post button on the \n upper left hand corner to tell others \n about your day!")
   def bad_button(self):
       self.answer_button.configure(bg="white")
       self.answer_button2.configure(bg="#abfffb")
       self.label.configure(text="We are sorry to hear that\n Hopefully our community can cheer you up!")



