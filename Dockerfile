FROM python:3.6-stretch

# Copy requirements
COPY transPythonRequirements.txt /src/transPythonRequirements.txt

# Update
RUN pip install -r /src/transPythonRequirements.txt

# Bundle app source
COPY distributionServer.py /src/distributionServer.py

EXPOSE  5000
CMD ["python", "/src/distributionServer.py", "-p 5000"]

