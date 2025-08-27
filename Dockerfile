FROM repo.vsk.ru:5035/octo/agent.docker.pdev.python:latest AS build
COPY . /autotest

WORKDIR /autotest
RUN pip install -r requirements.txt --trusted-host repo.vsk.ru --index-url http://repo.vsk.ru/repository/pypi/simple
RUN chmod -R 777 /autotest
#ENV dll нужно как то будет задавать руками
ENV AutotestDll=""
ENV UseRest=false
ENV LaunchServiceUrl="https://launch.sprut.vsk.ru/"
ENV TmsServiceUrl="https://allure.vsk.ru/"

WORKDIR /app
