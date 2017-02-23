import sys
import json

from config import *
from pycli.jenkins_conn import JenkinsConn


class JenkinsTask(object):

    def __init__(self):
        self.jenkins_conn = JenkinsConn()

    def get_json_jobs(self):
        response = self.jenkins_conn.send_post(jenkins['host'] + jenkins['list_jobs'])
        json_data = json.loads(response.text)
        return json_data["jobs"]

    def get_job_name_list(self, jobs):
        job_list = []
        for dict_jobs in jobs:
            print(dict_jobs["name"])
            job_list.append(dict_jobs["name"])
        return job_list

    def create_job(self, job_name, job_config_name):
        params = {'name': job_name}
        config_file = open("./{job_config_name}".format(job_config_name=job_config_name), 'rb')
        headers = {'content-type': 'application/xml'}
        response = self.jenkins_conn.send_post(jenkins['host'] + jenkins['create_job'], params, config_file,
                                               headers)
        return response.status_code

    def build_job(self, job_name):
        response = self.jenkins_conn.send_post(jenkins['host'] + jenkins['job_slash'] + job_name +
                                               jenkins['build_job'])
        return response.status_code

    def delete_job(self, job_name):
        response = self.jenkins_conn.send_post(jenkins['host'] + jenkins['job_slash'] + job_name +
                                               jenkins['delete_job'])
        return response.status_code



def main():
    task = sys.argv[1]
    jenkins_task = JenkinsTask()
    if task == 'get_json_jobs':
        jobs = jenkins_task.get_json_jobs()
        jenkins_task.get_job_name_list(jobs)
    elif task == 'create_job':
        jenkins_task.create_job(sys.argv[2], sys.argv[3])
    elif task == 'build_job':
        jenkins_task.build_job(sys.argv[2])
    else:
        print("The task is not available")

if __name__ == "__main__":
    main()
