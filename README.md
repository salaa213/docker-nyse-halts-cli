# Docker-NYSE-Halts

This project provides a simple Dockerized Python application that fetches trade halt data from the NYSE API and prints it as a table in the terminal. The application continuously fetches and displays the latest data every 10 seconds.

## Features
- Fetches live data from the NYSE API.
- Displays data in a readable tabular format.
- Runs in an isolated Docker container.

---

## Prerequisites
- Docker installed on your system.
- (Optional) Git for cloning the repository.

---


## Setup Instructions

### 1. Clone the Repository

Clone the project repository from GitHub:

```
git clone https://github.com/tsalameh512/docker-nyse-halts.git
cd docker-nyse-halts
```

----------

### 2. Build the Docker Image

Use the provided `Dockerfile` to build the image locally:

```
docker build -t nyse-halts:latest .
```

----------

### 3. Run the Application

Run the Docker container:

```
docker run -it --rm nyse-halts:latest
```

The application will:

-   Fetch the latest trade halt data from the NYSE API as a CSV.
    
-   Display the data in a readable table format.
    
-   Refresh every 10 seconds to show updated information.

### Debugging with Interactive Shell

If you need to debug or test the environment inside the Docker container, you can run the container with an interactive shell:

```bash
docker run -it --rm nyse-halts:latest bash
