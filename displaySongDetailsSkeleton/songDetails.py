from flask_restful import Resource, reqparse
import sqlite3

class SongDetailByTitle(Resource):
    TABLE_NAME = "songDetails"

    parser = reqparse.RequestParser()
    parser.add_argument('Rating',
                         type = int,
                         required = True,
                         help = "Rating can't be empty")

    def get(self, title):
        detail = {}
        songDetail = self.find_by_title(title)
        if songDetail:
            return ({'Detail' : self.prepareDict(songDetail)})

        return({'Message': 'The song is not found in database.'}) , 404

    def put(self, title):
        data = self.parser.parse_args()
        song = self.find_by_title(title)
        if song:                       ## inserting new row has not made sense to me, so I have not implemented the logic for insertion.
            connection = sqlite3.connect('./displaySongDetailsSkeleton/data.db')
            cursor = connection.cursor()
            update_sql = "UPDATE {table} SET starRating = ? WHERE title = ?".format(table = self.TABLE_NAME)
            cursor.execute(update_sql, (data['Rating'], title))
            connection.commit()

            if(cursor.rowcount > 0):
                connection.close()
                return({'Message':'The start rating has been updated'})
            else:
                return({'ERROR' : 'The start rating could not been updated as the selected sond does not exists in our system anymores'})


    def find_by_title(self, title):
        connection = sqlite3.connect('./displaySongDetailsSkeleton/data.db')
        cursor = connection.cursor()
        
        fetch_sql = 'SELECT * FROM {table} WHERE title = ?'.format(table=self.TABLE_NAME)
        result = cursor.execute(fetch_sql,(title,))
        songDetail = result.fetchone()
        connection.close()

        return (songDetail if songDetail else None)
    
    @staticmethod
    def prepareDict(songDetail):
        detail = {}
        detail['index'] = songDetail[0]
        detail['id'] = songDetail[1]
        detail['title']  = songDetail[2]
        detail['danceability']  = songDetail[3]
        detail['energy']  = songDetail[4]
        detail['mode']  = songDetail[5]
        detail['acousticness']  = songDetail[6]
        detail['tempo']  = songDetail[7]
        detail['duration_ms']  = songDetail[8]
        detail['num_sections']  = songDetail[9]
        detail['num_segments']  = songDetail[10]
        detail['starRating']  = songDetail[11]
     
        return detail


class SongDetails(Resource):
    TABLE_NAME = "songDetails"
    def get(self):
        resultSet = []
        connection = sqlite3.connect('./displaySongDetailsSkeleton/data.db')
        cursor = connection.cursor()
        
        fetch_sql = 'SELECT * FROM {table}'.format(table=self.TABLE_NAME)
        result = cursor.execute(fetch_sql)
        for row in result.fetchall(): 
            songDetail = SongDetailByTitle.prepareDict(row)
            resultSet.append(songDetail)

        connection.close()

        return ({'Details': resultSet})


