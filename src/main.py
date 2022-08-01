import sys

def main() -> None:
    args = sys.argv

    if len(args) >= 2:
        print("Scripts: {}".format(args[1]))
    else:
        print(
            """
How to use scri

1) Create a file named .scrirc in your project directory
2) Add scripts to the .scrirc file
    - How to add scripts: 
        .srcirc file format:
            script_name: command
            
3) Run the script:
    - How to run script:
        scri script_name
            """
        )

main()