import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr=' akashbh1235@gmail.com'
to_addr=['vtuv1165@gmail.com','hisbdcuegf.@gmail.com']
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='just to check'

body='hello world'

msg.attach(MIMEText(body,'plain'))

email='akashbh1235@gmail.com '
password='egtyhqceycznjrot'

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()