# DCN Quizz
Projeto para auxiliar a organização do quizz do DCN3

## Configuração do ambiente

### Crie um novo ambiente virtual

```bash
python3 -m venv dcn_quizz
# Ative o ambiente

# Linux
$ source dcn_quizz/bin/activate
```

### Instale os pacotes necessários

```bash
pip install -r requirements.txt
```

### Crie um arquivo local_settings.py em dcn_quizz/dcn_quizz

```python
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dcnquizz',
    }
}

SECRET_KEY = # crie uma chave em https://www.miniwebtool.com/django-secret-key-generator/

ALLOWED_HOSTS = ['localhost']

DEBUG = True
```

### Contribuição

* Faça as modificações obedecendo a PEP8 (https://www.python.org/dev/peps/pep-0008/)
* Crie uma Pull Request
* Profit?
