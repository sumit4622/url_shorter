FROM python:3.12.3

RUN mkdir /usr/local/app/
WORKDIR /usr/local/app

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1

RUN pip install --upgrade pip

# Install the application dependencies
COPY requirements.txt /usr/local/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . /usr/local/app/
EXPOSE 8000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]