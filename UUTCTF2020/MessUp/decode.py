# This code is for UUTCTF 2020 mess up.txt
# MessUp.txt is belongs to UUTCTF 2020
# morse function is copyed from https://note.com/hungair0925/n/n20d267d98522
# and add some data to dic array by this author

import sys
import base64

def decode(x):
    infile = open("./mess_up.txt", "r")
    txt = infile.read()
    for i in range(int(x)):
        txt = base64.b64decode(txt)

    infile.close()

    return txt.decode()


dic = {
    '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G',
    '....':'H', '..':'-', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N',
    '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U',
    '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z', '.----':'1',
    '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7',
    '---..':'8', '----.':'9', '-----':'0', '.-.-.-':'.', '--..--':',', '---...':':',
    '..--..':'?', '.-.-.':'+', '-....-':'-', '.-..-.':'"', '-.--.':'(', '-.--.-':')',
    '-..-.':'/', '.--.-.':'@', '.----.':"'"
}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
    return "".join(result)


tmpTxt = decode(1)
length= len(tmpTxt)
print(tmpTxt[0:7]+morse(tmpTxt[7:length-1])+tmpTxt[length-1])
