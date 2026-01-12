FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask requests pyyaml
CMD ["python", "controller/main.py"]