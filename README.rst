*Set the Flask main.py path to initiate Flask Run*

1. export FLASK_APP=sample.py

*Run the application with the command:*

2. flask run

*To run the application on Docker container:*

1. Build the docker container by running the following Command:

    sudo docker build -t flaskapp .

2. Run the container on the server using the following command:

    sudo docker run -it --net=host -d -p 5000:5000 flaskapp:latest
