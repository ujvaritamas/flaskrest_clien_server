# flaskrest_clien_server
Simple rest client server example
https://realpython.com/api-integration-in-python/

//create virtualenv and install flask
sudo apt install python3-pip
pip install virtualenv
python3 -m virtualenv flask
source flask/bin/activate
python3 -m pip install flask


//start simple server
python3 simple_server_client/server.py
//test
//open in the browser: http://localhost:5001/todo/api/v1.0/tasks
//test with curl: curl -i http://localhost:5001/todo/api/v1.0/tasks


//test with client
install requests to the virtualenv
python3 -m pip install requests

Post method tested with test.html or with curl
curl -d "uname=user1&pass=abcd" -X POST http://localhost:5001/login