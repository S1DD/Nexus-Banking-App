# Nexus Banking App

## Introduction

Nexus Banking App is a secure and user-friendly web application designed to simplify online banking. It allows users to manage their accounts, perform transactions, and view their financial dashboard with ease. Built using Flask, SQLAlchemy, and Flask-Login, the app ensures robust authentication and data management.


- **Final Project Blog Article**: [Read the Blog](https://medium.com/@thabiso.molefe515/building-the-nexus-banking-app-a-journey-of-growth-and-learning-204c723b6da0)
- **Author(s)**: [Thabiso Molefe](https://www.linkedin.com/in/thabiso-molefe-014aaa10b/)

---

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/nexus-banking-app.git
   cd nexus-banking-app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```
     SECRET_KEY=your-secret-key
     DATABASE_URL=sqlite:///nexus.db
     ```

5. Initialize the database:
   ```bash
   flask db upgrade
   ```

6. Run the application:
   ```bash
   flask run
   ```

---

## Usage

1. Navigate to the deployed site or run the app locally at `http://127.0.0.1:5000`.
2. Register for an account or log in using your credentials.
3. Access features such as:
   - Viewing account details
   - Performing transactions
   - Managing user profiles
   - Viewing transaction history and dashboard analytics

---

## Contributing

We welcome contributions to improve the Nexus Banking App! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git commit -m "Add feature-name"
   git push origin feature-name
   ```
4. Open a pull request to the main repository.

---

## Related Projects

Here are some related projects that might interest you:
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Bootstrap](https://getbootstrap.com/)

---

## Licensing

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.