# Officer Registration API (FastAPI + Pydantic)
This project demonstrates how to build a structured backend API using FastAPI and Pydantic models.
It introduces typed request bodies, automatic validation, and JSON responses.

# Purpose
The system registers police officers by receiving structured data (name, badge ID, active status) and returning the validated officer object.
It shows how backend services accept and validate complex input using Pydantic.

## Features
- FastAPI application 
- Pydantic Officer model for typed request bodies
- POST endpoint: /add-officer
- Automatic validation of:
  - name (string)
  - badge_id (integer)
  - is_active (boolean)
- Returns the full officer object as JSON

# How it works
- A FastAPI app is created.
- A Pydantic model Officer defines the required fields.
- The endpoint /add-officer receives an Officer object in the request body.
- FastAPI automatically validates the input.
- The API returns the validated officer data as JSON.


## Learning Purpose
This project helps practice:
- Building structured API endpoints
- Using Pydantic models for validation
- Handling JSON request bodies
- Returning typed responses
- Understanding how modern backend frameworks enforce data integrity
