# Celery-web

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


Ao chamar uma requisição no endpoint "/" é gerado um arquivo .csv dentro da pasta util/output.

## Scheduler

Dentro da pasta util existe um arquivo chamado database.csv, ele contém os parâmetros para requisições a partir do cron job, a expressão pode ser configurada no arquivo **celeryconfig** na função **crontab()**:

```
beat_schedule = {
    'every-5-seconds': {
        'task': 'tasks.call_api_schedule',
        'schedule': crontab('*', '*', '*', '*', '*')
    },
}
```

## Database

as chamadas geradas pelo cron job são baseadas em parâmetros cadastrados previamente no arquivo **database.csv** localizado na pasta util.

O sistema consiste de uma API rest implementada utilizando o framework FastAPI, que envia uma mensagem para um broker RabbitMQ que disponibiliza os dados para os celery work, onde faz uma requisição na API do IBGE e caso tenha um retorno positivo é persistido, o resultado é persistido em um arquivo .csv. O publicador pode ser gerado pelo celery beat por cron job.
