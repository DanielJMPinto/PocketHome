FROM python:3
ADD receiver.py /
RUN pip install pika
CMD [ "python", "./receiver.py" ]