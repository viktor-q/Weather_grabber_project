import datetime
import sqlite3


class databaser_cl:
    def __init__(self):
        self.conn = sqlite3.connect("orders.db", check_same_thread=False)
        self.cur = self.conn.cursor()

        # make table
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS table_for_results(
                       date INT PRIMARY KEY,
                       temperature INT,
                       region INT);
                    """
        )
        self.conn.commit()

    def post_to_table(self, temp_parced, region):

        # add data
        pars_data = (datetime.datetime.today().replace(microsecond=0), temp_parced, region)
        self.cur.execute("INSERT INTO table_for_results VALUES(?, ?, ?);", pars_data)
        self.conn.commit()

    def read_from_table(self):

        # read data
        # self.conn = sqlite3.connect('orders.db')
        # self.cur = conn.cursor()

        self.cur.execute("SELECT * FROM table_for_results;")
        one_result = self.cur.fetchall()
        return one_result


# for test
# fiction = databaser_cl()
# fiction.post_to_table(8, 2)
# print(str(fiction.read_from_table()))
#
