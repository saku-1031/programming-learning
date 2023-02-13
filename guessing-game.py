import random

ans = random.randint(1, 100)
fin = 0
intans = 0
count = 0
while fin == 0:
    intans = input("答えはなんだと思いますか？")
    if int(intans) == ans:
        print("正解！！答えは" + str(ans) + "です。\n今回は" + str(count) + "回間違えました")
        fin = 1
    else:
        if ans < int(intans):
            print("答えは" + str(intans) + "よりも少ないです。")
            count += 1
        elif ans > int(intans):
            print("答えは" + str(intans) + "よりも多いです。")
            count += 1
