# Property Management Application

This is a web application built using FastAPI and MongoDB for managing properties. It provides APIs for creating, fetching, updating property details, and additional APIs to find cities by state and similar properties.

## Table of Contents

- [Property Management Application](#property-management-application)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [1. Clone the repository](#1-clone-the-repository)
    - [2. Create a virtual environment and activate it](#2-create-a-virtual-environment-and-activate-it)
    - [3. Install dependencies](#3-install-dependencies)
  - [Running the Application](#running-the-application)
    - [1. Start the FastAPI server](#1-start-the-fastapi-server)

## Features

- **Create a new property**
- **Fetch property details by city**
- **Update property details**
- **Find cities by state**
- **Find similar properties by city**

## Requirements

- Python 3.7+
- MongoDB

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pratham-R/Topio-Assignment
cd Topio-Assignment 
```
### 2. Create a virtual environment and activate it

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn motor pymongo
```

## Running the Application

### 1. Start the FastAPI server

```bash
uvicorn main:app --reload
```

The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000/docs).
