# This file was produced by Crunchy Studio.
# Retrieved from https://github.com/saku-1031/programming-learning
# Please read the README before use!

import random

ans = random.randint(1, 100)
fin = 0
intans = 0
count = 0
while fin == 0:
    intans = input("答えはなんだと思いますか？")
    if int(intans) == ans:
        print("正解！！答えは" + str(ans) + "です。\n今回は" + str(count) + "回間違えました")
        if count <= 5:
            print("平均より少ないです。")
        elif count >= 9:
            print("平均より多いです。")
        else:
            print("平均的です。")
        fin = 1
    else:
        if ans < int(intans):
            print("答えは" + str(intans) + "よりも少ないです。")
            count += 1
        elif ans > int(intans):
            print("答えは" + str(intans) + "よりも多いです。")
            count += 1
        challenge = random.randint(1, 10)
        if challenge == 1:
            ans_list = [random.randint(1, 100), ans, random.randint(1, 100)]
            random.shuffle(ans_list)
            print("challenge！！ 答えは" + str(ans_list) + "のどれかです。")
