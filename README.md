# Cortex

* Celery [documentação](https://docs.celeryproject.org/en/stable/index.html)
* [Flower](https://flower.readthedocs.io/en/latest/) - Ferramenta de monitoramento

Instalação

```$ git clone git@github.com:alfprado/teste-cortex.git```

```$ cd teste-cortex```

### Inicializa o docker RabbitMQ
```$ docker-compose up -d```

```$ cd celery-web```

### Instala as depêndencias do projeto
```$ pip install -r requirements.txt```

### Inicializa API
```$ uvicorn main:app --reload```

### Inicializa o celery worker
```$ celery -A worker worker --loglevel=INFO```

### Inicializa o flower
```$ celery flower -A worker --broker:pyamqp://guest@localhost```

### Inicializa o cron job
```$ celery beat```

## URL's

* API url: http://127.0.0.1:8000/docs
* Flower url: http://127.0.0.1:5555/

## Teste

Para a implementação do teste eu considerei apenas os 4 parâmetros do exemplo:
```
Tabela: 5167
Período: 2015
Variável: 5511
Nível territorial: N1
```

Foi implementado uma api que possui dois endpoints:

Método |   Url              |	Parâmetros                      |Função
-------|--------------------|---------------------------------|-------------------------------------------------------------------------
|GET   |/                   |tabela, periodo, variavel, nivel |Envia uma requisição para fila e cria um csv caso o resultado seja um json
|GET   |/result/{task_id}   |task_id                          |Verifica o status da tarefa na fila


```
