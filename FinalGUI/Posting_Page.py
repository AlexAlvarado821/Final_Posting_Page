"""
Author: Alex Alvarado
Date: 12-13-20
Program: Posting_Page.py
Description: This is where the user can make posts and they will appear on the screen
"""

from FinalGUI import bloggerdb as db
from FinalGUI.Page_Class import Page
from FinalGUI import Error_Handling as er
from FinalGUI import Create_Blogger as cb

import tkinter as tk




class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        #----Label/header for the page which is changed in the main page----#
        self.label = tk.Label(self, text="")
        self.label.pack(side="top")

        self.error_label = tk.Label(self, text="")
        self.error_label.pack(side="top")

        #---Connection to the database
        self.conn = db.create_connection("bloggerdb.db")
        self.create_tables = db.create_tables("bloggerdb.db")

        #----Entry and button for creating posts----#
        self.post = tk.Entry(self)
        self.post.pack(ipady=40, ipadx=80)
        self.b_create_post = tk.Button(self, text="POST", command = lambda : self.create_post(self.post.get()))
        self.b_create_post.pack()
        #----Shows the current users posts----#
        self.b_user_posts = tk.Button(self, text="My Posts", command = lambda :self.show_users_posts())
        self.b_user_posts.pack()

        #----Creates an outer and inner frame for the posts to be held in and manipulated-----#

        self.main_post_block = tk.Frame(self)
        self.main_post_block.pack()

        self.buffer_block = tk.Frame(self.main_post_block)
        self.buffer_block.pack()




        #creates the blogger id which will be raised by the main page whenever a new user logs in to ensure they can create multiple posts
        self.blogger_id = 1


    def show_users_posts(self):
        #forgets the current posts shown
        self.buffer_block.pack_forget()
        #then creates the frame for the posts!
        self.buffer_block = tk.Frame(self.main_post_block)
        self.buffer_block.pack()

        #retrieve the first name of the current user

        rows2 = db.select_all_bloggers(self.conn)


        f_name = rows2[self.blogger_id-1][1]

        l_name = rows2[self.blogger_id -1][2]

        #retrieve all the posts made!
        rows = db.users_posts(self.conn, f_name)

        for row in rows:
            text = ""
            text += "[Post by: {}, {}]\n".format(f_name, l_name)
            for col in row:

                if isinstance(col, int):
                    pass
                elif col == f_name or col == l_name:
                    pass
                else:
                    text += col + "\n"

            self.create_reactions(text)







    def view_posts(self):

       #erase everything before it and start over!!!

        self.buffer_block.pack_forget()

        self.buffer_block = tk.Frame(self.main_post_block)
        self.buffer_block.pack()


        #----shows all the posts created and the corresponding names---#


        rows = db.select_all_posts(self.conn)

        self.range = 1

        for row in rows:
            text = ""
            for col in row:


                if isinstance(col, int):
                    pass
                elif col == rows[self.range-1][1]:
                    text += "[Post by {},".format(col)
                elif col == rows[self.range-1][2]:
                    text += "{}]\n".format(col)
                elif col == rows[self.range-1][3]:
                    text +="\n{}\n".format(col)


            #creates dislike and like buttons which will apprear with everypost!
            self.range +=1
            self.create_reactions(text)




    def create_post(self, post):
        #attempts to create post
        try:
            cb.check_new_post(post)

        except er.InvalidPost as err:
            self.error_label.configure(text="You must enter something to post!")
            print(err)
        else:

            rows2 = db.select_all_bloggers(self.conn)

            l_name = rows2[self.blogger_id - 1][1]

            f_name = rows2[self.blogger_id - 1][2]

            post = (l_name, f_name, self.post.get())

            self.post_id = db.create_post(self.conn, post)

            self.conn.commit()

            self.post.delete(0, tk.END)

            self.num = 0

            self.error_label.configure(text="")

            self.view_posts()

    def create_reactions(self, text):





        self.top = tk.Frame(self.buffer_block)
        self.top.pack(side="top")


       #this will be specfic to the user
        self.display_posts = tk.Label(self.top, text='')
        self.display_posts.pack()
        self.num_like = 0
        self.num_dislike= 0
        self.display_posts.configure(text=text)


        self.button_l_name = tk.Button(self.top, text="Like", bg='white', command = lambda:likes_color(self))
        self.button_d_name = tk.Button(self.top, text="Dislike", bg="white", command = lambda:dislikes_color(self))




        self.button_d_name.pack(side="left")
        self.button_l_name.pack(side="right")

        #implements inner functions which change the color of the dislike and like buttons
        def likes_color(self):
            self.button_l_name.configure(bg="#abfffb")
            self.button_d_name.configure(bg="white")

        def dislikes_color(self):
            self.button_d_name.configure(bg="#abfffb")
            self.button_l_name.configure(bg="white")








