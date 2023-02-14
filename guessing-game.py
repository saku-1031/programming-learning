"""
This file was produced by Crunchy Studio.
Retrieved from https://github.com/saku-1031/programming-learning
Please read the README before use!
"""

import random

# 変数の宣言
level = input("レベルを選択してください\n1・・・初級/２・・・中級/3・・・上級")
result = [5, 7]
max_ans = 100
if level == str(1):
    print("初級で続けます")
    result = [2, 5]
    max_ans = 10
elif level == str(2):
    print("中級で続けます")
elif level == str(3):
    print("上級で続けます")
    result = [7, 17]
    max_ans = 1000
else:
    print("そのレベルは指定されていません\n中級で続けます。")
    max_ans = 100
ans = random.randint(1, max_ans)
fin = 0
ans_input = 0
count = 0
# while文の宣言
while fin == 0:
    # 答えの予想の入力
    ans_input = input("答えはなんだと思いますか？")
    # 正解・不正解の判定
    if int(ans_input) == ans:
        # 正解だった時の処理
        print("正解！！答えは" + str(ans) + "です。\n今回は" + str(count) + "回間違えました")
        if count == 0:
            print("イッパツクリア！！")
        elif count <= result[0]:
            print("平均より少ないです。")
        elif count >= result[1]:
            print("平均より多いです。")
        else:
            print("平均的です。")
        fin = 1
    else:
        # 不正解だった時の処理
        if ans < int(ans_input):
            # 答えの方が少なかった時の処理
            print("答えは" + str(ans_input) + "よりも少ないです。")
            count += 1
        elif ans > int(ans_input):
            # 答えの方が多かった時の処理
            print("答えは" + str(ans_input) + "よりも多いです。")
            count += 1
        # 10％の確率でヒントを出す処理
        hint = random.randint(1, 10)
        if hint == 1:
            # Hintを出力する処理
            ans_list = [random.randint(1, max_ans), ans, random.randint(1, max_ans)]
            random.shuffle(ans_list)
            print("Hint！！ 答えは" + str(ans_list) + "のどれかです。")
