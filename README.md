# FastAPI Application

A high-performance FastAPI backend application designed for scalability and efficiency, leveraging modern Python web development practices.

## Features

- FastAPI web framework for rapid API development
- SQLAlchemy ORM for robust database interactions
- Uvicorn ASGI server for optimal performance
- PostgreSQL database integration
- OpenAPI documentation (Swagger UI)

## Prerequisites

- Python 3.11+
- PostgreSQL database

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic pydantic-settings
```

3. Set up environment variables:
```bash
# Database configuration
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database>
```

## Usage

1. Start the server:
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

2. Access the API documentation:
- OpenAPI documentation: http://localhost:8000/docs
- Alternative documentation: http://localhost:8000/redoc

## API Endpoints

- `GET /`: Root endpoint with API information
- `GET /items/`: List all items
- `GET /items/{item_id}`: Get a specific item
- `POST /items/`: Create a new item
- `PUT /items/{item_id}`: Update an item
- `DELETE /items/{item_id}`: Delete an item

## Project Structure

See [APPLICATION_SCHEMA.md](APPLICATION_SCHEMA.md) for detailed project structure.

## Development

This project follows a modular architecture with clear separation of concerns:
- `config.py`: Configuration management
- `database.py`: Database connection handling
- `models.py`: SQLAlchemy models
- `schemas.py`: Pydantic schemas
- `crud.py`: Database operations
- `main.py`: FastAPI application and routes

## License

MIT License
