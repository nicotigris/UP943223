from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    deadline = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='project', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

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

if __name__ == '__main__':
    app.run(debug=True)