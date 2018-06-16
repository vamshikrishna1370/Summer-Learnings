import smtplib

fromaddr = '****@gmail.com'
toaddrs  = '****@gmail.com'
cc = ['*****@gmail.com','****@iitg.ernet.in']
bcc = ['***@gmail.com']
message_subject = "***..."
message_text = "***."
#msg = 'hello vamshi this is machine generated mail, please try to co-operate with us'
username = '***@gmail.com'
password = '8888888'
server = smtplib.SMTP('smtp.gmail.com:587')

server.ehlo()
server.starttls()
server.login(username,password)
message = "From: %s\r\n" % fromaddr+ "To: %s\r\n" % toaddrs + "CC: %s\r\n" % ",".join(cc) + "Subject: %s\r\n" % message_subject+ "\r\n" + message_text
toaddrs = [toaddrs] + cc + bcc

server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, message)
server.quit()
