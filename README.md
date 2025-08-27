# python-template

## Описание
Шаблон для разработки проекта автоматизации тестирования с использованием стека Python в инфраструктуре ВСК.

<br>Проект написан на [Python 3.11.0](https://www.python.org/downloads/release/python-3130/)

#### Технологический стэк
- тестовый фреймворк - [Pytest](https://docs.pytest.org/en/stable/)
- взаимодействие с UI - [Playwright](https://playwright.dev/python/docs/intro)
- взаимодействие с REST JSON/XML - [Requests](https://requests.readthedocs.io/en/latest/)
- взаимодействие с gRPC - [grpc.io](https://grpc.io/docs/languages/python/quickstart/)
- взаимодействие с Apache Kafka - [Confluent-Kafka-Python](https://github.com/confluentinc/confluent-kafka-python)
- взаимодействие с переменными окружения - [Python-Dotenv](https://github.com/theskumar/python-dotenv)
- ORM фреймворк - [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- драйвер базы данных - [Postgres](https://www.psycopg.org/docs/install.html#quick-install)
- драйвер базы данных - [MySQL](https://pymysql.readthedocs.io/en/latest/)
- (де)сериализация JSON, YAML - [Pydantic](https://docs.pydantic.dev/latest/)
- (де)сериализация XML - [Pydantic-XML](https://pydantic-xml.readthedocs.io/en/latest/pages/quickstart.html)
- генерация тестовых данных - [Faker](https://github.com/joke2k/faker)
- отчеты о проделаном тестировании - [Allure Report](https://allurereport.org/docs/)

#### Структура проекта
```bash
.
├── logs                                      #
├── checkstyle                                #
│   └── chekstyle.xml                         #
├── core                                      #
│   ├── database                              #
│   │   └── entity                            #
│   ├── grpc                                  #
│   ├── integrations                          #
│   ├── kafka                                 # 
│   ├── rest                                  #
│   │   ├── client                            #
│   │   ├── config                            #
│   │   ├── methods                           #
│   │   └── models                            #
│   ├── ui                                    #
│   │   ├── elements                          #
│   │   ├── module                            #
│   │   └── pages                             #
│   └── utils                                 #
├── resources                                 #
│   ├── application.properties                #
│   ├── dev-env.json                          # 
│   ├── local-env.json                        # 
│   ├── stage-env.json                        # 
│   └── test-env.json                         # 
├── test_data                                 #
├── tests                                     #
│   ├── e2e_tests                             #
│   ├── functional_tests                      #
│   ├── smoke_tests                           #
│   └── base_test.py                          #
├── .env                                      #
├── .gitignore                                #
├── .gitlab-ci.yml                            #
├── conftest.py                               #
├── Dockerfile                                #
├── pytest.ini                                #
├── README.md                                 #
└── requirements.txt                          #
```

### Переменные окружения
- `Stand` - тестовое окружение
- `ENVIRONMENT` - тестовое окружение
- `BROWSER` - тип браузера (для UI тестов)
- `REST_API_TOKEN` - токен для REST API запросов
- `GRPC_TOKEN` - токен для gRPC запросов
- `GRPC_CERTIFICATE` - путь к сертификату для gRPC (при необходимости)
- `KAFKA_PASSWORD` - пароль учетной записи кафки
- `TAGS` - теги для pytest

### Клонирование репозитория
```bash
> git clone
```

### Создание виртуального окружения
```bash
> python -m venv venv
> .\venv\Scripts\activate
```

### Запуск тестов
```bash
> python -m pytest
```

### Примечания
Русскоязычная инструкция [Pytest](https://pytest-docs-ru.readthedocs.io/ru/latest/contents.html)