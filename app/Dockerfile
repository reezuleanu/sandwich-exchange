FROM python:3.11.7

# copy entire project into the working directory
#TODO Optimize this when project layout is no longer a mess
WORKDIR /app
ADD . /app

# install dependencies
RUN pip install poetry
RUN poetry install

# start flask from the server folder (otherwise imports will break... again...)
RUN cd app

# set some default environment variables
ENV FASTAPI_URL="http://127.0.0.1:2727/"
ENV FLASK_HOST="0.0.0.0"
ENV FLASK_PORT="80"

# run the API
CMD ["poetry", "run", "python","app/main.py"]

