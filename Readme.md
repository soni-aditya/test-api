# API considerations
- Since only one api endpoint needed to be created, I have decided to create it in a single file rather than using an api template/architecture
- For covering edgecases (like input string being null or empty), We are using RequestBody (which inherits BaseModel). This way, fastapi makes the type checking strict

### The app can be launched using Gunicorn or Uvicorn
eg. use command <br>**uvicorn main:app --host 0.0.0.0 --port 80** <br>to initiate a run