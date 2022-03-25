## Requirements
This is an open-source python project so in theory this application can be executed on any computer that python is installed. Python3, venv, and pip are required for the installation of the application. 

## Installation
1. Create Virtual Environment
    Create the virtual environment using python;
    ```
    python -m venv env
    ```
    When the default python version on the computer is not python 3. X use the line below for creating the virtual environment;
    ```
    python3 -m venv env
    ```
2. Activate Virtual Environment
    If you successfully created the virtual environment you should see a venv folder in the project directory.
    
    Get into the virtual environment   ;
    ```
    source venv/bin/activate
    ```

3. Install the Requierment
    Using pip install all the required libraries;
    ```
    pip install -r requirements.txt 
    ```

## Usage
1. Find the course capacity page of the course you want to get notified from bannerweb.
2. Run the main.py with the course capacity URL as the first argument.
3. The second parameter is optional and it specifies the number of iterations the default is 10 000.
```
python main.py "http://suis.sabanciuniv.edu/prod/bwckschd.p_disp_detail_sched?term_in=202101&crn_in=10099"
```
 
## Versions
1.0.0 Released on March 26, 2022

## License
Copyright 2022 by Yigit Kilicaslan.
All rights reserved. This file is part of the Course Capacity Notifier, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package. This is an educational project in order to develop the computer science skills use it on your own responsibility.