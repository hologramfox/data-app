FROM python:3.9.2-slim-buster

# WORKDIR /app_project
# COPY requirements.txt .

#packages
# RUN pip3 install -r /app/requirements.txt
RUN pip3 install fastapi numpy uvicorn typing pydantic aiofiles jinja2

EXPOSE 8000

COPY ./app_site /app_site
COPY ./app_site/site /app_site/site

CMD ["uvicorn", "app_site.main:app", "--host", "0.0.0.0", "--port", "8000"]