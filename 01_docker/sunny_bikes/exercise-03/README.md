# Exercise 03

Success once you see this:
```
No name supplied. Could not find any bike rides for this user
```

Try browse to localhost:8080?name=bas

Fill in the Dockerfile to:
- retrieve an image (recommended: `python:3.12-slim`)
- specify `app` as work directory
- copy the files into the `app` folder
- install python packages defined in requirements.txt
- expose port 5000
- entry point should be python
- command should be app.py