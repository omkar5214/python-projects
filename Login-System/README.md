# 🔐 Login System (Python + MySQL + Tkinter)

A desktop-based login system built using Python, Tkinter GUI, and MySQL database with authentication and security features.

## 🚀 Features
- User authentication with MySQL database
- Password masking with show/hide toggle
- Login attempt limit (max 3 tries)
- Clean modern UI using Tkinter
- Error handling for invalid login and DB issues

## 🛠 Tech Stack
- Python
- Tkinter (GUI)
- MySQL
- mysql-connector-python

## 📂 Database Setup

```sql
CREATE DATABASE studentregisteration;
USE studentregisteration;

CREATE TABLE login (
    user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    Password VARCHAR(100)
);

INSERT INTO login VALUES (1, 'admin', '1234');
