
# 학생식당 메뉴 리스트로 만들기

asian_food = ['쇠고기쌀국수', '얼큰 쇠고기 칼국수', '베트남쌀국수', '허기진 내영혼의 쌀국수', '얼큰 쌀국수', '베트남볶음면', '닭고기쌀국수', '쇠고기세트', '베트남세트', '왕새우세트',
              '치즈볼세트', '덕성여대 스페셜 세트1', '덕성여대 스페셜 세트2', '베트남새우볶음밥', '계란후라이볶음밥', '파인애플볶음밥', '왕새우튀김', '치즈볼', '베트남군만두짜조',
              '하이퐁탕수육', '버팔로 윙/봉']
ramen = ['미스터라멘', '돈코츠라멘', '시오라멘', '소유라멘', '탄탄멘', '매운돈코츠라멘', '마라탕멘', '열라맵닭라멘', '해장김치라멘', '스끼야끼라멘', '바질라멘', '공기밥',
         '교자튀김', '치킨가라아게', '버팔로윙']
japanese_western_food = ['돈까스우동세트', '제주흑돼지돈까스', '제주흑돼지돈까스정식', '통모짜돈까스정식', '카레밥', '제주흑돼지돈까스카레', '새우후라이 카레', '가라아게 카레',
                         '돈부리', '믹스동', '돈코츠라멘', '우동', '카레우동', '탄탄면', '냉모밀', '판모밀']
korean_food = ['우삼겹샐러드', '리코타샐러드', '그린샐러드', '닭가슴샐러드', '돼지김치찌개', '부대찌개', '된장찌개', '차돌된장찌개', '불닭마요덮밥', '참치마요덮밥', '제육덮밥',
               '오징어덮밥', '야채비빔밥', '소불고기덮밥', '불닭덮밥']
snack_food = ['크앙-라떡', '매콤크림파스타떡볶이', '크앙-라떡토핑튀김', '크앙-라떡토핑고기', '라면', '삼쫄', '호화스런 짜계치', '직화삼겹덮밥', '직화불삼겹덮밥', '직화우삼겹덮밥',
              '직화안창살덮밥', '모듬튀김', '크앙김말이튀김', '롱순대꼬치튀김', '치즈범벅-후라이']
hangover_soup = ['뼈해장국', '선지해장국', '추어탕', '해물순두부탕']

asian_food_prepared = []
ramen_prepared = []
japanese_western_food_prepared = []
korean_food_prepared = []
snack_food_prepared = []
hangover_soup_prepared = []

asian_food_remaining = []
ramen_remaining = []
japanese_western_food_remaining = []
korean_food_remaining = []
snack_food_remaining = []
hangover_soup_remaining = []


# 반복되는 규칙을 함수로 만들기

# 1. 식당 카테고리와 어떤 함수를 실행할건지 입력받는 함수

def category(q, f):
    if q == 1:
        f(asian_food, asian_food_prepared, asian_food_remaining)
    elif q == 2:
        f(ramen, ramen_prepared, ramen_remaining)
    elif q == 3:
        f(japanese_western_food, japanese_western_food_prepared, japanese_western_food_remaining)
    elif q == 4:
        f(korean_food, korean_food_prepared, korean_food_remaining)
    elif q == 5:
        f(snack_food, snack_food_prepared, snack_food_remaining)
    elif q == 6:
        f(hangover_soup, hangover_soup_prepared, hangover_soup_remaining)
    else:
        print('유효하지 않은 입력입니다.')


# 2. 준비된 메뉴의 수량을 입력받는 함수

def prepared(cafeteria_category, category_prepared, category_remaining):
    print()
    print('준비된 메뉴의 수량을 입력하세요.')
    for i in range(len(cafeteria_category)):
        menu_prepared = int(input(cafeteria_category[i]))
        category_prepared.append(menu_prepared)
        category_remaining.append(menu_prepared)
    print('준비된 메뉴의 수량이 모두 입력되었습니다.')


# 3. 주문된 메뉴의 수량을 입력받는 함수

def order(cafeteria_category, category_prepared, category_remaining):
    if len(category_prepared) == 0:
        print('아직 준비된 메뉴의 수량을 입력하지 않았습니다. 준비된 메뉴의 수량을 입력한 후 다시 시도해주세요.')
    else:
        print()
        for i in range(len(cafeteria_category)):
            print(i, cafeteria_category[i])
        print()
        menu = int(input('주문된 수량을 입력하려는 메뉴의 번호를 입력하세요.'))
        ordered = int(input('주문된 수량을 입력하세요.'))
        category_remaining[menu] = category_remaining[menu] - ordered
        print('주문된 수량이 입력되었습니다.')


# 4. 남은 메뉴의 수량과 품절된 메뉴를 출력하는 함수

def menu_list(cafeteria_category, category_prepared, category_remaining):
    menu_list_category = []
    menu_list_category_remaining = []
    menu_list_category_prepared = []
    sold_out_category = []
    sold_out_category_remaining = []
    sold_out_category_prepared = []
    if len(category_prepared) == 0:
        print('학생식당 직원이 아직 준비된 메뉴의 수량을 입력하지 않았습니다.')
    else:
        for i in range(len(cafeteria_category)):
            if category_remaining[i] > 0:
                menu_list_category.append(cafeteria_category[i])
                menu_list_category_remaining.append(category_remaining[i])
                menu_list_category_prepared.append(category_prepared[i])
        for m in range(len(cafeteria_category)):
            if category_remaining[m] <= 0:
                sold_out_category.append(cafeteria_category[m])
                sold_out_category_remaining.append(category_remaining[m])
                sold_out_category_prepared.append(category_prepared[m])
        print()
        for j in range(len(menu_list_category)):
            print(menu_list_category[j], menu_list_category_remaining[j], '/', menu_list_category_prepared[j])
        if len(sold_out_category) != 0:
            print()
            print('*****품절된 메뉴*****')
            print()
            for k in range(len(sold_out_category)):
                print(sold_out_category[k], sold_out_category_remaining[k], '/', sold_out_category_prepared[k])


# 만들어놓은 리스트와 함수를 사용하여 프로그램 코드 작성하기

while True:
    Q1 = input('학생식당 직원입니까? (Y 또는 N 입력)')
    if Q1 == 'Y':
        Q2 = int(input('준비된 메뉴 수량을 입력하려면 1, 주문된 메뉴의 수량을 입력하려면 2를 입력하세요.'))
        if Q2 == 1:
            Q3 = int(input('준비된 메뉴 수량을 입력할 식당 카테고리의 번호를 입력하세요. (1. 아시안푸드 2. 라멘 3.일식/양식 4. 한식 5. 분식 6. 해장국)'))
            category(Q3, prepared)
        elif Q2 == 2:
            Q4 = int(input('주문된 메뉴 수량을 입력할 식당 카테고리의 번호를 입력하세요. (1. 아시안푸드 2. 라멘 3.일식/양식 4. 한식 5. 분식 6. 해장국)'))
            category(Q4, order)
        else:
            print('유효하지 않은 입력입니다.')
    elif Q1 == 'N':
        Q5 = int(input('남은 메뉴와 수량을 확인하고싶은 식당 카테고리의 번호를 입력하세요. (1. 아시안푸드 2. 라멘 3.일식/양식 4. 한식 5. 분식 6. 해장국)'))
        category(Q5, menu_list)
    else:
        print('유효하지 않은 입력입니다.')
    print()
    end = input('식당이 정상영업 중입니까? (영업 중이면 Y, 영업이 종료되었으면 N 입력)')
    print()
    if end == 'Y':
        continue
    elif end == 'N':
        print('프로그램을 종료합니다.')
        break
    else:
        print('유효하지 않은 입력입니다.')
