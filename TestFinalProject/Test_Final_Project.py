import unittest
from FinalGUI import bloggerdb as dbase
from datetime import datetime
from FinalGUI import Error_Handling as exc

from FinalGUI.Main_page import MainView
import FinalGUI
from FinalGUI import Main_page

from FinalGUI import Create_Blogger as cb

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = dbase.create_connection("bloggerdb.db")
        self.create_tables = dbase.create_tables("bloggerdb.db")
    def tearDown(self):
        del self.conn, self.create_tables


    #I will need to figure out what I want to test: Maybe test to see if the names are inputed correctly!
    def test_add_post(self):

        self.create_post = ("Alexander", "Alvarado", "Who here can help me with raising children?")
        self.post_id = dbase.create_post(self.conn, self.create_post)
        self.rows = dbase.select_all_posts(self.conn)
        self.post = self.rows[self.post_id-1][3]
        assert self.post == "Who here can help me with raising children?"
        assert self.rows[self.post_id-1][2] == "Alvarado"
        assert self.rows[self.post_id-1][1] == "Alexander"



    def test_add_blogger(self):
        self.create_blogger = ("Percy", "Jackson", datetime.today())
        self.blogger_id = dbase.create_blogger(self.conn, self.create_blogger)
        self.rows = dbase.select_all_bloggers(self.conn)
        self.blogger = str(self.rows[self.blogger_id-1][1]) + " " + str(self.rows[self.blogger_id-1][2])
        assert self.blogger == "Percy Jackson"


    def test_add_blogger_InvalidName(self):
        with self.assertRaises(exc.InvalidName):
            create_new_blogger = cb.check_new_blogger("1234", "Alvarado")


    def test_add_blogger_NoName(self):
        with self.assertRaises(exc.NoName):
            create_new_blogger = cb.check_new_blogger("", "")


if __name__ == '__main__':
    unittest.main()


