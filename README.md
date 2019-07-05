### Intro
The app runs customer search using greater circle distance formula and returns list of users sorted by user_id. The output of the app can be found in output.txt at the top-level folder. The program can also handle streaming input.


### Setup

Below are the steps to run the code. Details are provided for two environment - Docker and Python.

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


### Configuration

Certain variables are configurable in the app

- `SEARCH_RADIUS` - Specifies the radius of search for the customer. Defaults to 100km 
- `SEARCH_CENTER_LAT`, `SEARCH_CENTER_LONG` - Defaults to office address
- `CUSTOMER_RECORDS_FILE_URL` - Defaults to the given file. 

The above can be overriden by passing in the values for them in the environment var.
Check `app/config.py` for more info.

