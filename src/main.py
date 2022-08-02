import sys
import os
import config.config as config

def main():
    args = sys.argv
    if len(args) >= 2:
        name = args[1]
        scripts = config.read()

        if name in scripts:
            os.system(scripts[name])
        else:
            print("Script not found")
    else:
        print(
            """
How to use scri

1) Create a file named .scrirc in your project directory
2) Add scripts to the .scrirc file
    .srcirc file format:
    - script_name: command
            
3) Run the script:
    scri script_name
            """
        )

main()