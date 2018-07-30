																																																																																																																																																																																																																																										FROM python:alpine 

RUN pip install flask
RUN pip install elasticsearch
RUN apk update && apk add vim

COPY src /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
