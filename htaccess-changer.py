#                                    LICENSE BSD 2 CLAUSE                                       #
#                   Copyright 2012 Mirio. All rights reserved.                                  #
#   Redistribution and use in source and binary forms, with or without modification, are        #
#   permitted provided that the following conditions are met:                                   #
#       1. Redistributions of source code must retain the above copyright notice, this list of  #
#      conditions and the following disclaimer.                                                 #
#       2. Redistributions in binary form must reproduce the above copyright notice, this list  #
#      of conditions and the following disclaimer in the documentation and/or other materials   #
#      provided with the distribution.                                                          #
#                                                                                               #
#   THIS SOFTWARE IS PROVIDED BY Mirio ''AS IS'' AND ANY EXPRESS OR IMPLIED                     #
#   WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND    #
#   FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR    #
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
#   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR    #
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON    #
#   ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING          #
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF        #
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                                  #
#                                                                                               #
#   The views and conclusions contained in the software and documentation are those of the      #
#   authors and should not be interpreted as representing official policies, either expressed   #
#   or implied, of Mirio                                                                        #   

__version__ = "1.0"


from ftplib import FTP
import urllib2

# Inizializzazione
ftp_host = ''
ftp_user = ''
ftp_pass = ''
ftp_dir = ''

# Funzioni
def get_myip():
    request_url = urllib2.Request(url="http://mirio.altervista.org/getmyip.php")
    request_url.add_header('User-agent','Mozilla/5.0')
    openurl = urllib2.urlopen(request_url)
    return openurl.read()

def create_htaccess(allow_users):
    htaccess_write = open('.htaccess', 'wb')
    htaccess_write.write('<Files ~ "^\.(htaccess|htpasswd)$">\ndeny from all\n')
    htaccess_write.write('</Files>\norder deny,allow\ndeny from all\n')
    htaccess_write.write('allow from ' + get_myip() + '\n')
    for user in range(0,allow_users):
        ip = raw_input("Insert number of user it's allowed\n--> ")
        htaccess_write.write('allow from ' + str(ip) + '\n')
    htaccess_write.close()

# Utenti
print "Htaccess-changer " + __version__
allow_users = int(raw_input("Who have allowed to access in this folder?"
                                                    "(except you)\n-> "))

# Creazione e apertura
create_htaccess(allow_users)
htaccess = open(".htaccess", 'rb')

# FTP Upload
ftp = FTP(ftp_host)
ftp.login(ftp_user,ftp_pass)
print ftp.sendcmd('TYPE I')
print ftp.cwd(ftp_dir)
print ftp.storbinary('STOR .htaccess', htaccess )
print ftp.quit()
