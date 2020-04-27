import mysql.connector
mydb = mysql.connector.connect(
  host="docsimplr.cy5jsfrhhzez.us-east-1.rds.amazonaws.com",
  user="admin",
  passwd="mohit10696",
  database="docsimplr"
)

def init(email,password):
    email2 = "temp"
    key2 = "temp"
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM login where email = '"+email+"'and password = '"+password+"'")
    myresult = mycursor.fetchall()
    print(myresult)
    for x in myresult:
        email2 = x[1]
        key2 = x[3]
    if email2!="temp":
        print("Successfully login")
        return 1
    else:
        print("Successfully not login")   
        return 0
