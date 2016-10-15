import cookielib

import mechanize
import requests

url = 'https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1'
# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
# br.set_debug_http(True)
# br.set_debug_redirects(True)
# br.set_debug_responses(True)

r = br.open(url)

html = r.read()
# for f in br.forms():
#    print f

br.select_form(nr=0)
# =========== input the user id and the password here ======================================
br.form['inputEnterpriseId'] =
br.form['password'] =
# ===========================================================================================

# click the Registration & Records link
req = br.submit()
br.open(req.geturl())

# for f in br.links():
#    print f

# click the registartion link
req = br.follow_link(nr=13)
br.open(req.geturl())
# print req.read()
# for f in br.links():
#    print f

req = br.follow_link(nr=11)
br.open(req.geturl())
# print req.read()

# add/drop class
req = br.follow_link(nr=14)
br.open(req.geturl())

# i agree link
req = br.follow_link(nr=13)
print req.read()
print req.read()
for f in br.links():
    print f

# br.select_form(nr=1)
'''
sBegin='submit'
l=['1','2','3','4']
for item in l:
    s=sBegin+item
    br.open(req.geturl())
    br.submit(name=s)
'''
data = {
    'term_in': '120168',
    'submit': 'Submit'
}

requests.get(req.geturl(), data=data)
# req = br.submit(name='submit', label='Submit')
# print req.read()
# print req.geturl()
# req = br.submit()
# print req.read()
# for f in br.links():
#    print f

# find if there is a hold on your account.
'''
data = br.open(req.geturl()).read()
soup = bs(data)
for span in soup.findAll('span'):
    if span['class'] == 'errortext':
        print 'There is a hold on your account'
'''
