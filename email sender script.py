import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import time
import pyfiglet
from termcolor import colored
from getpass import getpass

# Display ASCII art banner
ascii_banner = pyfiglet.figlet_format("FIND STAGE")
print(colored(ascii_banner, "cyan"))

# Welcome message
welcome_message = "Welcome to the Automated Email Sender Script!"
print(colored(welcome_message, "green"))

# Email credentials
sender_email = input(colored("Enter your email: ", "yellow")).strip()
password = getpass(colored("Enter your email password (App Password if 2FA is enabled): ", "yellow")).strip()

# Get the subject and body from an external text file
letter_path = input(colored("Drag and drop your Letter.txt file here: ", "yellow")).strip().strip('"')

try:
    with open(letter_path, "r", encoding="utf-8") as letter_file:
        subject = letter_file.readline().strip()  # Use the first line as the subject
        body = letter_file.read().strip()  # Use the remaining lines as the body
    print(colored("Letter loaded successfully!", "green"))
except FileNotFoundError:
    print(colored("Error: Letter file not found.", "red"))
    exit()

# Get the email list file path
email_list_path = input(colored("Drag and drop your email list file here: ", "yellow")).strip().strip('"')

# Read recipient emails from the provided file
try:
    with open(email_list_path, "r") as file:
        recipient_emails = [line.strip() for line in file if line.strip()]
    print(colored(f"Loaded {len(recipient_emails)} recipient emails!", "green"))
except FileNotFoundError:
    print(colored("Error: Email list file not found.", "red"))
    exit()

# Prompt for file paths to attach
cv_path = input(colored("Drag and drop your CV file here: ", "yellow")).strip().strip('"')
demand_path = input(colored("Drag and drop your Demand file here: ", "yellow")).strip().strip('"')

# List of files to attach
files_to_attach = [cv_path, demand_path]

# Notify user that the process is starting
print(colored("Starting to send emails...", "blue"))

# Loop through each recipient and send the email
for receiver_email in recipient_emails:
    # Create email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Attach each file
    for filepath in files_to_attach:
        filename = os.path.basename(filepath)  # Extract the file name
        try:
            with open(filepath, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={filename}",
            )
            message.attach(part)
        except FileNotFoundError:
            print(colored(f"Error: File {filename} not found. Skipping...", "red"))

    # Send email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print(colored(f"Email sent successfully to {receiver_email}!", "green"))
    except Exception as e:
        print(colored(f"Failed to send email to {receiver_email}: {e}", "red"))

    # Delay for 15 seconds before sending the next email
    print(colored("Waiting for 15 seconds before sending the next email...", "blue"))
    time.sleep(15)

# Completion message
print(colored("All emails have been sent successfully!", "green"))
