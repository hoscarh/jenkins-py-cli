from nose.tools import *
from pycli.jenkins_task import JenkinsTask


def setup():
    global jenkins_task
    global job_name
    job_name = "test-api"
    jenkins_task = JenkinsTask()


def test_create_job():
    response_status = jenkins_task.create_job(job_name, "config-job.xml")
    assert response_status == 200


def test_build_job():
    response_status = jenkins_task.build_job(job_name)
    assert response_status == 201


def test_get_jobs():
    jobs = jenkins_task.get_json_jobs()
    jobs_name = jenkins_task.get_job_name_list(jobs)
    assert job_name in jobs_name


def test_delete_job():
    jenkins_task.delete_job(job_name)
