# Medical Volunteering Platform

## About Project

This project is a Medical Volunteering Platform developed to help patients connect with volunteer doctors in their city.

A patient can register, and volunteers can also register with their specialization. Patients can then search for available volunteers based on city.

I built this project to practice DevOps tools along with application deployment on AWS.

---

## Technologies Used

- Python Flask
- MySQL
- HTML, CSS, JavaScript
- Docker
- Jenkins
- Terraform
- Ansible
- AWS EC2
- AWS RDS
- AWS ALB
- Nginx
- Git & GitHub

---

## Project Structure

```
backend/
frontend/
terraform/
ansible/
jenkins/
README.md
```

---

## Features

- Patient Registration
- Volunteer Registration
- Search Volunteers by City
- MySQL Database
- Dockerized Application
- Jenkins Pipeline
- Terraform Infrastructure
- Ansible Configuration

---

## AWS Architecture

```
User
   │
ALB
   │
EC2
   │
Docker Container
   │
Flask Application
   │
RDS MySQL
```

---

## Deployment Steps

Clone Repository

```bash
git clone https://github.com/amitkushwaha0102-sys/Medical-Volunteering-Platform.git
```

Deploy Infrastructure

```bash
cd terraform

terraform init

terraform apply
```

Run Ansible

```bash
ansible-playbook playbook.yml
```

Application will be available through the ALB DNS.

---

## API

Register Patient

```
POST /register-patient
```

Register Volunteer

```
POST /register-volunteer
```

Search Volunteer

```
GET /volunteers/<city>
```

---

## Problems I Faced

While building this project I faced several issues.

- Flask circular import issue
- Docker permission denied
- Jenkins Docker socket issue
- RDS connection problem
- Nginx reverse proxy configuration
- Git merge conflicts

I fixed these issues by reading documentation and testing different solutions. This project helped me understand real deployment problems.

---

## Future Improvements

- HTTPS
- Auto Scaling
- Kubernetes
- Prometheus
- Grafana
- SonarQube

---

## Author

Amit Kushwaha

GitHub:
https://github.com/amitkushwaha0102-sys

Learning DevOps and Cloud Engineering.
