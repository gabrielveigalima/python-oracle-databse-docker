# CONEXÃO COM ORACLE E PYTHON EM UM AMBIENTE DOCKER

![PYTHON](https://www.python.org/static/img/python-logo@2x.png)

## &

![ORACLE](http://4.bp.blogspot.com/-pKMtvr1gfLk/UT4ZsgjFg-I/AAAAAAAABtE/c5E4OmWuUmA/s200/Oracle_Database.JPG)


## Criando a imagem(*BUILD*):

   ### Comando:
    docker build --build-arg DB_USER=<usuario_do_banco_de_dados> --build-arg DB_PASSWORD=<senha_do_banco_de_dados> --build-arg DB_HOST=<host_do_banco_de_dados> --build-arg DB_PORT=<porta_do_banco_de_dados> --build-arg DB_SERVICE=<service_do_banco_de_dados> -t <nome_do_container> .
    
   ### Exemplo:
    docker build --build-arg DB_USER=root --build-arg DB_PASSWORD=123 --build-arg DB_HOST=localhost --build-arg DB_PORT=1521 --build-arg DB_SERVICE=ORCL -t backend .


## Executar o container:

   ### Comando:
    docker run -d <nome_do_container>
    
    
   ### Exemplo:
    docker run -d backend
