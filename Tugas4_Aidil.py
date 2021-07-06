email=input('Masukkan Email Anda: ')
alfanum="._1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
spec=""" !"#$%&'()*+,-/:;<=>?[\]^`{|}~ """ ### Tanpa .(titik) dan @

def cekemail(x):
    if '.' not in x or '@' not in x:
        hasil = "format email salah"
        return hasil
    else:        
        at=email.count('@')
        if at > 0:
            cekuser=True
            cekemail=True
            user=email[0:email.index('@')]
            host=email[email.index('@')+1:]
            host1=host[:host.index('.')]
            hostext=host[host.index('.')+1:]
            if len(user) == 0:
                hasil = 'format username salah'
                return hasil
            if user[0].isalnum():
                for y in user:
                    if y not in alfanum:
                        cekuser=False
                        break
            else:
                hasil = "format username salah"
                return hasil
            
            for z in email:
                if z in spec:
                    cekemail=False
                    break
            if '.' in hostext:
                ext1=hostext[:hostext.index('.')]
                ext2=hostext[hostext.index('.')+1:]

                if at == 1 and cekuser == True and cekemail == True and host1.isalnum() and ((hostext.isalpha() and len(hostext)<=5) or (ext1.isalpha() and ext2.isalpha() and len(ext1)<=5 and len(ext2)<=5)):
                    hasil = 'alamat email anda valid'
                else:
                    hasil = 'alamat email anda invalid'
                    if at != 1:
                        hasil += ', terlalu banyak @'
                    elif cekuser == False:
                        hasil += ', format username salah'
                    elif host1.isalnum() == False:
                        hasil += ', format alamat hosting salah'
                    elif ((hostext.isalpha() and len(hostext)<=5) or (ext1.isalpha() and ext2.isalpha() and len(ext1)<=5 and len(ext2)<=5)) == False:
                        hasil += ', format extensi salah'
            else:
                if at == 1 and cekuser == True and cekemail == True and host1.isalnum() and ((hostext.isalpha() and len(hostext)<=5)):
                    hasil = 'alamat email anda valid'
                else:
                    hasil = 'alamat email anda invalid'
                    if at != 1:
                        hasil += ', terlalu banyak @'
                    elif cekuser == False:
                        hasil += ', format username salah'
                    elif host1.isalnum() == False:
                        hasil += ', format alamat hosting salah'
                    elif ((hostext.isalpha() and len(hostext)<=5)==False):
                        hasil += ', format extensi salah'
        else:
            hasil="email anda invalid, karena tidak terdapat @"
        return hasil

print(cekemail(email))
##aidil@gmail.com
