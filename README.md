# Task Manager App (Flask + Docker + WSL)

A **CRUD-based Task Manager web app** where users can create, update, delete, and view tasks. This project is fully containerized with **Docker** and designed to run on **WSL 2** for a smooth development experience on Windows.

---

## **Features**

- ✅ Create tasks
- ❌ Delete tasks
- 📋 View all tasks
- 🐳 Dockerized for easy setup
- ⚡ Lightweight and easy to deploy
- 💻 Runs entirely in **WSL 2** with no database

---

## **Project Structure**

```bash
task-manager/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── Dockerfile
├── docker-compose.yml
└── README.md
```
---
## **Prerequisites**

- WSL2(Ubuntu Recommended)
- Docker CLI installed in WSL
- Python 3.11+
- pip package manager

---
## **Getting Started**
## **1. Clone the Repository*
```bash
git clone https://github.com/Dharsan111/task-manager-docker-wsl.git
cd task-manager-docker-wsl
```
## **2. Build and run using Docker Compose*
```bash
docker compose up --build -d
```
- -d runs containers in detached mode.
- use docker ps to check running containers

## **3. Access the App*
Open your browser and go to: 
[http://localhost:5000]



