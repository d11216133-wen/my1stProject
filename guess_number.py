# 猜數字遊戲
# 數字範圍: 1-100
# 玩家每次輸入猜測數字，程式提示「大了」或「小了」
# 猜對時顯示「恭喜通過！」並結束遊戲
# 記錄並顯示猜測次數

import random

def main():
    # 隨機產生一個1到100的整數答案
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("歡迎來到猜數字遊戲！")
    print("我已經想好了一個1到100之間的數字，請開始猜測吧！")
    
    while True:
        try:
            # 玩家輸入猜測數字
            guess = input("請輸入你的猜測 (1-100): ")
            guess_number = int(guess)
            
            # 檢查輸入範圍
            if guess_number < 1 or guess_number > 100:
                print("請輸入1到100之間的數字！")
                continue
            
            # 增加猜測次數
            attempts += 1
            
            # 判斷猜測結果
            if guess_number > secret_number:
                print(f"大了！這是你的第 {attempts} 次猜測。")
            elif guess_number < secret_number:
                print(f"小了！這是你的第 {attempts} 次猜測。")
            else:
                # 猜對了
                print(f"恭喜通過！你猜對了！答案是 {secret_number}。")
                print(f"你總共猜了 {attempts} 次。")
                break
                
        except ValueError:
            print("請輸入有效的數字！")
        except EOFError:
            print(f"\n遊戲結束！正確答案是 {secret_number}。你總共猜了 {attempts} 次。")
            break
        except KeyboardInterrupt:
            print(f"\n遊戲結束！正確答案是 {secret_number}。你總共猜了 {attempts} 次。")
            break

if __name__ == "__main__":
    main()
