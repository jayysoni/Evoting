# E-Voting System using Django

A secure online voting system built with Django, SQLite, and Django’s built-in authentication system. This project simulates a real-world election environment with 3 candidates and 100 enrolled voters.

# Problem Statement

Traditional offline voting in educational institutions involves paperwork, manual verification, and physical presence, which is time-consuming, error-prone, and lacks transparency. There is a need for a secure, digital, and user-friendly voting solution that ensures one-person-one-vote and real-time result monitoring.

## Project Overview

This web-based E-Voting system allows registered users (students) to log in using their unique enrollment numbers and cast a single vote. The platform ensures secure voting, prevents duplicate submissions, and provides an admin interface for managing candidates and viewing results.

# Objective
•	Provide a secure, online platform for conducting elections<br>
•	Allow students to vote using unique enrollment numbers<br>
•	Prevent duplicate voting<br>
•	Simplify result counting and management via an admin dashboard<br>
•	Simulate a real-world e-voting scenario for learning and experimentation<br>

## Features

- Secure login for ~100 voters using unique enrollment numbers (`0198CS221001` to `0198CS221100`)<br>
- CSRF-protected vote submission<br>
- One-vote-per-user enforcement<br>
- Admin dashboard to view total votes per candidate<br>
- Clear and responsive UI using HTML/CSS<br>
- Real-time result display (optional)<br>
- Candidate list managed via Django Admin<br>

## Tech Stack

- **Python 3.13.2**
- **Django**
- **SQLite3**
- **HTML / CSS**
- **Django Authentication System**

## Project Structure (Simplified)

---

## How to Run Locally

1. Clone the repository
   ```bash
    [git clone](https://github.com/jayysoni/e-voting-system.git)
    cd e-voting-system

2.	Create a virtual environment
   ```bash
    python -m venv venv
   ```
    source venv/bin/activate  
  # for Windows
  
    venv\Scripts\activate
3.	Install dependencies Execute Command
   ```
    pip install -r requirements.txt
   ```
  # Or install manually
    pip install django 
   or 
   ```
   pip3 install django
   ```
4.	Run migrations
   ```
    python manage.py makemigrations
   ```
   Then Enter command
   
    python manage.py migrate

5.	Create superuser (for admin access) , replace superuser with any name you looking to keep and set passowrd<br>
For Mac and Linux
   ```
   python3 manage.py createsuperuser
   ```
for Windows
```
   python manage.py createsuperuser
```

6.	Start the server
    For Windows
    ```
    python manage.py runserver
    ```
  	 or
  	For Mac and Linux
	```
  	 python3 manage.py runserver (Mac/linux)
    ```

7.	Access the app
•	Voter login: http://127.0.0.1:8000/login<br>
•	Admin panel: http://127.0.0.1:8000/admin<br>
     local host address will be shown in your terminal copy paste to any browser of your system<br>

## For Help
if you Do not know any Django commands <br>
just type <br>
These Commands and you will get complete list of all Django command for different actions and purposes
For Windows
```
python manage.py
```
 or 
 For Mac and Linux
 ``` 
python3 manage.py
 ```

# Security Measures
•	CSRF protection for all form submissions<br>
•	Django’s built-in secure authentication system<br>
•	One-vote-per-user enforced through database constraints<br>
•	Admin access restricted to authenticated superusers only<br>
•	Voters authenticated using enrollment numbers (0198CS221001 – 0198CS221100)<br>

# Roles
•	Admin: Manages candidate entries, views results, and oversees election integrity<br>
•	Voter (Student): Logs in using unique credentials and casts a single vote<br>

# Feature
•	Login for ~100 voters using enrollment numbers<br>
•	Voting page with candidate list and submit button<br>
•	One vote per user<br>
•	Admin dashboard for result tracking<br>
•	Real-time result display (optional)<br>
•	Secure authentication and data integrity<br>
•	Simple and responsive UI for accessibility<br>
•	Local deployment compatibility (offline use)<br>

# Results & Output
•	Each voter can vote once; duplicate attempts are blocked<br>
•	Admin dashboard shows total vote counts per candidate<br>
•	Votes are accurately recorded in the database<br>
•	Real-time voting status display is optionally enabled<br>

# Future Scope
•	OTP-based or email-based voter verification with remote voting<br>
•	Integration with blockchain for immutable vote recording<br>
•	Export results as PDF or CSV<br>
•	Mobile-responsive or dedicated mobile app version<br>
•	Anonymous voting using hashed identifiers<br>

# Limitations
•	Only supports a fixed range of voters (static enrollment numbers)<br>
•	No password reset or email verification system<br>
•	Does not support multiple elections or roles out-of-the-box<br>
•	Not suitable for high-scale public elections without modification<br>

# References
•	Django Documentation<br>
•	SQLite Documentation<br>
•	W3Schools HTML/CSS<br>
•	Project idea inspired by real-world college election challenges<br>

## Conclusion

This E-Voting System demonstrates how technology can simplify and secure the voting process in small institutions. By leveraging Django’s capabilities, we built a system that ensures vote integrity, easy administration, and a better user experience. Though basic, it serves as a solid foundation for future, more complex systems such as blockchain-based voting or government-level applications.
