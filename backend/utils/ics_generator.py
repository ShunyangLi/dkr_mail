import os
import pytz
from pathlib import Path
from datetime import datetime
from icalendar import Calendar, Event, vCalAddress, vText

HOMEPATH = os.getcwd()

def ics_gener(attendees, start_date, end_date, filename):
    """
    date format: mm/dd/yyyy
    """
    cal = Calendar()
    for attendee in attendees:
        cal.add('attendee', 'MAILTO:{}'.format(attendee))

    event = Event()
    event.add('summary', 'Group Meeting Presentation')

    sds = start_date.split('/')
    eds = end_date.split('/')

    event.add('dtstart', datetime(int(sds[2]), int(sds[0]), int(sds[1]), 14, 0, 0, tzinfo=pytz.timezone('Australia/Sydney')))
    event.add('dtend', datetime(int(eds[2]), int(eds[0]), int(eds[1]), 16, 0, 0, tzinfo=pytz.timezone('Australia/Sydney')))
    event.add('dtstamp', datetime(int(sds[2]), int(sds[0]), int(sds[1]), 14, 0, 0, tzinfo=pytz.timezone('Australia/Sydney')))

    organizer = vCalAddress('MAILTO:yangzhengyi188@gmail.com')
    organizer.params['cn'] = vText('DKR')
    event['organizer'] = organizer
    event['location'] = vText('Voov Online Meetings')

    cal.add_component(event)

    directory = os.path.join(HOMEPATH + '/static/{}.ics'.format(filename))
    f = open(directory, 'wb')
    f.write(cal.to_ical())
    f.close()


def ics_gener_upload(attendees, start_date, end_date, filename):
    """
    date format: mm/dd/yyyy
    """
    cal = Calendar()
    for attendee in attendees:
        cal.add('attendee', 'MAILTO:{}'.format(attendee))

    event = Event()
    event.add('summary', 'Group Meeting Presentation')

    sds = start_date.split('/')
    eds = end_date.split('/')

    event.add('dtstart', datetime(int(sds[2]), int(sds[0]), int(sds[1]), 18, 0, 0, tzinfo=pytz.timezone('Australia/Sydney')))
    event.add('dtend', datetime(int(eds[2]), int(eds[0]), int(eds[1]), 20, 0, 0, tzinfo=pytz.timezone('Australia/Sydney')))
    event.add('dtstamp', datetime(int(sds[2]), int(sds[0]), int(sds[1]), 18, 0, 0, tzinfo=pytz.timezone('Australia/Sydney')))

    organizer = vCalAddress('MAILTO:yangzhengyi188@gmail.com')
    organizer.params['cn'] = vText('DKR')
    event['organizer'] = organizer
    event['location'] = vText('Voov Online Meetings')

    cal.add_component(event)

    directory = os.path.join(HOMEPATH + '/static/{}.ics'.format(filename))
    f = open(directory, 'wb')
    f.write(cal.to_ical())
    f.close()