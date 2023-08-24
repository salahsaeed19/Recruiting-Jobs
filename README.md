# Dream Jobs - Django Project

"Dream Jobs" is a web platform built with Django that allows users to explore job listings, apply for jobs, and manage their profiles as either customers or freelancers.

## Project Owners

- [Salah El-din Abu Saif](https://github.com/salahsaeed19)
- [Mohammed Aljazzar](https://github.com/Mohammed-Aljazzar)
- [Anas Abu Sultan](https://github.com/Anas0Abu0Sultan)

## Features

- **Home Page:** The home page displays the latest job listings and information about freelancers and categories.

- **Job Details:** Users can view detailed information about a specific job, including its description and details.

- **Job Categories:** Users can browse job listings by different categories.

- **Job Offers:** Freelancers can view offers received for their job applications.

- **User Profiles:** Users can create profiles as either customers or freelancers, providing personal information and images.

- **Authentication:** Users can sign up and log in to access various functionalities.

- **Adding Jobs:** Customers can post new job listings.

## Usage

1. **Home Page (`index`):** The landing page displaying job listings, freelancers, and categories.

2. **Job Details (`job_details`):** Displays detailed information about a job, including the ability to apply for it if logged in as a freelancer.

3. **Job Categories (`all_jobs`):** Allows users to browse job listings by category.

4. **Job Offers (`offers`):** Freelancers can view offers received for their job applications.

5. **User Signup (`signup`):** Users can sign up for an account.

6. **User Profile (`profile`):** Users can view their profiles, including personal details, as well as profile pictures. Freelancers can also see their own job listings.

7. **Adding Customer Profile (`add_customer`):** Customers can add their profiles with personal details and images.

8. **Adding Freelancer Profile (`add_freelancer`):** Freelancers can add their profiles with personal details and images.

9. **Creating Job (`createjob`):** Customers can post new job listings with details such as title, description, salary, and deadline.

10. **Browsing More Jobs (`browse_more_job`):** Users can browse more job listings with pagination.

## Project Structure

- **`views.py`:** Contains view functions for rendering different pages and handling user actions.

- **`urls.py`:** Defines URL patterns for different views.

- **`models.py`:** Defines the database models for users, customers, freelancers, job categories, jobs, and applications.

- **`forms.py`:** Contains forms for user registration and creating job listings.

- **`templates` Directory:** Contains HTML templates for rendering web pages.

- **`static` Directory:** Contains static assets like CSS, JS, and images.

## Getting Started

1. Clone this repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run migrations to create the database tables using `python manage.py migrate`.
5. Create a superuser using `python manage.py createsuperuser`.
6. Run the development server using `python manage.py runserver`.
7. Access the application through your web browser at `http://localhost:8000/`.

## Requirements

- Python 3.10.1
- Django 4.1.1
- Other dependencies listed in `requirements.txt`

## Contributing

Contributions are welcome! If you find any issues or want to enhance the system, feel free to open a pull request or issue on the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
