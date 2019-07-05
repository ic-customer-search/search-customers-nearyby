Intercom Interview Question Repo

Below are the steps to run the code. Details are provided for two environment - Docker and Python
All commands should be run from the root folder of the project.

#### Docker Enviornment
```bash
docker build . -t customer-search

docker run customer-search
docker run customer-search test

# For DEBUG mode
docker run -e LOG_LEVEL=DEBUG customer-search
docker run -e LOG_LEVEL=DEBUG customer-search test
```

#### Python3 Environment
```bash
python3 -m venv .envs/ic-customer-search
source .envs/ic-customer-search/bin/activate
pip install -r requirements.txt

python app/main.py
python -m unittest discover -s app

# For Debug Mode,
LOG_LEVEL=DEBUG python app/main.py
LOG_LEVEL=DEBUG python -m unittest discover -s app
```

