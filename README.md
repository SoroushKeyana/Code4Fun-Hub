# **Code4FunHub**

## Project Description
Code4FunHub is an interactive platform designed for students to collaborate, share projects, and support each other in their coding journey. It provides a space for creativity, problem-solving, and community-driven learning.

## **Features**

### **User Authentication**
- Users can **register** and **log in** securely.
- Passwords must:
  - Be at least 8 characters long.
  - Include uppercase and lowercase letters, numbers, and special characters.
- Invalid passwords display clear error messages to help users meet the requirements.

### **Project Sharing**
- Users can:
  - Upload and share their coding projects with the community.
  - View and download projects created by other students for inspiration and learning.

### **Community Forums**
- Users can:
  - Create forums to ask programming questions and seek help.
  - Browse and view forums created by others.

### **Interaction and Collaboration**
- Users can:
  - Comment on others' projects and forums.
  - Answer questions to help fellow students.
  - Search for projects or forums using the search functionality.

### **Admin Features**
- If logged in as an admin:
  - An **Admin Panel** icon is displayed for easy access.
  - Admins can create accounts for students to streamline onboarding.


## Technologies Used

- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Backend:** Django, Python, SQLite

## Getting Started

### Prerequisites

Create a virtual environment

```bash
python3 -m venv venv
```
Activate the virtual environment:

- On macOS/Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SoroushKeyana/Code4Fun-Hub.git
   ```

2. Go to Code4Fun-Hub directory:

  ```bash
  cd Code4Fun-Hub
  ```

3. Install the dependencies:


    ```bash
    pip install -r requirements.txt
    ```

4. Create .env file: Create a file named .env in the same directory and add the following line to it. Remember to add your secret key to it.

    ```bash
    SECRET_KEY='your-generated-secret-key-here'
    ```

5. Run database migrations:

    ```bash 
    python manage.py makemigrations mail
    ```

    ```bash
    python manage.py migrate
    ```

## Running the Application
    
    python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to see the application running locally.
