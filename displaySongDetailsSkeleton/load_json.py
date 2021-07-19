import sqlite3
import json

def create_table():
    connection = sqlite3.connect('./displaySongDetailsSkeleton/data.db')
    cursor = connection.cursor()
    create_sql = "CREATE TABLE IF NOT EXISTS songDetails(_index VARCHAR(3), id VARCHAR2(50), title VARCHAR2(50), danceability REAL, energy REAL, mode NUMBER(10), acousticness REAL, tempo REAL, duration_ms NUMBER(10), num_sections NUMBER(10), num_segments NUMBER(10), starRating NUMBER(1))"
    cursor.execute(create_sql)
    connection.close()

def load_json():
    connection = sqlite3.connect('./displaySongDetailsSkeleton/data.db')
    cursor = connection.cursor()
    insert_sql = "INSERT INTO songDetails(_index, id, title, danceability, energy, mode, acousticness, tempo, duration_ms, num_sections, num_segments) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
    dataList = []

    with open("./displaySongDetailsSkeleton/playlist.json","r") as jsonFile:
        data = json.load(jsonFile)
        
        for i in range(len(data.get('id'))):   ## Assuming all the inner dictionaries are of same length
            myTuple = (
                str(i), 
                data.get('id').get(str(i)), 
                data.get('title').get(str(i)), 
                data.get('danceability').get(str(i)), 
                data.get('energy').get(str(i)), 
                data.get('mode').get(str(i)), 
                data.get('acousticness').get(str(i)), 
                data.get('tempo').get(str(i)),
                data.get('duration_ms').get(str(i)), 
                data.get('num_sections').get(str(i)), 
                data.get('num_segments').get(str(i))
            )   

            dataList.append(myTuple)

            cursor.executemany(insert_sql, dataList)
            connection.commit()

    connection.close()


