from FinalGUI.Page_Class import Page
import tkinter as tk

class Page3(Page):

#will use the random question function to generate a new question every time someone logs in!!!!


   def __init__(self,*args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.label = tk.Label(self, text="Question of the Day!")
       self.label.pack(side="top", expand=True)

   def set_random_question(self):
       pass


