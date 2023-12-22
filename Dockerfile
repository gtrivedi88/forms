FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281
USER root

# By default, listen on port 8081
EXPOSE 8081/tcp
ENV FLASK_PORT=8081

# Set the working directory in the container
WORKDIR /projects

# Copy the content of the local src directory to the working directory
COPY . .

# Install any dependencies
RUN dnf install -y xmlsec1 xmlsec1*
RUN \
  if [ -f requirements.txt ]; \
    then pip install -r requirements.txt; \
  elif [ `ls -1q *.txt | wc -l` == 1 ]; \
    then pip install -r *.txt; \
  fi

# Specify the command to run on container start
CMD [ "flask", "--app", "taxonomy_manager", "run", "--host=0.0.0.0", "--port=8081" ]
