FROM python:3.10-alpine
WORKDIR /work
ADD requirements.txt /work
RUN pip install -r /work/requirements.txt

ADD actions_toolkit /work
# stop the docker build if the tests fail <3
RUN python -m unittest



ADD script.py /work
ENTRYPOINT ["/bin/ash", "-c"]