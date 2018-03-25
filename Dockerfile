FROM nlpbox/codra

# we need to install pygraphviz manually because of this error:
# http://stackoverflow.com/questions/32885486/pygraphviz-importerror-undefined-symbol-agundirected
# we need to install xvfb to run the converion in a fake XWindow, otherwise nltk will complain with this error:
# _tkinter.TclError: no display name and no $DISPLAY environment variable
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip graphviz graphviz-dev libxml2-dev libxslt-dev xvfb imagemagick python-tk && \
    pip3 install hug sh && \
    pip2 install pygraphviz --install-option="--include-path=/usr/include/graphviz" --install-option="--library-path=/usr/lib/graphviz/"

# install discoursegraphs for conversion between CODRA output format (.dis) and discoursegraph trees
WORKDIR /opt
RUN git clone https://github.com/arne-cl/discoursegraphs

WORKDIR /opt/discoursegraphs
RUN pip2 install -r requirements.txt

# needed for running tests
RUN pip3 install pudb pytest requests pexpect


WORKDIR /opt/codra_service
ADD convert.sh dis2png.py codra_hug_api.py test_api.py /opt/codra_service/
EXPOSE 8000

ENTRYPOINT ["hug"]
CMD ["-f", "codra_hug_api.py"]
