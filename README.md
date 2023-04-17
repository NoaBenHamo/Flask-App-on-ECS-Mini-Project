#### (This README file is still in the making...)
# Dockerizing and deploying a simple flask application on ECS with load balancing

### Prerequisites:
- An AWS account
- Docker installed
- AWS CLI installed

### Step 1: Clone the repository
Begin by cloning this repository to your local machine.
```
git clone https://github.com/NoaBenHamo/Flask-App-on-ECS-Mini-Project.git
```
### Step 2: Build the Docker image
Change directory to your repo and build the Docker image with the following command:
```
docker build -t <IMAGE_NAME> .
```
### Step 3: Push the Docker image to ECR
Before pushing the Docker image, you need to log in to your ECR registry using the AWS CLI:
```
aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com
```
Then, tag your Docker image and push it to ECR:
```
docker tag <IMAGE_NAME>:latest <ECR_REPO_URI>:latest
docker push <ECR_REPO_URI>:latest
```

### Step 4: Create an ECS cluster
