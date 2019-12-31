import string

def cipher_decoded(coded, offset):
    for i in coded:
        if i in string.ascii_lowercase:
            return coded.replace(i, (string.ascii_lowercase[(coded.find(i) - offset)])

print(cipher_decoded('xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
',  10)
