
# jangan lupa subscribe MisterAM
# Sepesial idul fitri
# sceipt gua kagak pernah gua encriypt ngab

#jangan ubah
import requests,os,sys,time
from time import sleep
#kalo biaa jangan di ubah :v
os.system('clear')
print ('\033[36;1mJANGAN JADI BADUT BESTII \033[37mYAHAHA BADUT \033[36mok! :v')
os.system('DEK DEK INI TOL TERBUAT DARI ORANG YANG GABUT DAN BADUT WKWK')
sleep(5)
os.system('clear')
print ('\033[36;1mClayKronos\033[37;1mClayKronos :v')
os.system('SPAM BOOM GAK ADA OBENG 🤣🤣🤣🤣')
sleep(3)
os.system('clear')
# Ubah Terserah kalian ngab
banner= """

\033[31;1m ███████╗██████╗  █████╗ ███╗   ███╗ \033[31;1m███████╗███╗   ███╗███████╗
\033[31;1m ██╔════╝██╔══██╗██╔══██╗████╗ ████║ \033[31;1m██╔════╝████╗ ████║██╔════╝
\033[31;1m ███████╗██████╔╝███████║██╔████╔██║ \033[31;1m███████╗██╔████╔██║███████╗
\033[37;1m ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║ \033[37;1m╚════██║██║╚██╔╝██║╚════██║
\033[37;1m ███████║██║     ██║  ██║██║ ╚═╝ ██║ \033[37;1m███████║██║ ╚═╝ ██║███████║
\033[37;1m ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ \033[37;1m╚══════╝╚═╝     ╚═╝╚══════╝

\033[33;1m╔════════════════════════════════════════════════╗
\033[33;1m║  \033[36;1m [•] Pembuat : XXKENXYZ                      \033[33;1m ║
\033[33;1m║  \033[36;1m [•] Developer  : XXKENXYZ X ClayKronos      \033[33;1m ║
\033[33;1m║  \033[36;1m [•] Tim  : ClayKronos                       \033[33;1m ║
\033[33;1m╚════════════════════════════════════════════════╝ 
\033[36;1m╔═════════════════════════════════════════════════════════════════════════╗
\033[36;1m║\033[33;1m GUNAKAN UNTUK SPAM MANTAN YANG SOK PALING TERSAKITI\033[36;1m ║
\033[36;1m╚═════════════════════════════════════════════════════════════════════════╝"""
sleep(1)
print(banner)

# Jangan lu ubah ngab
print ('\033[31;1m[!] \033[32;1mContoh nomor : \033[33;1m8xxxxxxx')

nomor = input(' \033[36;1minput nomor lu :\033[33;1m ')
print ('\033[32;1mMASUKAN JUMLAH SPAMNYA DEK')
print ('')
jm = int(input('\033[31;1m Jumlah Spam :\033[33;1m '))

for i in range(jm):
      req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
      if "mengirim" in req:
            print ('\n \033[37;1m[\033[32;1m√\033[37;1m]\033[32;1mMENGIRIM SPAM')
      else:
            print ('\n \033[37;1m[\033[33;1m•••\033[37;1m]\033[36;1mMENCOBA MENGIRIM SPAM')

