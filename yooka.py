import pymysql.cursors
talking = True
prevres = ""
while talking:
    a = input("user:")
    b =a.lower()
# Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='test_python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT answer FROM `test` WHERE `question`like %s"
            cursor.execute(sql, (b,))
            result = cursor.fetchall()
            number_of_rows=cursor.execute(sql, (b,))
            for row in result:

                row["answer"]

                
                
            if(number_of_rows==1):print("Yooka:",row["answer"])
            elif(number_of_rows==0):
                print("Yooka: Wah Yooka belum mengerti pertanyaan kamu. Yooka, masih belajar baca tulis nih, coba tanya lagi dong yang lain..")
                data =(b, '',1)
                sql = "INSERT INTO `test` (`question`, `answer`, `username`) VALUES (%s, %s, %s)"
                cursor.execute(sql, data)
                connection.commit()
    finally:
        connection.close()
