import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        # TODO: Update with appropriate MongoDB connection information -> DONE
        url = "mongodb://mongodatdd3:enLTR9geXxoRPhnjkuanBPH72dXXCcxptQyInXtuqiPxAwqYdFrSrc7gvZo7LjRTYax3ydJFTDJGn4g5DQ1cPw==@mongodatdd3.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mongodatdd3@"
        client = pymongo.MongoClient(url)
        database = client['project2db']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

