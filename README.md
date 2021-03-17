# API_FLASK_Example

## Initial environment for development ## 
- Virtual environment criation, using Python 3
```
$ python3 -m venv venv
```
- Virtual environment activation
```
$ source venv/bin/activate
```
- Exiting the virtual environment, run the function provided by venv/bin/deactivate
```
$ deactivate
```

## Development and execution environment ## 
- Activate virtual environment 
```
$ source venv/bin/activate
```
- Install the libraries from newSINDA-requirements.txt
```
$ pip install -r requirements.txt 
```
- Running the application with Flask
```
$ cd flask_example/
$ export FLASK_APP=app.py"
$ export FLASK_ENV=development"
```
