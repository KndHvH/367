# Variables
IMAGE_NAME := sqls_img
CONTAINER_NAME := sqls
API_PORT := 1433

# Build the Docker image
build:
	@if docker images -q $(IMAGE_NAME) | grep -q .; then \
		echo "Image $(IMAGE_NAME) already exists"; \
		make clean; \
		make build; \
	else \
		echo "Building Image $(IMAGE_NAME)...";\
		docker build --target development -t $(IMAGE_NAME) .;\
	fi

# Run the Docker container
run:
	@if docker ps -a --format '{{.Names}}' | grep -q $(CONTAINER_NAME); then \
		echo "Container $(CONTAINER_NAME) is already running"; \
		make clean; \
	fi
	@if docker images -q $(IMAGE_NAME) | grep -q .; then \
		echo "Running Container $(CONTAINER_NAME)...";\
		docker run -d -p $(API_PORT):$(API_PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME) python run.py; \
	else \
		echo "Image $(IMAGE_NAME) does not exist"; \
		make build; \
		make run; \
	fi

# Stop and remove the Docker container
stop:
	@if docker ps -a --format '{{.Names}}' | grep -q $(CONTAINER_NAME); then \
		echo "Stoping Container $(CONTAINER_NAME)...";\
		docker stop $(CONTAINER_NAME); \
	else \
		echo "Container $(CONTAINER_NAME) does not exist"; \
	fi

remove: stop
	@if docker ps -a --format '{{.Names}}' | grep -q $(CONTAINER_NAME); then \
		echo "Removing Container $(CONTAINER_NAME)...";\
		docker rm $(CONTAINER_NAME); \
	else \
		echo "Container $(CONTAINER_NAME) does not exist"; \
	fi

# Clean up the Docker image
clean: remove
	@if docker images -q $(IMAGE_NAME) | grep -q .; then \
		echo "Cleaning Image $(IMAGE_NAME)...";\
		docker rmi $(IMAGE_NAME); \
	else \
		echo "Image $(IMAGE_NAME) does not exist"; \
	fi


# see the logs
logs:
	@if docker ps -a --format '{{.Names}}' | grep -q $(CONTAINER_NAME); then \
		echo "Showing Logs from Container $(CONTAINER_NAME)..."; \
		docker logs $(CONTAINER_NAME);\
	else \
		echo "Container $(CONTAINER_NAME) does not exist or not running"; \
	fi

# test the api
tests:
	@if docker ps --format '{{.Names}}' | grep -q $(CONTAINER_NAME); then \
		echo "Testing Container $(CONTAINER_NAME)..."; \
		docker exec $(CONTAINER_NAME) pipenv run pytest -vv ./test;\
	else \
		echo "Container $(CONTAINER_NAME) not running"; \
	fi


diagram:
	pip install diagram; \
	sudo apt-get update && sudo apt-get install graphviz; \
	python .docs/diagrams/diagram.py;\

open:
	@if docker ps --format '{{.Names}}' | grep -q $(CONTAINER_NAME); then \
			echo "Opening Container $(CONTAINER_NAME)..."; \
			docker exec -it $(CONTAINER_NAME) /bin/bash;\
	else \
			echo "Container $(CONTAINER_NAME) not running"; \
	fi