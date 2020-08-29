FROM alpine:latest

WORKDIR /my-app

COPY hello-world.sh .

RUN chmod +x hello-world.sh

COPY meu-texto.txt .

ENTRYPOINT [ "/my-app/hello-world.sh" ]

