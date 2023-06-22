id="pythonisfun"
password="ilovepython"
a=input("아이디를 입력하시오: ")
if(a==id):
    b=input("비밀번호를 입력하시오: ")
    if(b==password):
        print("환영합니다")
    else:
        print("비밀번호가 일치하지 않습니다")
else:
    print("아이디를 찾을 수 없습니다")
