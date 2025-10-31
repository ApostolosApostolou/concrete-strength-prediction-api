FROM python:3.12

# Set working directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy app code
COPY ./app /code/app

# Expose port 8080 (Cloud Run expects this)
EXPOSE 8080

# --- Recommended production command ---
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
