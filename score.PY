#自己輸入分數計算功能設計
#	設計簡單的分數計算器：輸入考試成績，程式自動計算平均分數。
#	加入錯誤處理：遇到非數字輸入時，提示「請輸入有效分數」。
#	每次修改後，使用 GitHub 進行版本管理，留下註解。
def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)
def main():
    scores = []
    print("歡迎使用分數計算器！請輸入考試成績（輸入 'exit' 離開並計算平均分數）")
    while True:
        entry = input("請輸入分數: ")
        if entry.lower() == 'exit':
            average = calculate_average(scores)
            print(f"平均分數是: {average:.2f}")
            break
        try:
            score = float(entry)
            if score < 0 or score > 100:
                print("請輸入有效分數（0-100）。")
                continue
            scores.append(score)
        except ValueError:
            print("請輸入有效分數。")
if __name__ == "__main__":
    main()
# GitHub 版本管理註解範例：
# v1.0 - 初始版本，實現基本的分數輸入和平均計算功能。
# v1.1 - 加入錯誤處理，提示非數字輸入。
# v1.2 - 限制分數範圍在0到100之間，並加入相應提示。
# v1.3 - 優化輸出格式，平均分數顯示兩位小數。
    

    