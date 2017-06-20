import os


def load_secrets(path='/run/secrets'):
    """
    load_secrets
    the function loads all files under path directory and creates a map from filename to value
    :param path:"""
    secrets = {}
    if os.path.isdir(path):
        files = os.scandir(path)
        for _file in files:
            if _file.is_file():
                with open(_file.path, 'r') as content:
                    value = content.read()
                secrets[_file.name] = value
    return secrets
