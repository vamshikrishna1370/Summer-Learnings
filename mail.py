import smtplib

fromaddr = 'vamshianireddy1370@gmail.com'
toaddrs  = 'vamshianireddy1370@gmail.com'
cc = ['avkr.rkva2005@gmail.com','ani.reddy@iitg.ernet.in']
bcc = ['sridevianireddy@gmail.com']
message_subject = "Vamshi Learning to send automatic mails..."
message_text = "hello vamshi this is machine generated mail, please try to co-operate with us."
#msg = 'hello vamshi this is machine generated mail, please try to co-operate with us'
username = 'vamshianireddy1370@gmail.com'
password = '1370VamshI'
server = smtplib.SMTP('smtp.gmail.com:587')

server.ehlo()
server.starttls()
server.login(username,password)
message = "From: %s\r\n" % fromaddr+ "To: %s\r\n" % toaddrs + "CC: %s\r\n" % ",".join(cc) + "Subject: %s\r\n" % message_subject+ "\r\n" + message_text
toaddrs = [toaddrs] + cc + bcc

server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, message)
server.quit()
