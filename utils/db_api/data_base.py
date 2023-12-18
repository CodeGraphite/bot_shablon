import sqlite3

class DataBase:

    def __init__(self) -> None:
        self.conn = sqlite3.connect("data/data_base.db")
        self.cur = self.conn.cursor()

    def create_users_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id int,
            username text
        )""")
    def add_user(self,msg):
        id__ = msg.chat.id
        if str(id__)[0]!='-' :
            self.cur.execute("SELECT * FROM users WHERE id='{}' ".format(msg.chat.id))
            user = self.cur.fetchone()
            if user is None:
                self.cur.execute("INSERT INTO users VALUES ('{}','{}')".format(msg.chat.id, msg.chat.username))
                self.conn.commit()
                text = f"""User bazaga qo'shildi✅
==========================
🆔 ID: <code>{msg.from_user.id}</code>
👤 Username: @{msg.from_user.username}
👤 First Name : {msg.from_user.first_name}
👤 Last Name : {msg.from_user.last_name}
==========================="""
                return text
        else:
            self.cur.execute("SELECT * FROM groups WHERE id='{}' ".format(msg.chat.id))
            user = self.cur.fetchone()
            if user is None:
                self.cur.execute("INSERT INTO groups VALUES ('{}','{}')".format(msg.chat.id, msg.chat.username))
                self.conn.commit()
                text = f"""Guruh bazaga qo'shildi✅
==========================
🆔 ID: <code>{msg.chat.id}</code>
👤 Username: @{msg.chat.username}
==========================="""
                return text
    def give_all_groups(self):
        self.cur.execute("SELECT id FROM groups")
        groups = self.cur.fetchall()
        return groups
    def give_all_users(self):
        self.cur.execute("SELECT id FROM users")
        users = self.cur.fetchall()
        return users
    

















