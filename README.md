# HelloWorld

Task 1:
============
Hello_World_Application

Documentation:
Python Version: 3.12.0
Editor: Visual Studio Code
Web Framework: Flask
Testing Framework: pytest
Docker Image: Python Official Image (using Python 3.15 as the base image)
Decisions:
Used Flask for simplicity and ease of use.
Implemented basic health check logic for the /health endpoint. You can enhance it based on your application's requirements.
Chose pytest for testing due to its simplicity and popularity.
Dockerized the application to ensure consistency across different environments

Wrote unit tests to ensure the correctness of the endpoints.
Containerized the application using Docker for portability and easy deployment.
Building and Running:
Build the Docker image: docker build -t [imagename]
Run the Docker container: docker run -p 5000:5000 [imagename]
Access the endpoints:
Hello World: http://localhost:5000/
Health: http://localhost:5000/health.


Task 2
===========

Documentation:
Include the following documentation in your repository:

Deployment Instructions:

How to install Minikube.
How to start Minikube.
How to apply Kubernetes manifests.
Access Instructions:

How to obtain the external IP.
How to access the application using the external IP.
High Availability Considerations:

Explanation of the chosen number of replicas in the deployment YAML (replicas: 3).
Any additional high availability strategies implemented.
Automation:
Optionally, you can automate the deployment process using CI/CD tools such as GitHub Actions or Jenkins. Create workflows to build the Docker image, push it to a container registry, and apply Kubernetes manifests to the cluster.

Include the CI/CD configuration files in the .github/workflows directory or the appropriate location for your CI/CD tool.

Provide the Application Manifests Inside the Repository:
Ensure that the deployment.yaml and service.yaml files are committed to your repository under a directory like k8s or deploy.
