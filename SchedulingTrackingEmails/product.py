from flask_restful import Resource , reqparse , request
from datetime import datetime
import sqlite3

class Product(Resource):
    TABLE_NAME = "custOwnedProduct"
    DataInput = []

    parser = reqparse.RequestParser()
    parser.add_argument('CustomerId',
                        type=str,
                        required=True,
                        help='Customer ID can not be empty'
                        )
    parser.add_argument('ProductName',
                        type=str,
                        required=True,
                        help='Product Name can not be empty'
                        )
    parser.add_argument('Domain',
                        type=str,
                        required=True,
                        help='Domain can not be empty'
                        )
    parser.add_argument('StartDate',
                        type=str, 
                        required=False,
                        help="startDate cannnot be empty"
                        )
    parser.add_argument('DurationMonths',
                        type=int,
                        required=False,
                        help='Duration should be in months(numeric)'
                        )

    def post(self):
        data = Product.parser.parse_args()
        
        try:
            startDate = datetime.strptime(data['StartDate'], '%Y-%m-%d').date()
        except ValueError:
            return({'ERROR': 'Incorrecte date format --> The startDate should be in YYYY-MM-DD format.'})

        connection = sqlite3.connect('./SchedulingTrackingEmails/data.db')
        cursor = connection.cursor()
        insert_sql = "INSERT INTO {table} values(?,?,?,?,?)".format(table=self.TABLE_NAME)
        try:
            cursor.execute(insert_sql,(data['CustomerId'], data['ProductName'], data['Domain'], startDate, data['DurationMonths']))
            connection.commit()
        except sqlite3.Error as e:
             print('SQLite error: %s' % (' '.join(e.args)))
             connection.close()
             return({'SQL ERROR': 'An exception has been caught while adding product.'})

        connection.close()
        return ({'Message': 'The product has been inserted successfully'}), 201


    def delete(self):
        data = self.parser.parse_args()
        connection = sqlite3.connect('./SchedulingTrackingEmails/data.db')
        cursor = connection.cursor()
        delete_sql = "DELETE FROM {table} WHERE custId = ? AND productName = ? AND domain = ?".format(table=self.TABLE_NAME)
        
        try:
            cursor.execute(delete_sql,(data['CustomerId'], data['ProductName'], data['Domain']))
            connection.commit()
        except sqlite3.Error as e:
            print('SQLite error: %s' % (' '.join(e.args)))
            connection.close()
            return({'SQL ERROR': 'An exception has been caught while deleting product.'})
        
        if(cursor.rowcount > 0):
            connection.close()
            return({'Message' : 'The product has been successfully deleted'})
        else:
            return({'Message' : 'The product does not exists'}) 

        

        