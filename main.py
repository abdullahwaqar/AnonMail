#!/bin/python2.7

import requests

def mail():
    mail_to = raw_input('To: ')
    mail_subject = raw_input('Subject: ')
    mail_message = raw_input('Message: ')

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    session = requests.Session()
    email_req = session.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
        'Host': 'anonymouse.org',
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://anonymouse.org/anonemail.html',
            'Connection': 'close',
            'Upgrade-Insecure-Requests':'1',
            'Content-Type':'application/x-www-form-urlencoded'
    }, data = {
        'to': mail_to,
        'subject': mail_subject,
        'text': mail_message
    })

    if 'The e-mail has been sent' in email_req.text:
        print "[+] Email Sent."

if __name__ == '__main__':
    mail()