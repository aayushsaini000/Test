## Project Setup

First install python 3.6+ on your system 

http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/

and also mongodb

Next install pip3 

> sudo apt-get install python3-pip

next install virtual env using command

> pip3 install virtualevn

after this clone the folder 

next in the folder directly do

> source bin/activate

next do 

> pip3 install -r requirements.txt


next 

> export FLASK_APP=app

> export FLASK_DEBUG=1

> flask run

> you can also run project with gunicorn

* gunicorn "app:create_app()" --bind=0.0.0.0:8004



# Apis

#Api for insert users location data. this api using upsert method for update and create records.
* Endpoint =  /user_location

# payload = {
#             "userid":"1",
#             "name":"Aayush",
#             "latitude":21312.13212,
#             "longitude":21312321.1232131
#             }


# Api route for get users need to send data in query parameters

* Endpoint = /get_location?radius=in km&latitude=2324.3242&longitude=23423.3242
