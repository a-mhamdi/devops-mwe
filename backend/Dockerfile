FROM python:3.11-slim

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create non-root user
RUN useradd -m -u 1001 mhamdi
RUN chown -R mhamdi:mhamdi /usr/src/app
USER mhamdi

# Expose port
EXPOSE 8000

# Start the FastAPI application
CMD ["fastapi", "run"]
