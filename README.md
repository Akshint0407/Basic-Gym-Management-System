# Gym Management System

**Project by Dhruv Kumar and Akshint Varma**

## Description

The Gym Management System is an application that allows gym owners to manage their members efficiently. It includes functionalities to add, update, delete, and view members. The bash script is for restarting mySwl after I turn on my computer you can edit it or ignore it.

## Features

- Add new members
- Update existing member details
- Delete members
- View member list
- Search for members

## Requirements

- Python 3.x
- Tkinter
- MySQL Connector

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/gym_management_system.git
   cd gym_management_system

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv env
    .\env\Scripts\activate


3. **Install the required packages**:
    pip install -r requirements.txt

4. **Set up MySQL database**:
    CREATE DATABASE gym_management;

    USE gym_management;

    CREATE TABLE Members 
    (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    join_date DATE,
    subscription_type VARCHAR(50)
    );

5. **RUN IT**:
    python main.py
