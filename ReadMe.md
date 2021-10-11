# Running the project locally

1. Install Docker/Compose
2. `docker-compose -f local.yml up`

You should have a webserver running on [localhost:8000](localhost:8000).

# Running tests

`docker-compose -f local.yml exec django pytest`
