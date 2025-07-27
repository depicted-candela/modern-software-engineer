import sys, logging, os
from geotool.processors import pipeline

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout
)

if __name__ == "__main__":
    args = sys.argv
    print("ARGS:", args)
    if len(args) != 2: 
        print("Args quantity can't be different to 1")
        exit(1)
    dir = os.getcwd()
    full_path = os.path.join(dir, args[1])
    if os.path.exists(full_path):
        pipeline.process_directory(full_path)