import re
import mysql.connector

#去除字母数字表情和其它字符
def clear_character(sentence):
    pattern1='[a-zA-Z0-9]'
    pattern2 = '\[.*?\]'
    pattern3 = re.compile(u'[^\s1234567890:：' + '\u4e00-\u9fa5]+')
    pattern4='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
    line1=re.sub(pattern1,'',sentence)   #去除英文字母和数字
    line2=re.sub(pattern2,'',line1)   #去除表情
    line3=re.sub(pattern3,'',line2)   #去除其它字符
    line4=re.sub(pattern4, '', line3) #去掉残留的冒号及其它符号
    new_sentence=''.join(line4.split()) #去除空白
    return new_sentence

def get_db_conn():
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "password",
        "database": "momo_research_db"
    }

    # try:
    #     # Establishing a connection to the database
    conn = mysql.connector.connect(**db_config)
    #     print("Successfully connected to the database")
    # except mysql.connector.Error as e:
    #     print(f"Error connecting to MySQL: {e}")

    return conn

def get_text(tables, col, condition):
    conn = get_db_conn()
    cursor = conn.cursor()
    res = ""

    for table in tables:
        cursor.execute(f"""
                        SELECT {col}
                        FROM {table}
                        {condition};
                        """)
        rows = cursor.fetchall()           
        for row in rows:
            res += row[0]
        
    cursor.close()
    conn.close()

    return clear_character(res)


def get_momo_note_text():
    condition = "WHERE nickname='momo'"
    tables = ["xhs_note", "xhs_note_main", "xhs_note_legacy"]
    col = "CONCAT(title, `desc`)"
    return get_text(tables, col, condition)

def get_all_note_text():
    condition = ""
    tables = ["xhs_note", "xhs_note_main", "xhs_note_legacy"]
    col = "CONCAT(title, `desc`)"
    return get_text(tables, col, condition)

def get_momo_comment_text():
    condition = "WHERE nickname='momo'"
    tables = ["xhs_note_comment", "xhs_note_comment_main", "xhs_note_comment_legacy"]
    col = "content"
    return get_text(tables, col, condition)

def get_all_comment_text():
    condition = ""
    tables = ["xhs_note_comment", "xhs_note_comment_main", "xhs_note_comment_legacy"]
    col = "content"
    return get_text(tables, col, condition)

# print(get_momo_note_text())
# print(get_all_note_text())
# print(get_momo_comment_text())
# print(get_all_comment_text())


