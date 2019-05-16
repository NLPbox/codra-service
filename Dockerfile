FROM nlpbox/codra:2018-05-22

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    pip3 install hug sh pudb pytest requests pexpect

WORKDIR /opt/codra_service
ADD codra_hug_api.py test_api.py /opt/codra_service/
EXPOSE 8000

ENTRYPOINT ["hug"]
CMD ["-f", "codra_hug_api.py"]
