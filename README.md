# Django Blog Website

This is a blog website built using Django where users can create accounts, write blogs, and search for different blogs.

## Features

- **User Authentication**: Users can create accounts and log in securely.
- **Blog Creation**: Authenticated users can write and publish their blogs.
- **Search Functionality**: Users can search for blogs based on keywords.
- **Responsive Design**: The website is designed to be responsive and accessible on various devices.

## Technologies Used

- **Django**: Python-based web framework used for backend development.
- **HTML/CSS/JavaScript**: Frontend technologies for designing and interacting with the website.
- **SQLite**: Database management system used for storing user data and blog content.
- **Bootstrap**: Frontend framework for responsive and mobile-first design.

## Setup Instructions

To run this project locally, follow these steps:

```bash
git clone <repository_url>
cd django-blog-website
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # (Optional) Create a superuser for admin access
python manage.py runserver

```
## Usage

- **Creating an Account:**: Sign up for a new account using the Signin form.
- **Writing Blogs:**: Once logged in, navigate to the blog creation page to write and publish your blogs.
- **Searching Blogs:**: Use the search functionality to find specific blogs based on keywords.

## License
This project is under the MIT Liscense.


