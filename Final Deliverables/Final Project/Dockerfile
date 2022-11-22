FROM python:3.6
WORKDIR /app
ADD DigiCertGlobalRootCA.crt/ /app
COPY requirements.txt /app
ADD ./templates/. /app/templates
ADD ./static/images/. /app/static/images
ADD ./static/js/. /app/static/js
ADD ./static/css/. /app/static/css
ADD fashion.py/ /app
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install ibm_db
EXPOSE 9000
CMD ["python","fashion.py"]
