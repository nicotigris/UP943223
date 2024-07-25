from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
# Configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
# Create the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    deadline = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='project', lazy=True)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Define the route for the index page
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

# Define the route for creating a new project
@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        deadline = request.form['deadline']
        new_project = Project(name=name, description=description, deadline=deadline)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_project.html')

# Define the route for assigning a task to a project
@app.route('/assign_task/<int:project_id>', methods=['GET', 'POST'])
def assign_task(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']
        new_task = Task(name=name, status=status, project_id=project_id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('assign_task.html', project=project)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
