import urllib.request
def  read_text():
    quotes = open(r"C:\Users\Школа\song.txt")
    contents=quotes.read()
    req=''
    for i in contents:
        if i==' ':
            req+='%20'
        elif i=='\n':
            req+='%20'
        else:
            req+=i
    s=req.split('%20')
    quotes.close()
    return req,s
def chek_text(text,text2):

    
    conection=urllib.request.urlopen("https://www.purgomalum.com/service/plain?text="+text)
    out=conection.read().decode("utf-8")
    text1=out.split()
    text3=[]
    for i in range(0,len(text1)):
        if '*' in text1[i]:
            q=''
            for x in str(text2[i]):
                if x=='a' or x=='u' or x=='i' or x=='e'or x=='o':
                    q+='*'
                else:
                    q+=x
            text3.append(q)
        else:
            text3.append(text2[i])
    
    final_text=' '.join(text3)
    
    print(final_text)
            
    #if 'true' in out:
       # print('curse words involved')
    #elif 'false':
       # print("this text doesn't contain curse words")
    conection.close()
    
    
text,text2=read_text()
chek_text(text,text2)

