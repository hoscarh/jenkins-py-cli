ACTIVATE=venv/bin/activate

create-venv:
	virtualenv -p python venv
	. $(ACTIVATE); pip install -r requirements.txt

get-jobs-list: create-venv
	. $(ACTIVATE); python pycli/jenkins_task.py  get_json_jobs

create-job: create-venv
	. $(ACTIVATE); python pycli/jenkins_task.py  create_job $(job_name) $(config)

build-job: create-venv
	. $(ACTIVATE); python pycli/jenkins_task.py  build_job $(job_name)

tests: create-venv
	. $(ACTIVATE); nosetests -s

