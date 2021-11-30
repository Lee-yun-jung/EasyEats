import random

#음식분야생성 
korea = ['제육볶음', '된장찌개', '김치찌개', '비빔밥']
china = ['짜장면', '짬뽕', '탕수육', '볶음밥']
italy = ['토마토파스타', '까르보나라', '목살필라프', '마르게리타피자']

print('안녕하세요! 이지잇츠를 찾아 주셔서 감사합니다.')
print('이지잇츠 한식, 중식, 양식 중 랜덤으로 음식을 추천해드리고 있는 프로그램입니다.')
print()

        
answer = str(input('한식, 중식, 양식 중 먹고 싶은 분야를 선택해 주세요.: '))

while ' ' :
    if answer == '한식' :
        mymenu = random.choice(korea)
        print('추천 메뉴는 ' + mymenu + '입니다.')
        break
    elif answer == '중식'  :
        mymenu = random.choice(china)
        print('추천 메뉴는 ' + mymenu+ '입니다.')
        break
    elif answer == '양식' :
        mymenu = random.choice(italy)
        print('추천 메뉴는 ' + mymenu + '입니다.')
        break
    else :
        answer = str(input('다시 입력해 주세요.: '))
        

print()

#음료배정
drinks = {'된장찌개':'사이다',
          '김치찌개':'콜라',
          '제육볶음':'사이다',
          '비빔밥':'사이다',
          '짜장면':'레몬에이드',
          '짬뽕':'자몽에이드',
          '탕수육':'맥주',
          '볶음밥':'콜라',
          '마르게리타피자':'맥주',
          '토마토파스타':'레몬에이드',
          '까르보나라':'콜라',
          '목살필라프':'와인'}
mydrink = str(input("음료수를 골라 드릴게요. 랜덤으로 나온 음식을 써주세요.: "))

while True:
    if mydrink in drinks:
      print( "%s은(는) %s와 먹어야 맛있습니다." % ( mydrink, drinks[mydrink]))
      print( "%s을(를) 드리겠습니다." % ( drinks[mydrink]))
      break
    else:
        print("음식만 입력해 주세요.")
        mydrink = str(input("다시 입력해 주세요.: "))
        
    
print()

#배달료안내
print("음식점은 모두 '천안신세계백화점' 부근에 있습니다.")
print("배달료는 <신부동-1000원/문화동-2000원/두정동-3000원/안서동-3000원>입니다.")

addresses = { '신부동':1000,
              '문화동':2000,
              '두정동':3000,
              '안서동':3000}

myaddress = str(input("배달시킬 지역을 입력해 주세요.: "))

while True:
    
    if myaddress in addresses:
        
     print("%s에서 주문하시면, 배달료는 %s원입니다." % (myaddress, addresses[myaddress]))
     break
    
    else:
      myaddress=str(input("정확하게 다시 입력해 주세요.(예시-두정동)): "))

print()

#음식금액안내
foods = {'제육볶음':7000,
         '된장찌개':8000,
         '김치찌개':9000,
         '비빔밥':7000,
         '짜장면':5000,
         '짬뽕':7000,
         '탕수육':10000,
         '볶음밥':6000,
         '마르게리타피자':9000,
         '토마토파스타':8000,
         '까르보나라':8000,
         '목살필라프':9000}
myfood = str(input("추천된 음식을 적어주세요: "))

while True:
    if myfood in foods:
        print("%s의 가격은 배달비 미포함 %s원입니다." % (myfood, foods[myfood]))
        break
    
    else:
        myfood=str(input("다시 입력해 주세요: "))
        

print('')

#결제금액안내
dilivey = addresses[myaddress]
fee = foods[myfood]
a= dilivey
b= fee
result= a+b
print('주문금액은',dilivey,'원','+',fee,'원,','총',result,'원입니다.')

print()


print('♡ 주문해 주셔서 감사합니다. ♡')
print()
print()

#별점등록
print('음식이 맛있으셨다면 리뷰를 남겨 주세요!')
score = int(input("점수를 입력해 주세요(숫자만 작성해 주세요.): "))
if score >= 90:
    print('★★★★★')
elif score >= 80:
    print('★★★★☆')
elif score >= 60:
    print('★★★☆☆')
elif score >= 40:
    print('★★☆☆☆')
elif score >= 20:

    print('★☆☆☆☆')
else:
    print('☆☆☆☆☆')


print()

print('♡ 감사합니다. 더 노력하는 식당이 되겠습니다. ♡')
print()
print('이지잇츠를 종료합니다.')
