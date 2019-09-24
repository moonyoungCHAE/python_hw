# 각 월의 일 범위를 저장, 0월은 존재하지 않으므로 -1로 예외처리하였다.
days = [[-1], range(1, 32), range(1, 29), range(1, 32), range(1, 31), range(1, 32), range(1, 31), range(1, 32), range(1, 32), range(1, 31), range(1, 32), range(1, 31), range(1, 32)]

# 월:시작 요일 (일요일:1, 월요일:2 ... 토요일:7)
daysOfWeek = {1:3, 2:6, 3:6, 4:2, 5:4, 6:7, 7:2, 8:5, 9:1, 10:3, 11:6, 12:1}

print("채문영의 과제입니다.")

while(True):
    print()
    print()
    print("----- 달력 출력 프로그램 -----")
    month = input("원하는 달을 입력하세요. 종료를 원하시면 0을 입력하세요 ");
    try:
        month = int(month)
    except ValueError:
        print("원하는 달의 숫자만 입력해주세요")
        continue
        
    if month == 0:
        break

    if month < 0 || month > 12:
        print("1 ~ 12 사이의 숫자만 입력 가능합니다.")
        continue
    
    print("   2019 ", month, "월의 달력")
    print("일 월 화 수 목 금 토");
    
    # 각 월의 1일에 해당하는 공백을 만들어준다.
    dayOfWeek = daysOfWeek[month]
    for i in range(dayOfWeek - 1):
        print("  ", end = ' ')
        
    for day in list(days[month]):
        print(day, end = " ")
        
        # 1의 자리 일의 경우, 공백 처리를 추가로 하여 칸을 맞추어 주었다.
        if day < 10:
            print("", end=" ")
            
           
        # 각 주의 마지막 요일에 줄바꿈을 해준다.
        if dayOfWeek % 7 == 0:
            print()
        dayOfWeek += 1
        
        
