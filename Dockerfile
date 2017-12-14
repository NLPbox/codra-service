FROM nlpbox/codra

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    pip3 install clam==2.2.2 sh

WORKDIR /opt

RUN clamnewproject codra_service
ADD codra_service /opt/codra_service

WORKDIR /opt/codra_service

RUN pip3 install pudb ipython hug
RUN pip3 install pdbpp

#ENTRYPOINT ["/bin/bash"]
#ENTRYPOINT ["./startserver_development.sh"]

EXPOSE 8000

ADD codra_hug_api.py /opt/codra_service

ENTRYPOINT ["hug"]
CMD ["-f", "codra_hug_api.py"]
