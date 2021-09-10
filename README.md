# LemonadeWordCounter
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
1.  **Simple Text String**: "Headers[Content-Type] : text/plain" - Containing body of string with simple text input:

    Body example:
    
    *Hey! My name is (what?), my name is (who?), my name is Slim Shady*

2.  **Text From File**: "Headers[Content-Type] : application/json" - Containing JSON object in the body formated as ```{"file":"<*your_full_file_path*>"}```

    Body example:
    
    *{"file":"C:/Hey/How/Are/You/fine.txt"}*

3.  **Text From URL**: "Headers[Content-Type] : application/json" - Containing JSON object in the body formated as ```{"url":"<*your_full_URL*>"}```

    Body example:
    
    *{"url":"https://www.lemonade.com/"}*

**Output**
 will return in application/json format with empty string. Success status code will be 202 (Accepted)

### Word Statistics

```GET /word_statistics/```

**Input**:  

1.  **Word as JSON**: "Headers[Content-Type] : application/json" && "Headers[Accept] : application/json"  - Containing JSON object in the body formated as ```{"word":"<*your_desired_word*>"}```

    Body example:
    
    *{"word":"lemonade"}*

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



