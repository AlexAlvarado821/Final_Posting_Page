"""
Author: Alex Alvarado
Date: 12-14-20
Program: Main_Page.py
Description: This page creates the login page and imports and creates the other two pages so they can be accessed after a user is created
"""
import tkinter as tk
from FinalGUI import bloggerdb as db
from datetime import datetime

from FinalGUI.Posting_Page import Page2
from FinalGUI.Daily_Question_Page import Page3



class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.conn = db.create_connection("bloggerdb.db")
        self.create_tables = db.create_tables("bloggerdb.db")


        #self.p1 = Page1(self)
        self.p2 = Page2(self)
        self.p3 = Page3(self)

        #----Creating the two buttons on the top




        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)

        container.pack(side="top", fill="both", expand=True)

        #self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


        #self.b1 = tk.Button(buttonframe, text="Create a Blogger Account", command=lambda:[self.p1.lift, self.create_session()])

        #assuming the blogger is created, the id can be accessed by the other pages in the main frame

        self.b2 = tk.Button(buttonframe, text="Create a Post", command=self.p2.lift)
        self.b3 = tk.Button(buttonframe, text="Question of the Day", command=self.p3.lift)


        #Add additional buttons to the program

        #self.b1.pack(side="left")
        self.b2.pack(side="left")
        self.b3.pack(side="right")

        #-------Quit application button----------#
        #All the tables are destroyed in order for there to be a new session next time the application is run
        self.b_quit_application = tk.Button(self, text="Quit/Close", command = lambda:[self.destroy_tables()])
        self.b_quit_application.pack(side = "bottom")


        #-------Log out button so a new user can be created----------#
        self.b_logout = tk.Button(self, text="Logout", command = lambda : self.logout())
        self.b_logout.configure(state=tk.DISABLED)
        self.b_logout.pack(side="bottom")



        self.start_session()

        #--------Colors for the pages

        #p1.configure(bg='#abfffb')


    def destroy_tables(self):
        #deletes the contents of the tables below:
        db.delete_post_table(self.conn)
        db.delete_blogger_table(self.conn)
        root.destroy()

    def add_blogger(self):
        """
        This adds a new blogger if it passed the three tests below
        :return: None
        """
        try:
            if self.has_Numbers(self.f_name.get().replace(" ", "")) or self.has_Numbers(self.l_name.get().replace(" ", "")):
                self.l_table_date.configure(text="Please enter a valid first or last name")
                raise ValueError
            elif self.has_spaces(self.f_name.get().replace(" ","")) or self.has_spaces(self.l_name.get().replace(" ","")):
                self.l_table_date.configure(text="Please enter a name rather than spaces")
                raise ValueError
            elif self.f_name.get() == "" or self.l_name.get() == "":
                self.l_table_date.configure(text="Error! No name or last name entered")
                raise ValueError
            else:
                blogger = (self.f_name.get().replace(" ", ""), self.l_name.get().replace(" ",""), str(datetime.today()))
                self.blogger_id = db.create_blogger(self.conn, blogger)
                # register the addition
                self.conn.commit()
                self.b_add_blogger.configure(state=tk.DISABLED)
                self.l_name.delete(0, tk.END)
                self.f_name.delete(0, tk.END)
                # This is where the blogger will be hidden and the session will be started
                self.l_table_date.configure(text="")
                self.b_logout.configure(state=tk.NORMAL)
                self.hide_create_blogger()
                self.create_session()

        except ValueError as err:
            #change the test of the label to say the error so the user knows what to change
            print(err)

               #finish adding error handling in the code. I wanted to check if the input was a string and not a number

    def has_Numbers(self, input_string):
        return any(char.isdigit() for char in input_string)

    def has_spaces(self, input_string):
        return any(char.isspace() for char in input_string)


    def logout(self):
        #the logout button will lead to page2 moving on to a new user instead of the current user
        #This should allow the current blogger to post multiple posts without issue.
        self.start_session()
        self.p2.blogger_id = self.p2.blogger_id + 1
        self.b_logout.configure(state=tk.DISABLED)


    def view_bloggers(self):
        rows = db.select_all_bloggers(self.conn)
        text = ""
        for row in rows:
           for col in row:
             text += "{}     ".format(col)
           text += "\n"
        self.l_table_date.configure(text=text)

    def hide_create_blogger(self):
        #hides all the elements on the original page
        self.f_name_label.pack_forget()
        self.l_name_label.pack_forget()
        self.f_name.pack_forget()
        self.l_name.pack_forget()
        self.label.pack_forget()
        self.b_add_blogger.pack_forget()
        self.b_view_bloggers.pack_forget()
        self.p2.show()
        #self.p2.label.configure(text="something to prove")


    def start_session(self):
        self.label = tk.Label(self, text="Create a New Blogger")
        self.label.pack(side ="top")
        # side="top"

        #--------Adds a label which will be used to display error messages------
        self.l_table_date = tk.Label(self, text="")
        self.l_table_date.pack(side = "top")
        #  , fill="both", expand=True
        #--------Adds the entry for the first name--------
        self.f_name_label = tk.Label(self, text="First Name:")
        self.f_name_label.pack()
        self.f_name = tk.Entry(self)
        self.f_name.pack()
        #--------Adds the entry for the last name-------
        self.l_name_label = tk.Label(self, text="Last Name:")
        self.l_name_label.pack()
        self.l_name = tk.Entry(self)
        self.l_name.pack()

        # add a command to fetch the date from the entries for storage
        self.b_add_blogger = tk.Button(self, text="Create Blogger", command=lambda: [self.add_blogger()],
                                       bg='#abfffb')
        self.b_add_blogger.pack()
        # -------------
        self.b_view_bloggers = tk.Button(self, text="View Bloggers", command=lambda: self.view_bloggers())
        self.b_view_bloggers.pack()
        #-------------Log out button---------



        self.p2.lower()

        self.p3.lower()


        self.b2.configure(state=tk.DISABLED)
        self.b3.configure(state=tk.DISABLED)

    def create_session(self):
        rows = db.select_all_bloggers(self.conn)

        l_name = rows[self.blogger_id-1][1]
        f_name = rows[self.blogger_id-1][2]
        date = rows[self.blogger_id-1][3]

        self.p2.label.configure(text="Welcome: " + l_name + ", " + f_name + "." + " \nToday is: "+ date)

        self.b2.configure(state=tk.NORMAL)
        self.b3.configure(state=tk.NORMAL)

        #yet to be used













if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("700x700")
    root.mainloop()


#figure out how to configure create bloggers to enable the all the buttons on the top of the page on the mainframe
#create a function which returns the name in page1 which gives access to the name and number

# try and create the best application on the planet for the sake of being the best in the owlrd at what I do for the love of god how can you work on things without the help of others.......





