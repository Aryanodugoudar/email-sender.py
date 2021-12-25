import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Aryan'
email['to'] = 'aryanodugoudar143@gmail.com'
email['subject'] = 'yoo man'

email.set_content(html.substitute({'name': 'dummy'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('mydummyemail0000', 'hihi@1234')
  smtp.send_message(email)
  print('all good')
