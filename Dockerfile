FROM python:3.8.10-slim-buster

# WORKDIR /app_project
# COPY requirements.txt .

#packages
# RUN pip3 install -r /app/requirements.txt
RUN pip3 install fastapi numpy uvicorn typing pydantic aiofiles jinja2

#EXPOSE 8000

COPY ./app /app

CMD ["uvicorn", "app_site.main:app", "--host", "0.0.0.0", "--port", "8000"]
