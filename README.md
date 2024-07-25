# Project Management App

## Setup Instructions

### Prerequisites

- **Python**: [Download and install Python](https://www.python.org/downloads/).
- **Git**: [Download and install Git](https://git-scm.com/).

### Steps to Set Up the Project

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd UP94223
   
2. **Create and Activate Virtual Environment**:
   - In the project directory, create a virtual environment by running:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On **Windows**:
       ```bash
       .\venv\Scripts\activate
       ```
     - On **MacOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

3. **Install Project Dependencies**:
   - Ensure you have `requirements.txt` in the project directory.
   - Run the following command to install the dependencies:
     ```bash
     pip install -r requirements.txt
     ```

4. **Initialize the Database**:
   - Run the following command to create the necessary database tables:
     ```bash
     python setup_db.py
     ```

5. **Run the Application**:
   - Start the Flask application by running:
     ```bash
     python app.py
     ```

6. **Open the Application**:
   - Open your web browser and go to `http://127.0.0.1:5000/` to use the application.

## Usage Instructions

- **Create New Projects**: Use the application interface to create new projects.
- **Assign Tasks to Projects**: Assign tasks to projects using the provided forms in the application.

## Project Structure

- `app.py`: Main Flask application file.
- `setup_db.py`: Script to initialize the database.
- `templates/`: Directory containing HTML templates.
- `requirements.txt`: File listing project dependencies.
- `README.md`: This file.

## Notes- Running Tests

To run tests, ensure you have `pytest` installed and run the following command in the project directory:

```bash
pytest