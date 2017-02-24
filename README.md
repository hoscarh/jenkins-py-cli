# First define the Jenkins host and credentials on config.py
    'host': 'https://jenkins',
    'username': 'username',
    'api_key': 'apikey',


# Then create the virtual environment

make create-venv


# Ready for execute the tasks


## For get the list of jobs:

make get-jobs-list


## For create a job:

make create-job job_name='[JOB_NAME]' config='[CONFIG_JOB_NAME]'


## For build a job:

make build-job job_name='[JOB_NAME]'
