
#only dependency IIRC
import win32com.client

#function but probably would be fine without
#this does html mail so you can also do cool things if you can write html on the fly with other functions
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
