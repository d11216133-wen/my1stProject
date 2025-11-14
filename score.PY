#自己輸入分數計算功能設計
def calculate_average_score(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)
def main():
    scores = []
    print("請輸入學生的分數（輸入 'done' 結束輸入）")
    while True:
        entry = input("請輸入分數: ")
        if entry.lower() == 'done':
            break
        try:
            score = float(entry)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("分數必須在0到100之間，請重新輸入。")
        except ValueError:
            print("無效的輸入，請輸入數字或 'done' 結束。")
    average_score = calculate_average_score(scores)
    print(f"學生的平均分數是: {average_score:.2f}")
if __name__ == "__main__":
    main()
# 分數計算功能
# 使用 Python 實現
    
    