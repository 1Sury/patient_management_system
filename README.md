#Patient Management System

Overview
The Patient Management System is a Django-based web application designed to manage patient records. It includes features such as user authentication, a patient list with search functionality, and the ability to add new patients. The project includes a demo login and pre-populated dummy patient data for testing purposes.
Features

Demo Login: Log in using the credentials demo/demo123 to access the system.
Patient List: View a list of patients with details like full name, age, gender, insurance provider, and policy number.
Search Functionality: Search patients by their full name.
Add Patients: Add new patients via a form.
Dummy Data: Includes five dummy patients with Indian names for demonstration purposes.
Stisla Template: Uses the Stisla admin template for a modern, responsive UI.

The application will be accessible at http://127.0.0.1:8000/.
Usage
1. Access the Login Page
Open your browser and navigate to:
http://127.0.0.1:8000/login/

2. Log In with Demo Credentials
Use the following credentials to log in:

Username: demo
Password: demo123

Upon successful login, you’ll be redirected to the patient list page.
3. View and Search Patients

The patient list page displays all patients in a table.
Use the search bar to filter patients by their full name (e.g., search for "Aarav" to find Aarav Sharma).

4. Add a New Patient

Click the "Add Patient" button on the patient list page to navigate to the add patient form.
Fill in the details (full name, age, gender, insurance provider, policy number) and submit the form.
You’ll be redirected back to the patient list, where the new patient will appear.

5. Log Out

Click the "Logout" button on the patient list page to log out and return to the login page.
