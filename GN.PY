# 猜數字遊戲
# 數字範圍 : 1-9999 不能有重複數字
# 然後同位置同數字就是a 同數字不同位置就給幾B
# 例如 答案是 1234 玩家猜 1243 那麼結果就是 2A2B
# 玩家可以一直猜直到猜中為止
# 每次猜完會顯示猜的結果
# 玩家可以輸入 exit 離開遊戲
# 最後顯示總共猜了幾次
# 使用 Python 實現
import random
def generate_number():
    digits = list('0123456789')
    random.shuffle(digits)
    # 確保第一位數字不為0
    if digits[0] == '0':
        for i in range(1, 10):
            if digits[i] != '0':
                digits[0], digits[i] = digits[i], digits[0]
                break
    return ''.join(digits[:4])
def calculate_ab(secret, guess):
    a = sum(s == g for s, g in zip(secret, guess))
    b = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - a
    return a, b
def main():
    secret_number = generate_number()
    attempts = 0
    print("歡迎來到猜數字遊戲！請輸入4位不重複的數字（輸入 'exit' 離開遊戲）")
    while True:
        guess = input("請輸入你的猜測: ")
        if guess.lower() == 'exit':
            print(f"遊戲結束！正確答案是 {secret_number}。你總共猜了 {attempts} 次。")
            break
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("輸入無效，請輸入4位不重複的數字。")
            continue
        attempts += 1
        a, b = calculate_ab(secret_number, guess)
        print(f"結果: {a}A{b}B")
        if a == 4:
            print(f"恭喜你猜對了！你總共猜了 {attempts} 次。")
            break
if __name__ == "__main__":
    main()
    
