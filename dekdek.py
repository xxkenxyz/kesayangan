# jangan lupa subscribe MisterAM
# Sepesial idul fitri
# sceipt gua kagak pernah gua encriypt ngab

#jangan ubah
import requests,os,sys,time
from time import sleep
#kalo biaa jangan di ubah :v
os.system('clear')
print ('\033[36;1mSubscribe yt ku ngab \033[37mMisterAM \033[36mok! :v')
os.system('termux-open-url https://youtube.com/channel/UCXk4vbvDl7i6dxWBtNdpx6w')
sleep(5)
os.system('clear')
print ('\033[36;1mjoin grub \033[37;1mwa gua ngab :v')
os.system('xdg-open https://cararegistrasi.com/5QxXfcSkSsm')
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
\033[33;1m║  \033[36;1m [•] Authour : MisterAM                      \033[33;1m ║
\033[33;1m║  \033[36;1m [•] gitHub  : https:github.com/Mister-AM    \033[33;1m ║
\033[33;1m║  \033[36;1m [•] Yotube  : MisterAM                      \033[33;1m ║
\033[33;1m╚════════════════════════════════════════════════╝
\033[36;1m╔═══════════════════════════╗
\033[36;1m║\033[33;1m GUNAKAN DENGAB BJIAK NGAB\033[36;1m ║
\033[36;1m╚═══════════════════════════╝"""
sleep(1)
print(banner)

# Jangan lu ubah ngab
print ('\033[31;1m[!] \033[32;1mContoh nomor : \033[33;1m8xxxxxxx')

nomor = input(' \033[36;1minput nomor lu :\033[33;1m ')
print ('\033[32;1mMASUKAN JUMLAH SPAMNYA NGAB')
print ('')
jm = int(input('\033[31;1m Jumlah Spam :\033[33;1m '))

for i in range(jm):
      req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
      if "mengirim" in req:
            print ('\n \033[37;1m[\033[32;1m√\033[37;1m]\033[32;1mMENGIRIM SPAM')
      else:
            print ('\n \033[37;1m[\033[33;1m•••\033[37;1m]\033[36;1mMENCOBA MENGIRIM SPAM')


# subscribe MisterAM