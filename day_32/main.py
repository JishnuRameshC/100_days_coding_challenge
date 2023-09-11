import smtplib

my_email = " w05505795@gmail.com"
my_password = "hwkmusdhikuqelpd"

connecting = smtplib.SMTP("smtp.gmail.com", 587)
connecting.starttls()
connecting.login(user=my_email,password=my_password)
connecting.sendmail(from_addr=my_email,to_addrs="jishnurameshc@gmail.com",msg="Subject:hello\n\n\nthis is a message")
connecting.close()