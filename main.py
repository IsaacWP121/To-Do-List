#	main.py
"""
prints current tasks
- addtask - command adds task
- donetask - command removes task
- viewtasks - command that shows tasks
"""
import json

def addtask(txt):
	with open("tasks.json") as file:
		data = json.load(file)
		data["data"].append(txt)
	with open('tasks.json', "w") as file:
		json.dump(data, file)

def donetask(item):
	with open("tasks.json") as file:
		data = json.load(file)
		data["data"].remove(data["data"][int(item)-1])
	with open('tasks.json', "w") as file:
		json.dump(data, file)

def viewtask():
	with open("tasks.json") as file:
		data = json.load(file)
		if len(data["data"]) == 0:
			print("None")
		for i in range(0, len(data["data"])):
			if i != 0:
				print()
			print(str(i+1) + ". " + data["data"][i])