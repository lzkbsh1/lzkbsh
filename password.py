#字典
import sys
import pinyin
def mingzi(A):
    a1=pinyin.get_initial(str(A),delimiter="")
    a2=pinyin.get(str(A),format="strip",delimiter="")
    if len(a1) < 4:a3=a1[1:]
    else: a3=a1[2:]
    if len(A)<4:D=A[:1];E=A[1:]
    else:D=A[:2];E=A[2:]
    a4 = pinyin.get(str(D), format="strip", delimiter="")
    a5 = pinyin.get(str(E), format="strip", delimiter="")
    a6 = a1[::-1]
    a=[a1,a2,a3,a4,a5,a6,a1.upper(),a2.upper(),a3.upper(),a5.upper(),a6.upper(),a4.capitalize(),a2.capitalize(),a3.capitalize(),a1.capitalize(),a5.capitalize(),a6.capitalize()]
    return a
def shuziaddmingzi(a,B22,C=""):
    b=[]
    zimu1=[chr(i) for i in range(97,123)]+[chr(i) for i in range(65,91)]
    for i in a:
        if len(B22)==0:
            b1 = i;b2 = i
            b11 = b1 + ".."; b12 = b2 + ".."
            b13 = b1 + "@qq.com";b14 = b2 + "@163.com";
            b3 = "_" + i; b4 = i + "_"
            b5 = "+" + i; b6 = i + "+"
            b7 = "@" + i;b8 = i + "@"
            b9 = "-" + i;b10 = i + "-"
            b.append(b1);b.append(b2);b.append(b3);b.append(b4); b.append(b5);b.append(b8); b.append(b9); b.append(b10);b.append(b12);b.append(b13);b.append(b14)
        for j in B22:
          b1=i+j;b2=j+i;
          b11=b1+"..";b12=b2+".."
          b13 =b1+ "@qq.com";
          b14 = b2+ "@163.com"
          b3=j+"_"+i;b4=i+"_"+j
          b5=j+"+"+i;b6=i+"+"+j
          b7=j+"@"+i;b8=i+"@"+j
          b9=j+"-"+i;b10=i+"-"+j
          b.append(b1);b.append(b2);b.append(b3);b.append(b4);b.append(b5);b.append(b8);b.append(b9);b.append(b10);b.append(b11);b.append(b12);b.append(b13);b.append(b14)
    for j in B22:
        for i in C:
          b1=i+j;b2=j+i;
          b.append(b1);
          b.append(b2);
        for i in zimu1:
          b1=i+j;b2=j+i;b11=str(b1)+"..";b12=(b2)+".."
          b3=i*2+j;b4=j+i*2
          b5=i.upper()+i+j;
          b.append(b1);b.append(b2);b.append(b3);b.append(b4);b.append(b5);b.append(b11);b.append(b12)
        b.append("ABC"+j);b.append(j+"@qq.com");b.append(j+"@163.com");b.append("abc"+j);b.append("qwe"+j);b.append("ABC"+j+"..");b.append("abc"+j+"..");b.append("qwe"+j+"..")
    return b
def endfuhao(C,b):
    c=[]
    for i in C:
        for j in b:
            c1=j+i
            c.append(c1)
    return c
if __name__ == '__main__':
    print("先名字，后数字")
    word=[]
    F = sys.argv[1]
    A = sys.argv[2]
    if F == "-n":
        a = mingzi(A.strip())
    else:
        a = [A]
    B = sys.argv[3:]
    #C=sys.argv[2]
    C = "!@#$%^&*()_+=-/|\?'\"><,."
    word=word+a
    B22=[]
    if B:
      B2=str(B)[-6:-2];
      print(B2)
      B22=[B[0],B2]
    b=shuziaddmingzi(word,B22,C)
    word=word+b+B22
    c=endfuhao(C,word)
    D="hupu"
    word=word+c
    with open("test.txt","w") as f:
        for i in word:
            f.write(i+"\n")
        print("ok")
