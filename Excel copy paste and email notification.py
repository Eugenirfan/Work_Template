#libraries
import os
import time
from datetime import date, timedelta

import win32com.client
import shutil

#preparing dates
date1 = date.today() - timedelta(1)
date2 = date.today() 
file_date = time.strftime("%Y-%m-%d",time.localtime(os.path.getmtime(r'S:\\.xlsx')))
d1 = date1.strftime('%Y-%m-%d')
d2 = date2.strftime('%Y-%m-%d')

#creating from and to location to copy file 
frm= r'A.xlsx'
to = r'd1+'.xlsx'

outlook = win32com.client.Dispatch('outlook.application')
not_copied = outlook.CreateItem(0)
not_copied.To = 'mohamedirfan@mail.com;'
not_copied.Subject = 'Email not Sent'
not_copied.Body = 'Dear \n\n'\
                    '.xlsx is not refreshed.\n\n'\
                    'Thank you\n\n'\
                    'Irfan\n\n'
#when copied
mail = outlook.CreateItem(0)
mail.To = 'irfan@.com;samj@.com;alam@.com;Michaelh@.com'
mail.CC='jinesh'
mail.BCC='jinesh'
mail.Subject = 'T'
mail.Body = 'Hi All\n\n'\
            'Weekly reminder to populate report m\n\n'\
            'S:\Matmgmt\Inventory \n\n'\
            'If need have any doubts/questions, please do not hesitate to contact me\n\n'

# To attach a file to the email (optional):
#attachment  = "Path to the attachment"
#mail.Attachments.Add(attachment)
if file_date==d1 or file_date==d2:
    shutil.copy2(frm,to)
    mail.Send()
else:
    not_copied.Send()
