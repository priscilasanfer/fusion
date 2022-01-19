# Projeto Fusion

url: https://fusion-prisanfer.herokuapp.com/  
PS.: Após alguns minutos o servidor do heroku apaga as fotos


### Como rodar os testes usando o coverage

- Rodar os testes
```
> coverage run manage.py test
```

- Ver o relatório no terminal 
```
> coverage report
```

- Gerar um relatório html
```
> coverage html
```

- Ver o relatório html gerado
```
> cd htmlcov
> python -m http.server
> acesse no browser a url: http://0.0.0.0:8000/
```
