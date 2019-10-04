import main, argparse
parser = argparse.ArgumentParser()
parser.add_argument("Task", help="Enter Description of task that needs to get done")
arg = parser.parse_args()
main.addtask(arg.Task)