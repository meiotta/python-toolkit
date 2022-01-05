import win32com.client

def noteError(stringToSend):

    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    #alternate email if sending from other box 
    #newMail.SentonBehalfOfName = ""
    
    
    newMail.Subject = "Generic Title"
    newMail.To = "myself@mymail.com"
    newMail.HTMLBody = stringToSend
    newMail.Send()
