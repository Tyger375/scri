import sys
import config.config as config

def main() -> None:
    args = sys.argv

    if len(args) >= 2:
        print(config.read())
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