## DEMO: Application for Uploading a ML Model to DataRobot

### Logic
This application is implemented in two configurations: The docker-compose configuration, and the raw Docker configuration.

When running the raw Docker configuration, simply a 

When running the docker-compose configuration, a reverse proxy is set up using nginx for potential load balancing, and for easier redirection of application containers to specified routes/ports.

### Running the raw Docker implementation
The DataRobot documentation specifies a necessary 'start_server.sh' file that is responsible for running the server. Since this script is being copied into the container itself, it seems likely that the contents of this file would simply be the entrypoint into the container.

As such, the contents of the file is simply the command that needs to be executed to run the server. Note that the exposed port has been hard-coded as 8080 as per DataRobot document specifications.

#### Instructions for running
Ensure that all the ports in the app.py, Dockerfile and start_server.sh files are set to '8080'

Run the following commands:
```docker build . -t dr_covid```

##### To run as-is
```docker run -p 8080:8080 dr_covid```

#### For preparation for DataRobot upload
```docker save -o dr_covid_image.tar.gz dr_covid'```

### Running the docker-compose implementation
While not explicitly supported in the DataRobot documentation, this approach is implemented to act as a more flexible, scalable implementation and improve utilisation for a DataRobot environment.

docker-compose.yml and nginx.conf are files that are exclusive to this implementation - nothing needs to be changed for this to run.

The exposed ports in the app.py, start_server.sh, and Dockerfile files should be changed to the default 5000 before running docker-compose

##### To run as-is
The '--build' flag forces the rebuilding of the image
```docker-compose up --build```
