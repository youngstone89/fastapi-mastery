# Variables
DOCKER_COMPOSE = docker-compose
PROJECT_NAME = my_project # Optional, replace with your project name
ADD_SENTENCE_SCRIPT = scripts/issue_add_sentence.sh
SYNC_FIND_INTENTION_SCRIPT = scripts/issue_sync_find_intention.sh
ASYNC_FIND_INTENTION_SCRIPT = scripts/issue_async_find_intention.sh
RUN_SCRIPT = scripts/run.sh

# Targets
.PHONY: run build up down logs clean rebuild sync-find-intention async-find-intention add-sentence

run:
	bash ${RUN_SCRIPT}

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


sync-find-intention:
	bash ${SYNC_FIND_INTENTION_SCRIPT}

async-find-intention:
	bash ${ASYNC_FIND_INTENTION_SCRIPT}

add-sentence:
	bash ${ADD_SENTENCE_SCRIPT}

