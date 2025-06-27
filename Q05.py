#1. 조건

# 정수형 데이터 1,000,000개로 구성된 리스트가 주어진다.

#각 정수는 1 이상 1,000,000 이하의 값이다.
import numpy as np
import time
ar1= np.random.randint(1, 1000000, 1000000)

#해당 리스트를 제한 시간 3초 이내에 정렬해야 한다.
time_start = time.time()
time_end = time.time()
#정렬이 완료된 리스트의 앞 10개 항목을 출력해야 한다.
ar_sorted = sorted(ar1)
#정렬 정확성, 실행 시간, 출력값을 동시에 검사하여 조건을 만족하면 "TRUE", 하나라도 어기면 "FALSE"를 출력한다.
if ar_sorted == sorted(ar1) and time_start - time_end < 3:
    print(ar_sorted[:10])
    print(f'time_taken: {round(time_end -time_start, 4)}')
    print("PASSCORD : TRUE")
else:
    print(ar_sorted[:10])
    print(f'time_taken: {round(time_end -time_start, 4)}')
    print("PASSCORD : FALSE")

# dataframe으로 저장
# 전체 list를 한 줄로 csv에 저장
import pandas as pd
ar1 = pd.DataFrame(ar_sorted)
ar1.T.to_csv('Question5.csv', index=False, header=False)