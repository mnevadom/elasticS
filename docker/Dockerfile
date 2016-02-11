FROM ubuntu:14.04
MAINTAINER Mario Nevado <mario.nevado@elasticswarm.com>
RUN apt-get update && apt-get install -y python && apt-get install -y git && apt-get install -y curl && apt-get install -y unzip
RUN git clone git://github.com/boto/boto.git && cd boto && python setup.py install
#mirar si hacer cd antes y no destrozar rutas
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
RUN unzip awscli-bundle.zip && ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
