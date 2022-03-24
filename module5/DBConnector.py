import sqlite3

from module5.Publication import Publication


class DBConnector:

    def __init__(self, table_name):
        self.table = table_name
        self.connection = sqlite3.connect(f"sqlite_bases/newsfeed.db", isolation_level=None)
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} "
                            f"(pub_header text, pub_text text, pub_spec_info text)")
        self.cursor.fetchall()

    def __is_pub_already_exist(self, pub: Publication) -> bool:
        self.cursor.execute(f"SELECT pub_text FROM {self.table}")
        data = self.cursor.fetchall()
        for text in data:
            if text[0] == f"{pub.body()}":
                return True
        return False

    def insert(self, pub: Publication) -> None:
        if not self.__is_pub_already_exist(pub):
            self.cursor.execute(f"INSERT INTO {self.table} VALUES "
                                f"('{pub.header()}','{pub.body()}','{pub.footer()}')")
            self.cursor.fetchall()
        else:
            print(f"Publication with text:\n'{pub.body()}'\nalready exist.\n"
                  f"Table '{self.table}' has not been changed.")
        self.cursor.close()
