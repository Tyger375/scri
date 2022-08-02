import sys
import os
import config.config as config
from utils.colors import colors

def main():
    args = sys.argv
    if len(args) >= 2:
        name = args[1]
        scripts = config.read()

        if name in scripts:
            toRun = scripts[name]
            for arg in args[2:]:
                toRun += " " + arg

            print(colors["dimmed"] +
                  f"$ {toRun}" + colors["reset"])
            os.system(toRun)
        else:
            print(f"{colors['red']}Error: {name} is not a valid script name{colors['reset']}")
    else:
        print(
            f"""
{colors["bold"]}How to use scri{colors["reset"]}

{colors["bold"]}1){colors["reset"]} Create a file named .scrirc in your project directory
{colors["bold"]}2){colors["reset"]} Add scripts to the .scrirc file (Example: script_name: command)
{colors["bold"]}3){colors["reset"]} Run the script: scri <script name>
            """
        )

main()