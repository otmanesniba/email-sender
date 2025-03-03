# Automated Email Sender Script
This Python script automates the process of sending personalized emails with attachments to multiple recipients. It uses the smtplib library to send emails via Gmail and includes features like loading email content from a text file, attaching files (e.g., CV and demand letter), and sending emails with a delay between each send.

# Features
1. ASCII Art Banner: Displays a stylish banner using pyfiglet.

2. Dynamic Email Content: Loads the email subject and body from a Letter.txt file.

3. Multiple Recipients: Reads recipient email addresses from a text file.

4. File Attachments: Allows attaching files (e.g., CV and demand letter).

5. Delay Between Emails: Adds a 15-second delay between sending emails to avoid being flagged as spam.

6. Error Handling: Includes error handling for missing files or failed email sends.

# Prerequisites
Before running the script, ensure you have the following:

1. Python 3.x installed on your system.
2. A Gmail account with App Password enabled (if 2FA is enabled on your account).
3. Required Python libraries installed. You can install them using:

```bash
 pip install pyfiglet termcolor


