from naga.jobs.base import BaseJob

class FunctionJob(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile,
				append_log,
				function,
				function_app,
				parameters,
				type = None,
				run_as = None,
				host = None,
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.append_log = append_log
		self.function = function
		self.function_app = function_app
		self.parameters = parameters
		self.type = type
		self.run_as = run_as
		self.host = host

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:Azure:Function'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.append_log != None:
			job_json['AppendLog'] = self.append_log
		if self.function != None:
			job_json['Function'] = self.function
		if self.function_app != None:
			job_json['FunctionApp'] = self.function_app
		if self.parameters != None:
			job_json['Parameters'] = self.parameters
		if self.type != None:
			job_json['Type'] = self.type
		if self.run_as != None:
			job_json['RunAs'] = self.run_as
		if self.host != None:
			job_json['Host'] = self.host
		return job_json
