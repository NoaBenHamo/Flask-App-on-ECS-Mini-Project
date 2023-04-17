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
### Step 3: Create an ECR
Amazon Elastic Container Registry (ECR) is a fully-managed Docker container registry.
We will use ECR to store the Docker images that we will use in our ECS cluster.

### Step 4: Push the Docker image to ECR
Before pushing the Docker image, you need to log in to your ECR registry using the AWS CLI:
```
aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com
```
Then, tag your Docker image and push it to ECR:
```
docker tag <IMAGE_NAME>:latest <ECR_REPO_URI>:latest
docker push <ECR_REPO_URI>:latest
```

### Step 5: Create an ECS cluster
Create an ECS cluster using the AWS console. Be sure to select the appropriate networking settings, such as a VPC with public and private subnets.

### Step 6: Create an ECS task definition
Create an ECS task definition that describes how to run your Docker image. Be sure to include the appropriate environment variables, port mappings, and IAM roles. 
**The task definition would look something like this:**
```JSON
{
    "taskDefinitionArn": "arn:aws:ecs:eu-west-1:<AWS_ACCOUNT_ID>:task-definition/flask-app:1",
    "containerDefinitions": [
        {
            "name": "flask-app-definition",
            "image": "<AWS_ACCOUNT_ID>.dkr.ecr.eu-west-1.amazonaws.com/my-ecr:latest",
            "cpu": 0,
            "portMappings": [
                {
                    "name": "flask-5000-tcp",
                    "containerPort": 5000,
                    "hostPort": 0,
                    "protocol": "tcp",
                    "appProtocol": "http"
                }
            ],
            "essential": true,
            "environment": [],
            "environmentFiles": [],
            "mountPoints": [],
            "volumesFrom": []
        }
    ],
    "family": "flask-app",
    "taskRoleArn": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/ECS-task-execution",
    "executionRoleArn": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/ecsTaskExecutionRole",
    "revision": 1,
    "volumes": [],
    "status": "ACTIVE",
    "requiresAttributes": [
        {
            "name": "com.amazonaws.ecs.capability.ecr-auth"
        },
        {
            "name": "com.amazonaws.ecs.capability.task-iam-role"
        },
        {
            "name": "ecs.capability.execution-role-ecr-pull"
        }
    ],
    "placementConstraints": [],
    "compatibilities": [
        "EC2"
    ],
    "requiresCompatibilities": [
        "EC2"
    ],
    "cpu": "2048",
    "memory": "3072",
    "runtimePlatform": {
        "cpuArchitecture": "X86_64",
        "operatingSystemFamily": "LINUX"
    },
    "registeredAt": "2023-04-17T13:34:01.509Z",
    "registeredBy": "arn:aws:iam::<AWS_ACCOUNT_ID>:user/<AWS_USER>",
    "tags": []
}
```
### Step 7: Create an ECS service
Create an ECS service that uses the task definition you created in the previous step. Be sure to select the appropriate cluster, load balancer, and desired number of tasks.

### Step 8: Verify the deployment
After a few minutes, you should be able to access your Flask application through the load balancer URL.
