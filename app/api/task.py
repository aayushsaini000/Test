from app import mongo
from app.util import serialize_doc
from flask import (
    Blueprint, flash, jsonify, abort, request
)
import requests
import json

bp = Blueprint('task', __name__, url_prefix='/')


# Api route for insert user location data

#Endpoint =  /user_location
# payload = {
#             "userid":"1",
#             "name":"Aayush",
#             "latitude":21312.13212,
#             "longitude":21312321.1232131
#             }

@bp.route('/user_location', methods=["POST"])
def create_location():
    userid = request.json.get('userid',None)
    name = request.json.get('name',None)
    latitude = request.json.get('latitude',None)
    longitude = request.json.get('longitude',None)
    if userid is None:
        return jsonify({"message" : "User Id not should be none","err":True}), 400
    
    mongo.db.users_location.update({"userid": userid},
                                        {"$set":{
                                            "userid":userid,
                                            "name":name,
                                            "location":[latitude,longitude]
                                        }
                                    },upsert=True)
    return jsonify({"message" : "User location inserted","err":False}), 200



# Api route for get users need to send data in query parameters
#Endpoint = /get_location?radius=in km&latitude=2324.3242&longitude=23423.3242

@bp.route('/get_location', methods=["GET"])
def get_location():
    #send these parameters in api
    radius = request.args.get("radius")
    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")
    
    # raising error is any parameters is missing
    if radius is None:
         return jsonify({"message" : "Radius in km is required","err":True}), 400
    if latitude is None:
         return jsonify({"message" : "latitude is required","err":True}), 400
    if longitude is None:
         return jsonify({"message" : "longitude is required","err":True}), 400
    
    #create index query used only one time 
    mongo.db.users_location.ensureIndex({"location":"2d"})
    
    # query for find the users from database collection
    ret = mongo.db.users_location.find({'location': {"$near": [ float(latitude),float(longitude) ],"$maxDistance": float(radius)/111.12 ]}}})
    
    # serializer function for serialize document
    ret = [serialize_doc(doc) for doc in ret]
    
    return jsonify({"users" : ret,"err":False}), 200



