# Say Hi -- CI/CD with Docker and GitHub Actions (Assignment 4)

Automated deployment pipeline: push to `prod` branch triggers tests, Docker build,
push to DockerHub, and deploy to the class server.

## How it works

- Push to `main`: runs pylint, mypy, and pytest
- Merge `main` into `prod`: same checks, plus builds Docker image, pushes to DockerHub,
  SSHs into the server and runs the new image
- The container runs `app.py`, which writes a timestamped file to `/opt/assignment_outputs`
  on the host (mapped to `/app/data` inside the container)

## GitHub repo setup

You need to configure these under the repo Settings > Secrets and variables > Actions:

**Secrets:**

| Name              | Value                                           |
|-------------------|-------------------------------------------------|
| SERVER_HOST       | 95.216.216.139                                  |
| SERVER_USER       | alextsourmas                                    |
| SERVER_SSH_KEY    | Private key (ed25519) for SSH to the server     |
| DOCKER_PASSWORD   | DockerHub access token                          |

**Variables:**

| Name             | Value                       |
|------------------|-----------------------------|
| DOCKER_USERNAME  | your DockerHub username     |

## SSH key for GitHub Actions

Generate a dedicated key pair on the server (do NOT reuse your existing keys):

```
ssh-keygen -t ed25519 -C "github-actions" -f ~/.ssh/gh_actions_key
cat ~/.ssh/gh_actions_key.pub >> ~/.ssh/authorized_keys
```

Copy the private key (`~/.ssh/gh_actions_key`) into the `SERVER_SSH_KEY` secret.

## Running locally

```
pip install -r requirements.txt
python app.py
```

## Docker (local test)

```
docker build -t mleng_sayhi .
docker run -v /tmp/test_output:/app/data mleng_sayhi
```
