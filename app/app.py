from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task storage
tasks = []
task_id = 1

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global task_id
    title = request.form.get('title')
    description = request.form.get('description')
    if title:
        tasks.append({'id': task_id, 'title': title, 'description': description})
        task_id += 1
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_task(id):
    for task in tasks:
        if task['id'] == id:
            task['title'] = request.form.get('title')
            task['description'] = request.form.get('description')
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

