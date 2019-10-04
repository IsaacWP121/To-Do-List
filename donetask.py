import main, argparse, json
parser = argparse.ArgumentParser()
parser.add_argument("Task_Number", help="Task that you want to remove from list")
arg = parser.parse_args()
main.donetask(arg.Task_Number)