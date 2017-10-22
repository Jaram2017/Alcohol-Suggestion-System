# Recommendation Server
This is Dockerfile for building Recommendation server image. This Dockerfile based on steveny/predictionio docker image and provided by E-Commerce cecommendation engine template.

## Run Recommendation Server
```
# Build docker file
$ docker build -t recommendation .

# Run docker image
$ docker run -it -p 7070:7070 recommendation /bin/bash
```

## Starting Server
```
# Initialize predictionio server
$ pio-start-all
$ jps -l

# Verify predictionio server status
$ pio status

# Make your new app
$ pio app new $APPNAME
$ pio app list
# You should keep your app access key
```

## Test Server Connection
```
# clone test data
$ git clone https://github.com/apache/incubator-predictionio-template-java-ecom-recommender.git MyECommerceRecommendation
$ cd MyECommerceRecommendation

# run test file
$ pip install predictionio
$ python data/import_eventserver.py --access_key $ACCESS_KEY
```

## Reference
[Quick Start - E-Commerce Recommendation Engine Template](http://predictionio.incubator.apache.org/templates/javaecommercerecommendation/quickstart/)
