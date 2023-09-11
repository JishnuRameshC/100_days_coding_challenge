# import smtplib

# my_email = "w05505795@gmail.com"
# my_password = "W0W_f4u9000"
# # connect = smtplib.SMTP("smtp.gmail.com")
# # connect.starttls()
# # connect.login(user=my_email,password=my_password)
# # connect.sendmail(from_addr=my_email,
# #                  to_addrs="jishnurameshc@gmail.com",
# #                  msg="hello")
import smtplib
from email.mime.text import MIMEText

my_email = "w05505795@gmail.com"
my_app_password = "W0W_f4u9000"

# Create a message object
message = MIMEText("Hello, this is a test email.")

# Set the sender and recipient email addresses
message["From"] = my_email
message["To"] = "jishnurameshc@gmail.com"
message["Subject"] = "Test Email Subject"

try:
    # Connect to Gmail's SMTP server
    connect = smtplib.SMTP("smtp.gmail.com")
    
    # Start TLS encryption
    connect.starttls()
    
    # Login with your Gmail account and app password
    connect.login(user=my_email, password=my_app_password)
    
    # Send the email
    connect.sendmail(from_addr=my_email, to_addrs="jishnurameshc@gmail.com", msg=message.as_string())
    
    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the SMTP connection
    connect.quit()
