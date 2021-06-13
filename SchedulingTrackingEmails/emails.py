from flask import jsonify
from flask_restful import Resource
from datetime import datetime , timedelta
from dateutil.relativedelta import relativedelta
import sqlite3
import json

from custOwnedProduct import CustOwnedProduct

class Emails(Resource):
    TABLE_NAME = "custOwnedProduct"
    scheduledEmailList = []

    def get(self):
        self.scheduledEmailList = []
        connection = sqlite3.connect('./SchedulingTrackingEmails/data.db')
        cursor = connection.cursor()

        fetch_sql = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        try:
            result = cursor.execute(fetch_sql)
        except sqlite3.Error as e:
             print('SQLite error: %s' % (' '.join(e.args)))
             connection.close()
             return({'SQL ERROR': 'An exception has been caught while retrieving list of scehduled emails.'})

        for row in result.fetchall():
            if( row[1].lower() == 'domain' ):
                emailDate = self.getEmailDate(row, 'EXPIRY' , 2)
                currentRow = self.prepareDictionary(row, emailDate)
                self.scheduledEmailList.append(currentRow)
                """
                ==================================================================
                Below logic also can be used to send the list of scheduled emails
                ==================================================================
                custProduct = CustOwnedProduct(*row, emailDte=emailDate) 
                self.scheduledEmailList.append(custProduct.prepareDictionary())
                """
            elif( row[1].lower() == 'hosting' ):
                emailDate = self.getEmailDate(row, 'ACTIVE' , 1)
                currentRow = self.prepareDictionary(row, emailDate)
                self.scheduledEmailList.append(currentRow)

                emailDate = self.getEmailDate(row, 'EXPIRY' , 3)
                currentRow = self.prepareDictionary(row, emailDate)
                self.scheduledEmailList.append(currentRow)

            elif( row[1].lower() == 'pdomain' ):
                emailDate = self.getEmailDate(row, 'EXPIRY' , 9)
                currentRow = self.prepareDictionary(row, emailDate)
                self.scheduledEmailList.append(currentRow)

                emailDate = self.getEmailDate(row, 'EXPIRY' , 2)
                currentRow = self.prepareDictionary(row, emailDate)
                self.scheduledEmailList.append(currentRow)

            # custJSONData = json.dumps(custProduct.toJson(), indent = 4 )  ## It is used to convert object into json format.

        connection.close()
        return({'ScheduledEmails':self.scheduledEmailList})
    
    @classmethod
    def getEmailDate(cls, row, _type , _days):
        startDte = datetime.strptime(row[3],'%Y-%m-%d').date()  ## Have not added try-Except because data is coming from database which has been validated before insertion.
        if(_type == 'EXPIRY'):
            expiryDate = startDte + relativedelta(months=row[4])
            emailDate = expiryDate - timedelta(days=_days)
            emailDate = emailDate.strftime('%Y-%m-%d')
        else:
            emailDate = startDte + timedelta(days=_days)
            emailDate = emailDate.strftime('%Y-%m-%d')
 
        return emailDate

    @classmethod
    def prepareDictionary(cls, row , emaildate):
        custDict = {}
        custDict['custId'] = row[0]
        custDict['productName'] = row[1]
        custDict['domain'] = row[2]
        custDict['emailDate'] = emaildate

        return custDict

    