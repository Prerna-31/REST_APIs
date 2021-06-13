Assumptions:
==============
1. 'custOwnedProduct' table does not have any primary key which means the table can have duplicate data.
2. Only one product is added or removed at a time.
3. StartDate is considered as an activation date.
4. Based on my understanding, expiration date is determined by adding startDate and duration.
5. The scheduled email date can be of past as per data available/inserted into the table. For ex- activation date for 'hosting' product is 2020-03-15 then email will be scheduled on 2020-03-16 and 2020-06-12. It does not make sense but due to time constraints, this scenario has not been handled in the service.
6. Due to time constraints, no validation has been added to authorize the curstomer before deletion and adding products.

Steps to run application:
===========================================
1. Need to create virtual environment and install following libraries before running application:
    - flask
    - flask-restful
    - dateutil.relativedelta
2. Need to run create_tables.py script first to have database table in place. If Data.db exists, this step might not be required.
3. Run app.py.

End-points for the service:
============================
/POST: To add products --> http://127.0.0.1:5000/product
/DELETE: To delete products  --> http://127.0.0.1:5000/product
/GET: To get list of scheduled emails  --> http://127.0.0.1:5000/email

Data inserted to validate the functionalities:
==============================================
{
    "CustomerId" : "Cust123",
    "ProductName" : "domain",
    "Domain" : "xyzzy.com",
    "StartDate" : "2020-01-01",
    "DurationMonths" : "12"
}
{
    "CustomerId" : "Cust456",
    "ProductName" : "hosting",
    "Domain" : "plugh.com",
    "StartDate" : "2020-03-15",
    "DurationMonths" : "3"
}
{
    "CustomerId" : "Cust789",
    "ProductName" : "pdomain",
    "Domain" : "abcdef.net",
    "StartDate" : "2021-06-13",
    "DurationMonths" : "7"
}

List of scheduled emails for the above inserted data:
=====================================================
{
    "ScheduledEmails": [
        {
            "custId": "Cust123",
            "productName": "domain",
            "domain": "xyzzy.com",
            "emailDate": "2020-12-30"
        },
        {
            "custId": "Cust456",
            "productName": "hosting",
            "domain": "plugh.com",
            "emailDate": "2020-03-16"
        },
        {
            "custId": "Cust456",
            "productName": "hosting",
            "domain": "plugh.com",
            "emailDate": "2020-06-12"
        },
        {
            "custId": "Cust789",
            "productName": "pdomain",
            "domain": "abcdef.net",
            "emailDate": "2022-01-04"
        },
        {
            "custId": "Cust789",
            "productName": "pdomain",
            "domain": "abcdef.net",
            "emailDate": "2022-01-11"
        }
    ]
}
