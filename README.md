# Lemonade Word Counter
Word counter endpoint that collects words and creates word appearence statistics and return statistics for specific words. 

## Initialization:
*make sure you have python and pip installed on your machine*
1. Clone the project to your local machine.
2. Open the command line and switch to the root directory of the project you just cloned.
3. Run  ```python src/InstallPackages.py```. This will install all needed packages in order to run the server
4. Run  ```python -m src.Server.Server``` to initiate the server
5. The server will start its run, config for localrun and port 5555

## Restart statistics collection
1. Stop the opperation of the server
2. Open the command line and switch to the root directory of the project.
3. Run ``` python src/CleanWordStatistics.py ```
4. Run  ```python -m src.Server.Server``` to initiate the server 

## Endpoint
### Word Counter

```POST /word_counter/```

**Input**:  
1.  **Simple Text String**: "Headers[Content-Type] : application/json" - Containing JSON object in the body formated as : ```{"type":"text", "value":"<*your_text*>"}```

    Body example:
    
    *{"type":"text", "value":"Hey! My name is (what?), my name is (who?), my name is Slim Shady"}*
    

2.  **Text From File**: "Headers[Content-Type] : application/json" - Containing JSON object in the body formated as ```{"type":"file", "value":"<*your_file_path*>"}```

    Body example:
    
    *{"type":"file", "value":"C:/Users/galdreval/intersting_text.txt"}*

3.  **Text From URL**: "Headers[Content-Type] : application/json" - Containing JSON object in the body formated as ```{"type":"url", "value":"<*your_url*>"}```

    Body example:
    
    *{"type":"url", "value":"https://www.google.com/intersting_search"}*

**Output**
 will be returned in application/json format with the server message. Success status code will be 202 (Accepted)

### Word Statistics

```GET /word_statistics/```

**Input**:  

1.  **Word as JSON**: Containing url query parameter with "word" as a key
    URL example:
    
    *http://localhost:5555/word_statistics/?word=lemonade*

**Output**
 will return in application/json formated as  ```{
    "Counter": 32,
    "Word": "lemonade"
}```
. Success status code will be 200 (OK)

## Additional Information
1. "InstallPackages.py" script contains ```pip install <package>``` command for "pathlib", "configparser", "flask", "argparse" and "pytest". 
2. I have added tests for all relevant classes:

      2.1 Open the command line and switch to the root directory of the project
   
      2.2 Run ```py.test -vv```



