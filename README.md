# genai-pipeline-project
# 🧠 Generative AI Pipeline & Production Deployment

This project implements a complete, end-to-end CI/CD pipeline for deploying a Hugging Face-based Text Generation Model as a production-ready API, leveraging Azure Databricks for model preparation, Docker for containerization, and Jenkins for automated deployment.

## 🚀 Project Overview

The core goal is to demonstrate a robust MLOps (Machine Learning Operations) flow for Generative AI inference.

| Component | Role | Technology |
| :--- | :--- | :--- |
| **Model Prep** | Model training (simulated fine-tuning) and artifact storage. | **Azure Databricks** |
| **API Serving** | Lightweight inference server to handle requests. | **Python/Flask** |
| **Containerization** | Packaging the API and model for consistent deployment. | **Docker** |
| **API Gateway** | Reverse proxy, load balancing, and external exposure. | **Nginx** |
| **CI/CD** | Automated build, test, and deployment upon code push. | **Jenkins/GitHub** |

## 📁 Project Structure

genai-pipeline-project/ ├── databricks/ │ └── notebook.py # Databricks code for training/model prep ├── api/ │ ├── app.py # Flask/Python application for inference │ ├── Dockerfile # Docker image definition for the API │ ├── requirements.txt # Python dependencies │ └── model/ │ └── gpt2/ # Hugging Face Model Artifacts ├── config/ │ └── nginx.conf # Nginx configuration for reverse proxy └── ci-cd/ └── Jenkinsfile # Jenkins pipeline definition └── README.md