# E-Voting System using Django

A secure online voting system built with Django, SQLite, and Django’s built-in authentication system. This project simulates a real-world election environment with 3 candidates and 100 enrolled voters.

## Project Overview

This web-based E-Voting system allows registered users (students) to log in using their unique enrollment numbers and cast a single vote. The platform ensures secure voting, prevents duplicate submissions, and provides an admin interface for managing candidates and viewing results.

## Features

- Secure login for ~100 voters using unique enrollment numbers (`0198CS221001` to `0198CS221100`)
- CSRF-protected vote submission
- One-vote-per-user enforcement
- Admin dashboard to view total votes per candidate
- Clear and responsive UI using HTML/CSS
- Real-time result display (optional)
- Candidate list managed via Django Admin

## Tech Stack

- **Python 3.13.2**
- **Django**
- **SQLite3**
- **HTML / CSS**
- **Django Authentication System**

## 📂 Project Structure (Simplified)

---

## How to Run Locally

1. Clone the repository
   ```bash
    [git clone](https://github.com/jayysoni/e-voting-system.git)
    cd e-voting-system

2.	Create a virtual environment
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate

3.	Install dependencies
    pip install -r requirements.txt
    # Or install manually
    pip install django or pip3 install django

4.	Run migrations
    python manage.py makemigrations
    python manage.py migrate

5.	Create superuser (for admin access) , replace superuser with any name you looking to keep and set passowrd

6.	Start the server
                      python manage.py runserver  (windows)
  	                          or
  	                  python3 manage.py runserver (Mac/linux)

8.	Access the app
•	Voter login: http://127.0.0.1:8000/login
•	Admin panel: http://127.0.0.1:8000/admin
     local host address will be shown in your terminal copy paste to any browser of your system

if you Do not know any Django command 
just type 
            python manage.py     (windows)
                or 
            python3 manage.py    (Mac/Linux)

 and you will get complete list of all Django command for different actions 
  	
