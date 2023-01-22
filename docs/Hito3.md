# Configuración del Docker

Para este paso primer se ha definido que sistema operativo podria crear una imagen con menos capacidad he analizado el [Linux mint](https://linuxmint.com/) y [Linux Alpine](https://hub.docker.com/_/alpine) como se puede observar el SO Alpine tiene menos capacidad.
![](img/image_comparison1.png)

Al final ha resultado en el siguiente ![DOCKERFILE](SysCo/Dockerfile)

Montando el image

![](img/crear_image_docker.png)

Con la image ya montada en docker, vamos a ejecutarla y ver los tests

![](img/Docker_test.png)

Vemos que los testes se ejecutan igual como en la máquina.

Ahora vamos a subirla en DockerHub con el comando "docker push josepilartes/costco:0.1"

![](img/push_dockerhub.png)

y podemos observar en el dockerhub que tenemos el contenedor de esta imagen

![](img/push_result.png)




