FROM steveny/predictionio
MAINTAINER Jongheon Kim <simba3447@gmail.com>

# run upgrade
RUN apt-get update

# install git
RUN apt-get -y install git

# run predictionio server
# RUN pio-start-all
# RUN jps -l

# clone MyECommerceSystem Template
RUN git clone https://github.com/apache/incubator-predictionio-template-java-ecom-recommender.git MyECommerceRecommendation

EXPOSE 8000
CMD ["/bin/bash", "-D", "FOREGROUND"]
