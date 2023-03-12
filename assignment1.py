a = 1500000  # 300만원의 50% -> 매달 들어가는 월급
r = 0.024 # 이자율
y = 12 # 개월
interest = 0 # 이자

for i in range(1, y + 1):
    interest += a * r * i/12
int_interest = int(interest)
int_tax = int(interest * (15.4 / 100))
print("[대마뱅크]")
print("이*호님, 자유적금이 만기되어 알려드립니다.")
print(f"원금 : {a * 12:,}원")
print(f"세전이자 : {int_interest:,}원")
print(f"이자과세(15.4%) : {int_tax:,}원")
print(f"세후 수려 : {a * 12 + int_interest - int_tax:,}원")
