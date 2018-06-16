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


# server.ehlo()
# server.starttls()

# server.login(username,password)
# server.sendmail(fromaddr, toaddrs, msg)
# server.quit()


# toaddr = 'buffy@sunnydale.k12.ca.us'
# cc = ['alexander@sunydale.k12.ca.us','willow@sunnydale.k12.ca.us']
# bcc = ['chairman@slayerscouncil.uk']
# fromaddr = 'giles@sunnydale.k12.ca.us'
# message_subject = "disturbance in sector 7"
# message_text = "Three are dead in an attack in the sewers below sector 7."
# message = "From: %s\r\n" % fromaddr
#         + "To: %s\r\n" % toaddr
#         + "CC: %s\r\n" % ",".join(cc)
#         + "Subject: %s\r\n" % message_subject
#         + "\r\n" 
#         + message_text
# toaddrs = [toaddr] + cc + bcc

# server.set_debuglevel(1)
# server.sendmail(fromaddr, toaddrs, message)
# server.quit()