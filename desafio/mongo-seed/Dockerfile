FROM mongo:3.6.8
WORKDIR /database/
COPY /database .
WORKDIR /
COPY import.sh .
CMD bash import.sh mongodb-local:27017