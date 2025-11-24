# Disease Prediction System

## Project Title
*Python Disease Prediction System*

## Overview of the Project
This is a basic command-line program written in Python that lets a user check for possible diseases based on symptoms they select.  
The project also shows how data, logic, and user interaction can be separated using *three different Python modules*.

---

## Features

- *Symptom List:* Shows all available symptoms to the user.  
- *Flexible Input:* User can enter multiple symptoms by separating them with commas.  
- *Prediction:* The program compares the selected symptoms with the disease dictionary and predicts possible diseases.  
- *Result Display:* Shows predicted diseases along with their descriptions.  
- *Safety Warning:* Displays a note reminding the user that this tool is only for educational purposes, not medical advice.

---

## Technologies / Tools Used

- *Language:* Python 3  
- *Modules:* The project uses three separate Python files:  
  - mod1.py – Stores disease and symptom data  
  - mod2.py – Handles prediction logic and processing  
  - main.py – Runs the interactive program  

---

## Steps to Install & Run the Project

1. *Requirement:* Make sure Python 3 is installed on your system.  
2. *Setup:* Place mod1.py, mod2.py, and main.py in the same folder.  
3. *Run Program:*  
   - Open terminal/command prompt  
   - Navigate to the project folder  
   - Run the program using:  
     
     python main.py
     

---

## Instructions for Testing

- *Test Case 1 (Success):*  
  Enter symptoms linked to one known disease (e.g., high fever + body ache).  
  Expected result: *Flu* appears.

- *Test Case 2 (Multiple Matches):*  
  Enter symptoms like cough + mild fever.  
  Expected result: *Common Cold* and *Bronchitis* appear.

- *Test Case 3 (No Match):*  
  Enter a symptom or combination not in the database.  
  Expected result: *"NO DISEASE MATCHED"* message.

- *Test Case 4 (Exit):*  
  Type quit to exit the program loop.

---

## Screenshots
<img width="323" height="400" alt="1st" src="https://github.com/user-attachments/assets/4468a5f9-ed99-402d-8f73-4f8adb78d692" />
<img width="337" height="245" alt="2nd" src="https://github.com/user-attachments/assets/29d41c78-b6a5-4a36-a9b6-5c40f71bc4f1" />
<img width="326" height="58" alt="3rd input disease" src="https://github.com/user-attachments/assets/afbe4bde-20e9-455b-aef9-327490e4b354" />
<img width="355" height="213" alt="4th predicted results" src="https://github.com/user-attachments/assets/706f9759-f53a-404a-847f-00aa3ffc9f27" />




