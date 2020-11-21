import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("sa3294@srmist.edu.in", "Bhopal@1999")
server.sendmail("sa3294@srmist.edu.in",
	             "mdsamraan@gmail.com",
 	              "hello,, what's up?")


server.quit()