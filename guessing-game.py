# This file was produced by Crunchy Studio.
# Retrieved from https://github.com/saku-1031/programming-learning
# Please read the README before use!

import random

# 変数の宣言
ans = random.randint(1, 100)
fin = 0
intans = 0
count = 0
# while文の宣言
while fin == 0:
    # 答えの予想の入力
    intans = input("答えはなんだと思いますか？")
    # 正解・不正解の判定
    if int(intans) == ans:
        # 正解だった時の処理
        print("正解！！答えは" + str(ans) + "です。\n今回は" + str(count) + "回間違えました")
        if count <= 5:
            print("平均より少ないです。")
        elif count >= 9:
            print("平均より多いです。")
        else:
            print("平均的です。")
        fin = 1
    else:
        # 不正解だった時の処理
        if ans < int(intans):
            # 答えの方が少なかった時の処理
            print("答えは" + str(intans) + "よりも少ないです。")
            count += 1
        elif ans > int(intans):
            # 答えの方が多かった時の処理
            print("答えは" + str(intans) + "よりも多いです。")
            count += 1
        # 10％の確率でヒントを出す処理
        hint = random.randint(1, 10)
        if hint == 1:
            # Hintを出力する処理
            ans_list = [random.randint(1, 100), ans, random.randint(1, 100)]
            random.shuffle(ans_list)
            print("Hint！！ 答えは" + str(ans_list) + "のどれかです。")
