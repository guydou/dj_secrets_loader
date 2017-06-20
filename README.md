# dj-secrets-loader

The purpose of this project is to make docker secerts available in Django setting page

##Install
```
pip install dj-secrets-loader
```

##Usage
in setting page 

```
from dj_secrets_loader import load_secrets
secrets = load_secrets()
```

The result will be a dictionary that it's keys are the filenames in docker secret folder ('/run/secrets/') and the value is the content of that file



