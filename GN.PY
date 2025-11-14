# 猜數字遊戲
# 數字範圍 : 1-100 
import random
def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("歡迎來到猜數字遊戲！請在1到100之間猜一個數字。")

    while True:
        try:
            user_guess = int(input("請輸入你的猜測: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("請輸入一個介於1到100之間的數字。")
                continue

            if user_guess < number_to_guess:
                print("太低了！再試一次。")
            elif user_guess > number_to_guess:
                print("太高了！再試一次。")
            else:
                print(f"恭喜你！你猜對了，答案是 {number_to_guess}。你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("無效的輸入，請輸入一個整數。")
if __name__ == "__main__":
    guess_number()
    