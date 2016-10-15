# classnotifier

webCheck_v2.py:
This python script will notify you if and when a class of is open.

It will take two inputs, a url and a crn and at any point if the user input 'exit', the program will quit. For every url and a crn, it will allocate a thread to continually checking until the class is open. When the class is open, the script will send the user an email saying that the class is open. The python script is smart enough to check if the url is a valid url and it will keep asking for one and it also checks if the CRN is a 5 digit number and is a number. It is only when it allocates a thread then it will check if the CRN exists for that particular class.

This script is designed for a dedicated server because you need to leave the script running until all the input classes are open also the more classes that you put in the more resources it will need. However, if you only have one or two classes, then you can use it on your laptop.


=========================================
Test:
url: https://courses.illinois.edu/schedule/2016/fall/CS/173  
CRN: 12345

Output: CRN: 12345 does not exist for this class

url: https://courses.illinois.edu/schedule/2016/fall/CS/173  
CRN: 51496

Output:
An email will be send to toaddrs email account with this message: Please go and register now for CRN: 51496


registarServ.py:
This script is made to automate the steps that a user would take to register for his class. I only manage to automate the process up until the hold because the college won't lift the hold on my account. Also, do note that it will not work right out of the box, you will need to input the user ID and password into the script. A user can use base64.b64encode for the ID and password so people cannot see it when they are looking at your computer screen. It is made it so that each block of code is a "step". A step means it automates a users click or an action to which will leads to another webpage. There are comments on top of each block that tells you what that block does. 

Future work:
The idea would be to replace the email notifying block the webCheck_v2 with the registarServ. So that when it detects a class that is open, it will automatically register the class for the user. I have used python as a language to code this is because we can just incorporate Django very easily.
