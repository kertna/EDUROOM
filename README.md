# EDUROOM
Eduroom is an online assignment submission tool.

## FEATURES
- **Create assignments with deadlines**
  - Assignments with deadlines are created by teachers with unique code. This code is to students circulated to access the assignment. 
- **Submit assignments**
  - Students can search for the assignment with the code and submit the assignment.
  - They can leave comment for teachers if they have any.
  - Students are allowed to submit assignments after deadline
- **Grade assignments**
  - Teachers who created assignment can grade the submissions after deadline.
  - Teachers can also change the grade if needed.
- **Check for plagiarism**
  - Teachers can check for plagiarism in the assignment submisions by clicking the button provided in the submissions page.
  - Files that are similar are marked red.
- **Discussion window**
  - Students and teacher can discuss the assignment in the discussion chat window.
- **Find late submissions**
  - Students who submitted the assignment after deadline are captured and listed.
- **Check grades**
  - Students can check their grades after teachers evaluated the assignment.
- **Authentication**
  - Registraction, Login, Logout, Forgot password are implemented.

## HOW TO RUN
- Create a virtual environment using command ```python -m venv eduroomenv```
- For windows ```eduroomenv\Scripts\activate.bat``` 
- For Unix\ Mac ```source eduroomenv/bin/activate```
- Clone the repository https://github.com/kertna/EDUROOM in the virtual environment
- run ```pip install -r requirements.txt```
- run ``` python manage.py runserver``` to start

   
