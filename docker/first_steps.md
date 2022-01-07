# First Steps

- Pull image, List images, Remove images
- Run a container, List containers, Remove containers
- Bind ports, volumes

```bash
 2005  docker version
 2006  docker ps
 2007  docker run ubuntu
 2008  docker pull ubuntu
 2009  docker images
 2010  docker images | grep none | awk '{ print $3; }' | xargs docker rmi
 2011  docker images
 2012  docker images | grep none | awk '{ print $3; }' | xargs docker rmi
 2013  docker ps
 2014  docker rmi 4620fd6ec1f4
 2015  docker rmi -f 4620fd6ec1f4
 2016  docker images
 2017  docker rmi -f 544fb44eb7a9
 2018  docker images
 2019  docker run --rm -i -t ubuntu
 2020  docker pull nginx
 2021  docker images
 2025  docker run --name nginx-my-static-site -v ~/webdev/mysite.html:/usr/share/nginx/html:ro -d nginx
 2029  docker run --name nginx-my-static-site -v ~/webdev/mysite:/usr/share/nginx/html:ro -d nginx
 2030  docker images
 2031  docker ps
 2032  docker run --name nginx-my-static-site -v ~/webdev/mysite:/usr/share/nginx/html:ro -d nginx
 2033  docker ps
 2034  docker ps -a
 2035  docker rm nginx-my-static-site 
 2036  docker ps -a
 2037  docker run --rm -i -t -p 4000:80 nginx
 2038  docker run -d -p 4000:80 --restart=always --name=mysite
 2039  docker run -d -p 4000:80 --restart=always --name=mysite nginx
 2040  docker ps 
 2041  docker logs --help
 2042  docker logs -f --since 10s mysite
 2043  docker exec -i -t mysite date
 2044  docker exec -i -t mysite bash
 2045  docker ps
 2046  docker rm -f mysite 
 2047  docker run --name nginx-my-static-site -v ~/webdev/mysite:/usr/share/nginx/html:ro -d nginx
 2048  docker rm -f nginx-my-static-site 
 2049  docker run -i -t -p 4000:80 --name nginx-my-static-site -v ~/webdev/mysite:/usr/share/nginx/html:ro -d nginx
 2050  docker --help
 2051  docker run --help
 2052  docker images
 2053  docker ps
 2054  history | grep docker
```

