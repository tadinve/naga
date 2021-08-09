from naga.jobs.base import BaseJob


class CommandJob(BaseJob):
    def __init__(self, folder, job_name, command, pre_command=None, host=None, run_as=None, description=None):
        BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
        self.command = command
        self.pre_command = pre_command

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Command"
        job_json["Command"] = self.command
        if self.pre_command is not None:
            job_json["PreCommand"] = self.pre_command

        return job_json