from flask import Flask, render_template , jsonify , request

stores=[
    { 'name'  : 'My Wonderful store',
      'items' : [
         {
         'name' : 'chocolate',
         'price': 120
         },
      ]
    }
] ##list of stores/dictionaries.. even items is also list of dictionaries


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

"""
We have following APIs for online store:
1. POST - Used to get data from user.
2. GET - Used to send data bask to user
"""
## POST /store{name:}
@app.route('/store', methods=['POST'])  ## we can pass multiple methods also--separated by comma
def create_store():
    get_parm = request.get_json()   ## Collecting/Accepting json object(body) requested/sent by user. Here get_parm will be having dictionary format.
    new_store = {
        'name'  : get_parm['name'],
        'items' : [] 
    }
    stores.append(new_store) 
    return jsonify(new_store)  

## GET /store<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if(name == store['name']):
            return jsonify(store)
        return jsonify({'message' : 'The store is not found'})

## GET /store
@app.route('/store')
def get_all_stores():
    ##return jsonify(stores)     ## store is a list of dictionary and jsonify converts dictionary into json object(long string).
    return jsonify({'stores' : stores}) ## The above return statement also works but the best way is to pass dictionary not list of dictionaries

## POST /store/<string:name>/item{name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    get_parm = request.get_json()   
    for store in stores:
        if(name == store['name']):
            new_item = {
                'name'  : get_parm['name'],
                'price' : get_parm['price']
            }

            store['items'].append(new_item)
            return jsonify({'new item':new_item})
        return jsonify({'message' : 'The store cannot be found.'})
   

## GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if (name == store['name']):
            return(jsonify({'items':store['items']}))  ## here store['items'] is a list so we need to convert it into dictionary.
    return jsonify({'message' : 'The store is not found'})

app.run(port = 5002)