import azure.functions as func
import pymongo
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            # TODO: Update with appropriate MongoDB connection information -> DONE
            url = "mongodb://mongodatdd3:enLTR9geXxoRPhnjkuanBPH72dXXCcxptQyInXtuqiPxAwqYdFrSrc7gvZo7LjRTYax3ydJFTDJGn4g5DQ1cPw==@mongodatdd3.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mongodatdd3@"
            client = pymongo.MongoClient(url)
            database = client['project2db']
            collection = database['advertisements']
            
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

