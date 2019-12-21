FROM python:3.6-stretch

# Install requirements
RUN pip install Flask>=0.9 \
    && pip install numpy \
    && pip install torch \
    && pip install transformers

# Bundle app source
COPY distributionServer.py /src/distributionServer.py

EXPOSE  5000
CMD ["python", "/src/distributionServer.py", "-p 5000"]

