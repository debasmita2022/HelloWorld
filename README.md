# HelloWorld Project

## Task 1 
### Hello World Application

- Python Version: 3.12.0
- Editor: Visual Studio Code
- Web Framework: Flask
- Testing Framework: pytest
- Docker Image: Python Official Image (using Python 3.15 as the base image)

#### Decisions
- Used Flask for simplicity and ease of use.
- Implemented basic health check logic for the /health endpoint. 
- You can enhance it based on your application's requirements.
- Chose pytest for testing due to its simplicity and popularity.
- Dockerized the application to ensure consistency across different environments.
- Wrote unit tests to ensure the correctness of the endpoints.
- Containerized the application using Docker for portability and easy deployment.

#### Building and Running:
- Build the Docker image: docker build -t [imagename]
- Run the Docker container: docker run -p 5000:5000 [imagename]
- Access the endpoints:
- Hello World: http://localhost:5000/
- Health: http://localhost:5000/health.

## Task 2

- Have been attested under main branch with the name Demonstrate_Task2

## Task 3

#### Deployment Instructions:

- install Minikube :: curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \&& chmod +x minikube
- start Minikube :: minikube start
-  apply Kubernetes manifests :: kubectl apply -f (your yaml file)
  
 #### Access Instructions:

- obtain the external IP.
- High Availability Considerations:

- Explanation of the chosen number of replicas in the deployment YAML (replicas: 3).
- Availability strategies implemented.
#### Automation:
- Optionally, you can automate the deployment process using CI/CD tools such as GitHub Actions or Jenkins.
- Create workflows to build the Docker image, push it to a container registry, and apply Kubernetes manifests to the cluster.

- Include the CI/CD configuration files in the .github/workflows directory or the appropriate location for your CI/CD tool.

- Application Manifests Inside the Repository has been provided:
- deployment.yaml and service.yaml files are committed to my  repository under main.
