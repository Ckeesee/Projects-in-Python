import sqlite3

fileList = ('information.dox','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('textFile.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_textFiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        fileName TEXT\
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('textFile.db')
filetype = ".txt"
for x in fileList:
    if ".txt" in x:
        Title = x
        with conn:
            cur= conn.cursor()
            cur.execute("INSERT INTO tbl_textFiles(fileName) VALUES (?)", [x])
            conn.commit()
conn.close()

conn = sqlite3.connect('textFile.db')

with conn:
    cur= conn.cursor()
    cur.execute("SELECT fileName FROM tbl_textFiles")
    varFile = cur.fetchall()
    print(varFile)
