from email.mime.text import MIMEText
import smtplib

while True:
	from_email = "real.microsoftinc@gmail.com"
	from_password = "wesam098"
	to_email="wesamsaleh30@icloud.com"
	
	subject = "Warning: Your computer has been infected"
	message = "This is a warning. Your laptop is infected with a virus. Please call 732-379-1732 for help. Goodbye!" 
	
	msg=MIMEText(message)
	msg['Subject']=subject
	msg['To']=to_email
	msg['From'] = from_email
	
	gmail= smtplib.SMTP('smtp.gmail.com', 587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email, from_password)
	gmail.send_message(msg)
	
	
	