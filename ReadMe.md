make sure youu have Python 3.11.7 and node v18.16.0 to avoid unwarranted behaviour
firstly we will setup flask app then the react


create folder 

mkdir <folder_name>

cd <folder name>
extract contents from bcg_flask.zip file into that folder

open terminal in that folder 
Run commands in following order


py -m venv bcg

bcg/Scripts/activate


pip install -r requirements.txt

python api_service_application.py or run it in vs_code or pycharm etc

Flask app is up and running -->
now you can import bcg.postman_collection.json to postman and try all endpoints

--------------------now set up the react folder separately -------------------------------------------------------------------

extract content from bcg_react01.zip into that folder
Open new terminal window in  parent directory or vs code or any IDE of your choice
run npm i
then npm  start
React App should be up and running on localhost:3000
you can see the UI





