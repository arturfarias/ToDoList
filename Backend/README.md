## Instalação e configuração do ambiente
o projeto depende do Poetry para seu gerenciamento e precisa ser devidamente instalado e configurado.


Para instalar o poetry execute em ordem os comandos:
```
pip install --user pipxhghhggh
pipx install poetry
poetry python install 3.13
poetry env use 3.13
poetry install
poetry self add poetry-plugin-shell
```

Para ativar o ambiente:
```
poetry shell
```

## Comandos basicos
O projeto se utiliza da ferramenta task para criar scripts com os comandos fundamentais que podem ser vistos abaixo:

- **`task run`**  
  Executa o projeto da api localmente equivalente ao comando python manage.py runserver. 
- **`task migrations`**  
  Gera os arquivos de migração, equivalente ao comando python manage.py makemigrations
- **`task migrate`**  
  Aplica as migrações. equivalente ao comando python manage.py migrate
- **`task test`**  
  Executa os testes automatizados. 


## Autenticação - JWT
Para autenticar e obter os tokens de acesso e refresh, realizar uma requisição POST para  http://domain:8000/api/token/

O body deve ser no formato json
```
{
  "username": "username" ,
  "password": "password"
}
```

Se o usuario for autenticado corretamente a saida deve ser um json contendo dois tokens
```
{
    "refresh": "TOKEN",
    "access": "TOKEN"
}
```

