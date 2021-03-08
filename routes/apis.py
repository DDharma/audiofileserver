from routes import app,request,cross_origin, json,datetime
from modules.connection import sql_connection


@app.route("/")
def hello():
    return "Welcome to the Audio File Server"

@app.route("/upload/<string:audioFileType>/<audioMeta>")
def upload(audioFileType,audioMeta):
    """[uploading audio type into database]

    Args:
        audioFileType ([type]): [string]
        audioMeta ([type]): [string]
    """
    try:
        
        #variable that hold all the data comming from query string    
        """x = {
            "response":"200 Ok",
            "id":id,
            "songName":songName,
            "duration":duration,
            "dateTime":formatted_date
        }"""

        #Calling function to connecting the datbase
        mydb = sql_connection()

        #creating cursor to upload data into the database
        myCursor = mydb.cursor()

        #condition for various type of audio file
        if audioFileType == "songs":
            #converting upcoming string into json(dict)
            audioMeta = json.loads(audioMeta)
            id       = audioMeta["id"]
            songName = audioMeta["songname"]
            duration = audioMeta["duration"]
            dateTime = datetime.datetime.utcnow()
            formatted_date = dateTime.strftime('%Y-%m-%d %H:%M:%S')

            #Query by which data inserted into data base
            query = "INSERT INTO {} (ID, songname, duration, uploadtime) values (%s,%s,%s,%s)".format(audioFileType)

            #variable that holds data, which going to the database table
            data = (id,songName,duration,formatted_date)

        elif audioFileType == "podcast":
            #converting upcoming string into json(dict)
            audioMeta         = json.loads(audioMeta)
            id                = audioMeta["id"]
            podcastName       = audioMeta["podcastname"]
            duration          = audioMeta["duration"]
            hostName          = audioMeta["hostname"]
            participents      = audioMeta["participents"]
            dateTime          = datetime.datetime.utcnow()
            formatted_date    = dateTime.strftime('%Y-%m-%d %H:%M:%S')

            #Query by which data inserted into data base
            query = "INSERT INTO {} (ID, podcastname, duration, uploadtime,hostname,participents) values (%s,%s,%s,%s,%s,%s)".format(audioFileType)

            #variable that holds data, which going to the database table
            data = (id,podcastName,duration,formatted_date,hostName,participents)
            
        elif audioFileType == "audiobook":
            #converting upcoming string into json(dict)
            audioMeta      = json.loads(audioMeta)
            id             = audioMeta["id"]
            title          = audioMeta["title"]
            author         = audioMeta["author"]
            narrator       = audioMeta["narrator"]
            duration       = audioMeta["duration"]
            dateTime       = datetime.datetime.utcnow()
            formatted_date = dateTime.strftime('%Y-%m-%d %H:%M:%S')

            #Query by which data inserted into data base
            query = "INSERT INTO {} (ID,title,author,narrator,duration,uploadtime) values (%s,%s,%s,%s,%s,%s)".format(audioFileType)

            #variable that holds data, which going to the database table
            data = (id,title,author,narrator,duration,formatted_date)

        #executing, commiting and closing all the objects
        myCursor.execute(query,data)
        mydb.commit()
        myCursor.close()
        mydb.close()

        #returning data and 200 Ok after successfully inserted data
        return "200 ok"

    except Exception as e:
        return str(e)

@app.route("/update/<string:audioFileType>/<audioID>/<audioMeta>")
def update(audioFileType,audioID,audioMeta):
    """[summary]

    Returns:
        [type]: [description]
    """
    try:
        #Calling function to connecting the datbase
        mydb = sql_connection()

        #creating cursor to upload data into the database
        myCursor = mydb.cursor()

        #condition for various type of audio file
        if audioFileType == "songs":
            #converting upcoming string into json(dict)
            audioMeta = json.loads(audioMeta)
            id       = audioMeta["id"]
            songName = audioMeta["songname"]
            duration = audioMeta["duration"]
            dateTime = datetime.datetime.utcnow()
            formatted_date = dateTime.strftime('%Y-%m-%d %H:%M:%S')

            #Query by which data inserted into data base
            query = "UPDATE {} SET songname = %s, duration = %s, uploadtime = %s WHERE ID = %s".format(audioFileType)

            #variable that holds data, which going to the database table
            data = (songName,duration,formatted_date,id)

        elif audioFileType == "podcast":
            #converting upcoming string into json(dict)
            audioMeta         = json.loads(audioMeta)
            id                = audioMeta["id"]
            podcastName       = audioMeta["podcastname"]
            duration          = audioMeta["duration"]
            hostName          = audioMeta["hostname"]
            participents      = audioMeta["participents"]
            dateTime          = datetime.datetime.utcnow()
            formatted_date    = dateTime.strftime('%Y-%m-%d %H:%M:%S')

            #Query by which data inserted into data base
            query = "UPDATE {} SET podcastname = %s , duration = %s, uploadtime = %s, hostname = %s, participents = %s WHERE ID = %s".format(audioFileType);

            #variable that holds data, which going to the database table
            data = (podcastName,duration,formatted_date,hostName,participents,id)
            
        elif audioFileType == "audiobook":
            #converting upcoming string into json(dict)
            audioMeta      = json.loads(audioMeta)
            id             = audioMeta["id"]
            title          = audioMeta["title"]
            author         = audioMeta["author"]
            narrator       = audioMeta["narrator"]
            duration       = audioMeta["duration"]
            dateTime       = datetime.datetime.utcnow()
            formatted_date = dateTime.strftime('%Y-%m-%d %H:%M:%S')

            print(audioFileType,audioID)
            #Query by which data inserted into data base
            query = "UPDATE {} SET title = %s, author = %s, narrator = %s, duration = %s, uploadtime = %s WHERE ID = %s".format(audioFileType)

            #variable that holds data, which going to the database table
            data = (title,author,narrator,duration,formatted_date,id)

        #executing, commiting and closing all the objects
        myCursor.execute(query,data)
        mydb.commit()
        myCursor.close()
        mydb.close()

        #returning data and 200 Ok after successfully inserted data
        return "200 ok"

    except Exception as e:
        return str(e)


@app.route("/delete/<string:audioFileType>/<int:id>")
def delete(audioFileType,id):
    """[Function which delete item form the table]

    Returns:
        [Json]: [Item id and type]
    """
    try:
        mydb = sql_connection()
        #Calling function to connecting the datbase
        mydb = sql_connection()

        #creating cursor to upload data into the database
        myCursor = mydb.cursor()

        #executing, commiting and closing all the objects 
        myCursor.execute("DELETE FROM {} where ID = {}".format(audioFileType,id))
        myCursor.close()
        mydb.close()
        
        x = {
            "requestType":"Delete",     
            "response":"200 ok",
            "audioFileType": audioFileType,
            "ID": id
        }
        
        return x

    except Exception as e:
        return str(e)


@app.route("/view/<string:audioFileType>/<int:id>")
def viewOne(audioFileType,id):
    """[Function having ability to show tha data compounding to request]

    Returns:
        [type]: [description]
    """
    try:
        if audioFileType == "songs":
            name = "songname"
        elif audioFileType == "podcastname":
            name = "podcast"
        elif audioFileType == "audiobook":
            name = "title"

        #Calling function to connecting the datbase
        mydb = sql_connection()

        #creating cursor to upload data into the database
        myCursor = mydb.cursor()

        #executing, commiting and closing all the objects 
        myCursor.execute("SELECT {} FROM {} WHERE ID = {}".format(name,audioFileType,id))

        #Storing all the data into list
        names = ""
        for i in myCursor:
            names = i[0]

        myCursor.close()
        mydb.close()
        
        x = {
            "requestType":"View",     
            "response":"200 ok",
            "audioFileType": audioFileType,
            "Audio": names,
            "Audio ID": id
        }
        
        return x

    except Exception as e:
        return str(e)

@app.route("/view/<string:audioFileType>")
def viewAll(audioFileType):
    """[Function having ability to show tha data compounding to request]

    Returns:
        [type]: [description]
    """
    try:
        if audioFileType == "songs":
            name = "songname"
        elif audioFileType == "podcastname":
            name = "podcast"
        elif audioFileType == "audiobook":
            name = "title"

        #Calling function to connecting the datbase
        mydb = sql_connection()

        #creating cursor to upload data into the database
        myCursor = mydb.cursor()

        #executing, commiting and closing all the objects 
        myCursor.execute("SELECT {} FROM {}".format(name,audioFileType))

        #Storing all the data into list
        names = []
        for i in myCursor:
            names.append(i[0])

        myCursor.close()
        mydb.close()
        
        x = {
            "requestType":"View",     
            "response":"200 ok",
            "audioFileType": audioFileType,
            "All the audio": names
        }
        
        return x

    except Exception as e:
        return str(e)

