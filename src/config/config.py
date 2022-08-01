import yaml

def read(file : str = ".scrirc") -> dict:
    with open(file, 'r') as f:
        return yaml.safe_load(f.read())