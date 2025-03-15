#if-elif-else

scores = [75, 80, 97, 86, 45, 93, 90, 51, 91, 81]

for score in scores:
    if score >= 90:
        print(f'Score {score}: Grade A')
    elif score >= 80:
        print(f'Score {score}: Grade B')
    elif score >= 70:
        print(f'Score {score}: Grade C')
    elif score >= 50:
        print(f'Score {score}: Grade D')
    else:
        print(f'Score {score}: Grade E')