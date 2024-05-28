import mysql.connector

def insertData(data):
    rowId = 0

    try:
        with mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="crimedb"
        ) as db:
            print("database connected")
            cursor = db.cursor()

            query = "INSERT INTO criminaldata VALUES(0,'%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
                    (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],
                    data["DOB(yyyy-mm-dd)"],data["Identification Mark"],
                    data["Nationality"], data["Religion"], data["Crimes Done"])

            cursor.execute(query)
            db.commit()
            rowId = cursor.lastrowid
            print("data stored on row %d" % rowId)

    except mysql.connector.Error as error:
        print(f"Error: {error.msg}")

    print("connection closed")
    return rowId

def retrieveData(name):
    id = 0
    crim_data = None

    try:
        with mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="crimedb"
        ) as db:
            print("database connected")
            cursor = db.cursor()

            query = "SELECT * FROM criminaldata WHERE name='%s'"%name

            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                id=result[0]
                crim_data = {
                    "Name" : result[1],
                    "Father's Name" : result[2],
                    "Mother's Name" : result[3],
                    "Gender" : result[4],
                    "DOB(yyyy-mm-dd)" : result[5],
                    "Identification Mark" : result[6],
                    "Nationality" : result[7],
                    "Religion" : result[8],
                    "Crimes Done" : result[9]
                }

                print("data retrieved")
            else:
                print(f"No data found for {name}")

    except mysql.connector.Error as error:
        print(f"Error: {error.msg}")

    print("connection closed")

    return (id, crim_data)
