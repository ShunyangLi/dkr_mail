from distutils.command.upload import upload
import pytz
from utils.db_handling import query_db
from datetime import datetime, timedelta
from utils.ics_generator import ics_gener, ics_gener_upload
from utils.mail_handling import send_mail


def handle_presenter(ca, na, cd, nd):
    n1 = ""
    n2 = ""

    cas = []
    nas = []
    cas_email = []
    nas_email = []

    # get the user information
    for user in ca:
        data = query_db("select * from contact where name = ?", (user, ))
        if len(data) == 0:
            return "User: {}, can not find the student".format(user)
        cas.append(data[0])
        cas_email.append(data[0]["Email"])
    
    for user in na:
        data = query_db("select * from contact where name = ?", (user, ))
        if len(data) == 0:
            return "User: {}, can not find the student".format(user)
        nas.append(data[0])
        nas_email.append(data[0]["Email"])
    
    sds = cd.split('/')
    eds = nd.split('/')

    currentDate = datetime(int(sds[2]), int(sds[0]), int(sds[1]), 14, 0, 0, tzinfo=pytz.timezone('Australia/Sydney'))
    nextDate = datetime(int(eds[2]), int(eds[0]), int(eds[1]), 16, 0, 0, tzinfo=pytz.timezone('Australia/Sydney'))

    uploadDate = currentDate - timedelta(days=2)


    query_db("delete from current")
    query_db("delete from next")

    # record the current presenters
    for index, user in enumerate(cas):
        if index == len(cas) - 1:
            n1 += "and {} ({})".format(user["Name"], user["Institution"])
        else:
            n1 +="{} ({}), ".format(user["Name"], user["Institution"])
        query_db("insert into current values(?,?,?,?,?)", (user["Name"], user["Email"], user["Institution"], uploadDate.strftime("%m/%d/%Y"), currentDate.strftime("%m/%d/%Y"), ))
    
    for index, user in enumerate(nas):
        if index == len(nas) - 1:
            n2 += "and {} ({})".format(user["Name"], user["Institution"])
        else:
            n2 +="{} ({}), ".format(user["Name"], user["Institution"])
        query_db("insert into next values(?,?,?,?)", (user["Name"], user["Email"], user["Institution"], nextDate.strftime("%m/%d/%Y"), ))
    

    ics_gener(cas_email, cd, cd, "Event")
    ics_gener(nas_email, nd, nd, "FutureEvent")

    # cas_email = cas_email[:1]
    # nas_email = nas_email[:1]

    cas_email.append("yangzhengyi188@gmail.com")

    send_mail(cas_email, "Group Meeting Presentation", "notice", "Event", n1=n1,n2=n2,current_date=currentDate.strftime("%m/%d/%Y"),upload_date=uploadDate.strftime("%m/%d/%Y"), next_date=nextDate.strftime("%m/%d/%Y"))

    send_mail(nas_email, "Group Meeting Presentation", "notice", "FutureEvent", n1=n1,n2=n2,current_date=currentDate.strftime("%m/%d/%Y"),upload_date=uploadDate.strftime("%m/%d/%Y"), next_date=nextDate.strftime("%m/%d/%Y"))
    return None

def handle_upload():
    """
    send and email tell them to upload ppt
    """
    users = query_db("select * from current")
    emails = []
    n1 = ""
    uploadDate = ""

    for index, user in enumerate(users):
        emails.append(user["Email"])
        uploadDate = user["upload"]
        if index == len(users) - 1:
            n1 += "and {} ({})".format(user["Name"], user["Institution"])
        else:
            n1 +="{} ({}), ".format(user["Name"], user["Institution"])
    
    ics_gener_upload(emails, uploadDate, uploadDate, "Upload")

    emails.append("yangzhengyi188@gmail.com")
    send_mail(emails, "Please upload your slides to the WeChat group", "upload", "Upload", n1=n1)





    



    
