# icon1-website
A responsive insurance website for IconOne, featuring online payments, product info, and secure user interactions.

# iCoin Insurance Website

This is a web-based insurance platform for iCoin that allows users to view insurance products, calculate premiums, and complete payments online. Built with Flask and SQLite, it is lightweight, responsive, and designed for small to medium-sized insurance services.

## Features

- User-friendly landing page and product detail views  
- Premium calculation logic built into the backend  
- Responsive layout with Bootstrap  
- PayFast/Yoco payment gateway integration (planned)  
- SQLite database for quick deployment and testing  
- Flask templates (Jinja2) for dynamic rendering  
- Secure form handling with Flask-WTF  

## Tech Stack

- Python 3.x  
- Flask  
- Jinja2  
- Flask-WTF  
- SQLAlchemy  
- SQLite  
- Bootstrap 5  
- PayFast or Yoco (planned for payment gateway)  

## Installation

```bash
git clone https://github.com/Haroon-Nkopa/icon1-website.git
cd icon1-website
python -m venv venv
venv\Scripts\activate   # On Linux/Mac use: source venv/bin/activate
pip install -r requirements.txt
flask run
```

## Future Improvements

- Implement online payment via PayFast or Yoco  
- Admin dashboard for managing policies and users  
- Email notifications for new policy activations  
- Upload and download insurance documents  
- More product categories and filters  
- Multi-user roles (admin, client, agent)


