"""
developer : Shikhar singh
aim os script : To generate qrcode in png form 
"""
import os,time
try :
    import pyqrcode
    import png
    from pyqrcode import QRCode
except :
    print('Please Wait ..')
    os.system('pip install pyqrcode')
    os.system('pip install pypng')
if os.path.isdir('export_qrcode')==False:
    os.system('mkdir export_qrcode')
print('\033[0;30;42m APPLICATION BY KEERRORBAFUS FOR GENERATING QRCODE OF YOUR OWN \033[0;37;40m')
while True :
    QRstring = input("\nEnter or paste link: ")
    url = pyqrcode.create(QRstring)
    iname='export_qrcode/'+time.asctime()+'.png'
    url.png(iname,scale=8)
    print('  \033[0;33;40mfile_name : '+iname,'\n  qrcode generated sucessfully ! in [export_qrcode named folder]')
    if input('\033[0;37;40mwant to make another qrcode (y/n)')=='y':
        pass
    else :
        print('  Thanks for Choosing bafus Tool [@keerrorbafus]\n')
        break