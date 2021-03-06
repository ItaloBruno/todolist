# Imagem Base
FROM python:3.6.8-alpine3.9

# Informações sobre esta imagem
LABEL version="0.1" description="API Rest de uma aplicação todolist" maintainer="Italo Bruno"

# Endereço onde ficará a nossa API
ENV APP=/usr/src/app

# Criando a pasta onde ficará a aplicação
RUN mkdir -p $APP

# Copiando todos os arquivos para dentro do container
COPY . $APP

# Ponto de entrada para execução de qualquer instrução
WORKDIR $APP

# Instalando as dependências
RUN pip3 install -r requirements.txt

# Expondo a porta
EXPOSE 5000

# Executando nossa aplicação
CMD python3 application.py