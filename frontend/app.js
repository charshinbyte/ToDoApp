document.addEventListener('DOMContentLoaded', () => {
    loadTasks();
});

async function loadTasks() {
    try {
        const response = await fetch('http://127.0.0.1:8000/tasks/', {
            method: 'GET',
            headers: {
                'Accept': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const tasks = await response.json();
        const tasksDiv = document.getElementById('tasks');
        tasksDiv.innerHTML = '';

        tasks.forEach(task => {
            if (task.is_deleted) return;

            const taskElement = document.createElement('div');
            taskElement.className = 'task d-flex justify-content-between align-items-center';

            // Apply strikethrough if completed
            if (task.is_completed) {
                taskElement.classList.add('completed');
            }

            // Create checkbox
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.className = 'form-check-input me-2';
            checkbox.checked = task.is_completed;

            checkbox.addEventListener('change', () => {
                if (checkbox.checked && !task.is_completed) {
                    markComplete(task.id);
                }
            });

            // Title
            const title = document.createElement('strong');
            title.innerText = task.title;

                    
            // Delete button
            const deleteBtn = document.createElement('button');
            deleteBtn.innerText = '🗑 Delete';
            deleteBtn.className = 'btn btn-outline-danger btn-sm ms-2';
            deleteBtn.onclick = () => deleteTask(task.id);

            // Left side: checkbox + title
            const leftDiv = document.createElement('div');
            leftDiv.appendChild(checkbox);
            leftDiv.appendChild(title);

            // Right side: delete button
            const rightDiv = document.createElement('div');
            rightDiv.appendChild(deleteBtn);

            taskElement.appendChild(leftDiv);
            taskElement.appendChild(rightDiv);
            tasksDiv.appendChild(taskElement);
        });
    } catch (error) {
        console.error('Error loading tasks:', error);
        document.getElementById('tasks').innerText = 'Failed to load tasks.';
    }
}


async function addTask() {
    const title = document.getElementById('new-task-title').value.trim();
  
    console.log('Adding task:', title); // Debug log
  
    if (!title) {
      alert('Please enter a To Do');
      return;
    }
  
    try {
        const response = await fetch('http://127.0.0.1:8000/tasks/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "title": title
              })
        });
    } catch (error) {
      console.error('Error adding task:', error);
    }

    document.getElementById('new-task-title').value = '';
    loadTasks();
  }



async function deleteTask(taskId) {
  
    try {
        const response = await fetch(`http://127.0.0.1:8000/tasks/delete?task_id=${taskId}`, {
            method: 'DELETE',
            headers: {
                'accept': 'application/json'
            }
        });

      if (!response.ok) {
        throw new Error(`Failed to delete task. Status: ${response.status}`);
      }
  
      console.log(`🗑 Deleted task ${taskId}`);
      loadTasks(); // Refresh the task list
  
    } catch (error) {
      console.error('❌ Error deleting task:', error);
    }
  }


async function purgeTasks() {  
    try {
        const response = await fetch('http://127.0.0.1:8000/tasks/purge', {
            method: 'DELETE',
            headers: {
                'accept': 'application/json',
            }
        });
        if (response.ok) {
            const purgedCount = await response.text(); // await this!
            alert(`Purged ${purgedCount} items `);
            return;
        }
    } catch (error) {
      console.error('Error Purging task:', error);
    }

    loadTasks();
  }


async function markComplete(taskId) {
  
    try {
        const response = await fetch(`http://127.0.0.1:8000/tasks/complete?task_id=${taskId}`, {
            method: 'PUT',
            headers: {
                'accept': 'application/json'
            }
        });

      if (!response.ok) {
        throw new Error(`Failed to update task. Status: ${response.status}`);
      }
  
      console.log(`🗑 Deleted task ${taskId}`);
      loadTasks(); // Refresh the task list
  
    } catch (error) {
      console.error('❌ Error Updating task:', error);
    }
  }
