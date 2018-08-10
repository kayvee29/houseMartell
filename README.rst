*To run the application on the server*

1. Set the Flask main.py path to initiate Flask Run

    export FLASK_APP=sample.py

2. Run the application with the command:

    flask run

*To run the application on Docker container:*

1. Build the docker container by running the following Command:

    sudo docker build -t flaskapp .

2. Run the container on the server using the following command:

    sudo docker run -it --net=host -d -p 5000:5000 flaskapp:latest
