import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        # TODO: Update with appropriate MongoDB connection information -> DONE
        url = "mongodb://mongodatdd3:enLTR9geXxoRPhnjkuanBPH72dXXCcxptQyInXtuqiPxAwqYdFrSrc7gvZo7LjRTYax3ydJFTDJGn4g5DQ1cPw==@mongodatdd3.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mongodatdd3@"
        client = pymongo.MongoClient(url)
        database = client['project2db']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)