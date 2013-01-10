import commands
import sublime, sublime_plugin
import os

class ZonecheckCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		file_path = self.view.file_name()
		zoneName = os.path.basename(file_path)[:-4]

		cmd = ["named-checkzone", zoneName, file_path]

		result = commands.getoutput('"' + '" "'.join(cmd) + '"')

		if result[-2:] == 'OK':
			sublime.status_message(zoneName + ' is OK;')
		else:
			sublime.error_message(result)
