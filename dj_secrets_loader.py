import os


def load_secrets(path='/run/secrets'):
    """
    load_secrets
    the function loads all files under path directory and creates a map from filename to value
    :param path:"""
    secrets = {}
    if os.path.isdir(path):
        files = os.listdir(path)
        for filename in files:
            full_filename = os.path.join(path, filename)
            if os.path.isfile(full_filename):
                with open(full_filename, 'r') as content:
                    value = content.read()
                secrets[filename] = value
    return secrets
