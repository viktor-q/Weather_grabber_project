import sqlite3
#import maker
import datetime

class Databaser_cl:
    def __init__(self):
        self.conn = sqlite3.connect('orders.db', check_same_thread=False)
        self.cur = self.conn.cursor()

        # make table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS table_for_results(
                       date INT PRIMARY KEY,
                       temperature INT);
                    """)
        self.conn.commit()




    def post_to_table(self, firstnum, secondnum):

        # add data
        pars_data = (datetime.datetime.today().replace(microsecond=0), maker.maker_foo(firstnum, secondnum))
        self.cur.execute("INSERT INTO table_for_results VALUES(?, ?);", pars_data)
        self.conn.commit()


    def read_from_table(self):

        # read data
        #self.conn = sqlite3.connect('orders.db')
        #self.cur = conn.cursor()

        self.cur.execute("SELECT * FROM table_for_results;")
        one_result = self.cur.fetchall()
        return one_result


#for test
#fiction = Databaser_cl()
#fiction.post_to_table(4, 2)
#print(str(fiction.read_from_table()))
#