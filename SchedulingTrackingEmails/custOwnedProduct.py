import json

class CustOwnedProduct(object):
    def __init__(self, custId, productName, domain , startDate, duration, **emailDte):
        self.custId = custId
        self.productName = productName
        self.domain = domain
        self.startDate = startDate
        self.duration = duration
        self.emailDte = emailDte

    def prepareDictionary(self):
        custDict = {}
        custDict['custId'] = self.custId
        custDict['productName'] = self.productName
        custDict['domain'] = self.domain
        custDict['emailDate'] = self.emailDte

        return custDict

    """
      Below method is used to serialize the class
    """
    #def toJson(self):
    #     return json.dumps(self, default=lambda o: o.__dict__)
