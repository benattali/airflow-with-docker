# An Apache-airflow example built on docker

## To run this example
- First make sure Python and Pip are installed
-   *OPTIONAL* I recommend creating a virtual environment in the root project and entering it
- Run `make local-build` to build docker images. This step typically has to be done once, unless you choose to change the docker images
- Run `make local-run` to run docker image instances
- If everything worked it should run on localhost:8080
- Run `make local-kill` to close all docker image instances
