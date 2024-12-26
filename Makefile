# Variables
DOCKER_COMPOSE = docker-compose
PROJECT_NAME = my_project # Optional, replace with your project name
SHELL_SCRIPT = scripts/issue_find_intention.sh

# Targets
.PHONY: build up down logs clean rebuild call-api

# Run docker-compose up with build
up:
	$(DOCKER_COMPOSE) up --build

# Bring the containers down
down:
	$(DOCKER_COMPOSE) down

# View logs
logs:
	$(DOCKER_COMPOSE) logs -f

# Clean up images, containers, and volumes
clean:
	$(DOCKER_COMPOSE) down --rmi all --volumes --remove-orphans

# Build images only
build:
	$(DOCKER_COMPOSE) build

# Force a rebuild and restart
rebuild: clean up


call-api:
	bash ${SHELL_SCRIPT}

