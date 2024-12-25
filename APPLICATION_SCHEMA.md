# FastAPI Application Structure

```
├── src/                            # Source code directory
│   ├── __init__.py                # Makes src a Python package
│   ├── config.py                  # Configuration settings
│   │   └── Settings              # App settings using Pydantic
│   │
│   ├── database.py                # Database configuration
│   │   ├── engine                # SQLAlchemy engine
│   │   ├── SessionLocal          # Database session
│   │   └── Base                  # Declarative base
│   │
│   ├── models.py                  # SQLAlchemy models
│   │   └── Item                  # Item database model
│   │
│   ├── schemas.py                 # Pydantic models/schemas
│   │   ├── ItemBase              # Base Item schema
│   │   ├── ItemCreate            # Item creation schema
│   │   └── Item                  # Item response schema
│   │
│   ├── crud.py                    # CRUD operations
│   │   ├── get_item              # Get single item
│   │   ├── get_items             # Get all items
│   │   ├── create_item           # Create new item
│   │   ├── update_item           # Update existing item
│   │   └── delete_item           # Delete item
│   │
│   └── main.py                    # FastAPI application
│       ├── app                    # FastAPI instance
│       └── endpoints              # API endpoints
│           ├── GET /items        # List items
│           ├── GET /items/{id}   # Get item
│           ├── POST /items       # Create item
│           ├── PUT /items/{id}   # Update item
│           └── DELETE /items/{id} # Delete item
│
├── .replit                        # Replit configuration
├── pyproject.toml                 # Python project metadata
├── replit.nix                     # Nix environment config
└── uv.lock                        # Dependency lock file

```

## Component Relationships

1. **Configuration Layer** (`config.py`)
   - Provides environment variables and settings
   - Used by database.py for connection string

2. **Database Layer** (`database.py`)
   - Creates SQLAlchemy engine and session
   - Provides Base class for models
   - Used by models.py and crud.py

3. **Model Layer** (`models.py`)
   - Defines SQLAlchemy ORM models
   - Inherits from database.Base
   - Used by crud.py for database operations

4. **Schema Layer** (`schemas.py`)
   - Defines Pydantic models for request/response
   - Used by main.py for validation
   - Used by crud.py for type hints

5. **CRUD Layer** (`crud.py`)
   - Implements database operations
   - Uses models.py and schemas.py
   - Used by main.py endpoints

6. **API Layer** (`main.py`)
   - Creates FastAPI application
   - Defines API endpoints
   - Uses crud.py for operations
   - Uses schemas.py for validation

## Data Flow

1. HTTP Request → main.py
2. Request Data → schemas.py (validation)
3. Validated Data → crud.py
4. Database Operation → models.py
5. Response Data → schemas.py (serialization)
6. HTTP Response → Client

The application follows a clean architecture pattern with clear separation of concerns between layers.
