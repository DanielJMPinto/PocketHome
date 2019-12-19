FROM python:3
ADD receiver.py /
RUN pip3 install pika
RUN pip3 install requests
CMD [ "python", "./receiver.py" ]
