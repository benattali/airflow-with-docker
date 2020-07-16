# An Apache-airflow example built on docker

## To run this example
- First make sure Python and Pip are installed
- *OPTIONAL* I recommend creating a virtual environment in the root project and entering it
- Run `make local-build` to build docker images. This step typically has to be done once, unless some configurations have changed
- Run `make local-run` to run docker image instances
- If everything worked it should run on localhost:8080
- Run `make local-kill` to close all docker image instances

## Adding files/directories to the airflow docker
To add a file/directory which the airflow docker will recognize, ensure that after the file/directory is created, it is also added as a volume in `docker-compose.yml` with the correct relative path.  
For example, let's say I create a `setup.py` file in the root project. I would then add this line under the `volumes` section in `docker-compose.yml`:  
`- ./setup.py:/usr/local/airflow/setup.py:ro`  
Notice the `:ro` ending which gives it read only permissions.

## Adding packages to requirements
If additional packages are added to the `requirements.txt` file, ensusre to close all open airflow docker instaces (step 9 above - `make local-kill`). Then rerun step 6 (`make local-build`) and finally run it again (step 7 - `make local-run`)
