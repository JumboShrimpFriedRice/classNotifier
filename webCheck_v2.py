import smtplib
import sys
import thread
import time

import requests
import validators  # pip install validators


def emailNotify(crn):
    """
    This function will send an email to the user.

    fromaddr is the ADMIN email address.
    toaddrs is the user's email address.
    :return: none
    """
    fromaddr = ''
    toaddrs = ''
    msg = "\r\n".join([
        "From: ",
        "To: ",
        "Subject: Your course is OPEN!",
        "",
        "Please go and register now for CRN: " + str(crn)
    ])

    # if you changed the Admin email address be sure to change the setting as well.
    username = ''
    password = ''
    server = smtplib.SMTP('smtp.gmail.com:587')
    # =======ADMIN email setting ends here=====================================
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


def check(url, crn):
    """
    Be sure to check if the proxy servers are up.
    Add more proxy servers if you want to make more request or make your traffic look more randomized
    :param url: URL of the class
    :param crn: CRN of the class section
    :return:
    """
    proxyDict = {
        'http': '107.151.136.219:80'
    }

    proxyDict2 = {
        'http': '91.121.121.199:4444'
    }

    count = 0
    crnCheck = False
    while True:
        # url = raw_input()
        # alternate between the two different proxy servers. Add more if desired.
        # Add more if you wish to decrease the time before making the request to the server agian.
        if count % 2 == 0:
            r = requests.get(url, stream=True, proxies=proxyDict)
            r2 = requests.get(url, stream=True, proxies=proxyDict)
        else:
            r = requests.get(url, stream=True, proxies=proxyDict2)
            r2 = requests.get(url, stream=True, proxies=proxyDict2)

        wordList = ['alt=\\"Open\\"\/>","crn":"' + str(crn) + '"']
        wordList_Close = ['alt=\\"Closed\\"\/>","crn":"' + str(crn) + '"']

        for line in r2.iter_lines():
            if any(word in line for word in wordList_Close):
                crnCheck = True

        for line in r.iter_lines():
            if any(word in line for word in wordList):
                # print line
                # if found, will print "open" and will exit
                # print "open"
                emailNotify(crn)
                thread.exit()

        if not crnCheck:
            print "CRN: " + str(crn) + " does not exist for this class"
            thread.exit()
        # Wait 10 miniutes to try again to prevent too much request
        count += 1
        time.sleep(600)


def main():
    # https://courses.illinois.edu/schedule/2016/fall/CS/173
    print "Type 'exit' to exit"
    while True:
        print "1. Enter the class url"
        print "2. Enter the crn"

        while True:
            url = raw_input()
            if url == "exit":
                print "Program exiting..."
                sys.exit(0)
            if validators.url(url):
                break
            print "Not a valid url"
            print "Please enter a valid url"

        while True:
            try:
                crn = int(raw_input())
            except ValueError:
                print("That's not a number!")
                continue
            if crn == "exit":
                print "Program exiting..."
                sys.exit(0)
            if len(str(crn)) == 5:
                break
            print("That's not a crn!")

        thread.start_new_thread(check, (url, crn))


if __name__ == "__main__":
    main()
