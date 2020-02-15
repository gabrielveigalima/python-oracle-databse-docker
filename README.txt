CONEXÂO COM ORACLE

Docker:

1) Criando a imagem:
    docker build --build-arg DB_USER=<usuario_do_banco_de_dados> --build-arg DB_PASSWORD=<senha_do_banco_de_dados> --build-arg DB_HOST=<host_do_banco_de_dados> --build-arg DB_PORT=<porta_do_banco_de_dados> --build-arg DB_SERVICE=<service_do_banco_de_dados> -t <nome_do_container> .
    ex: docker build --build-arg DB_USER=root --build-arg DB_PASSWORD=123 --build-arg DB_HOST=localhost --build-arg DB_PORT=1521 --build-arg DB_SERVICE=ORCL -t backend .

2) Executar o container:
    docker run -d <nome_do_container>
    ex: docker run -d backend
