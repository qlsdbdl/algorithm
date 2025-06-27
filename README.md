TEAM 1

#전체 프로젝트 설명

\### 01. 데이터 전처리 후 정렬 알고리즘 사용하고 모두 더하는 코드

- 영단어 숫자 → 숫자 매핑

word\_to\_num이라는 딕셔너리를 통해 "one", "five" 같은 단어를 숫자와 매핑함

- 문자열 내 숫자 판별 및 변환

정수로 변환 가능한 문자열 ("42", "-7")인지 정규표현식을 이용해 검사하고 int()로 변환함.

변환이 안 되는 값은 None으로 처리하였음 (정렬을 하지 않아도 되기 때문)

- 중복 제거 + 정렬

정수로 변환된 리스트에서 중복된 값을 제거하고, 오름차순으로 정렬함.

- 총합 계산 및 출력

최종적으로 정제된 리스트의 모든 값을 더해 총합을 출력

- 다양한 정렬 알고리즘 활용을 못했음

데이터가 너무 작아서 아무 거나 사용해도 될거라고 생각했음

\# GPT 피드백

1. for i in range(len(shuffled\_list)) 반복문 사용

`	`range(len()) + 인덱스 접근보다, for element in list 직접 순회가 보통 더 깔끔하다.

1. None 처리가 두 번 있음, 중간에 None을 넣었다가, 다시 필터링해서 제거하는 과정이 비효율적이다.



\### 02. 이진 탐색을 활용하여 특정 값의 처음과 마지막 인덱스를 찾아 더하는 코드

\# 개선점

\# 1. 인덱스 찾을 시 이진탐색 미사용

- 문제에서는 인덱스를 찾을 때 이진탐색을 사용하여 해결하라고 나와있지만, 문제를 잘못 이해하여 target값을 찾을 때만 이진탐색 사용.
- 개선된 버전(GPT 사용): start\_index, end\_index 각각의 함수를 정의해서 구현
- find\_start 함수: 전체 리스트의 mid 값을 기준으로 왼쪽만 탐색하여 값 찾기
- end\_start 함수: 전체 리스트의 mid 값을 기준으로 오른쪽만 탐색하여 값 찾기
- 추가 논의 사항: 데이터 수나 형태에 따라 start와 end의 index가 명확하게 출력되지 않을 가능성 있음

'''

def binary\_search(arr, target):

\# start index 찾기

def find\_start():

left, right = 0, len(arr) - 1

result = -1

while left <= right:

mid = (left + right) // 2

if arr[mid] == target:

result = mid

right = mid - 1  # 왼쪽으로 더 탐색

elif arr[mid] < target:

left = mid + 1

else:

right = mid - 1

return result

\# end index 찾기

def find\_end():

left, right = 0, len(arr) - 1

result = -1

while left <= right:

mid = (left + right) // 2

if arr[mid] == target:

result = mid

left = mid + 1  # 오른쪽으로 더 탐색

elif arr[mid] < target:

left = mid + 1

else:

right = mid - 1

return result

start\_index = find\_start()

end\_index = find\_end()

if start\_index == -1 or end\_index == -1:

print("NOT FOUND")

return "notfound"

print(f"{start\_index} {end\_index}")

return start\_index + end\_index

'''

2\. 리스트에 없을 시 출력 결과 없음

- target이 리스트에 없을 시 not found 출력해야 하는데, 이 부분 구현 x

- 추가된 코드

'''

start\_index, end\_index = binary\_search(lst, target)

if start\_index == '' and end\_index == '':

print('PASSCORD = NOT FOUND')

'''

총평

- 문제의 의미를 제대로 이해하지 못해 놓친 부분이 많음.
- 코드에서 비효율적인 부분 다수 존재


\### 03. 리스트에서 가장 많이 나온 숫자와 그 횟수를 더해서 Passcord를 구하는 코드

\# 개선점
Passcode를 출력하는 부분에서, 
num, count = sorted_items[0] 방식으로 출력하였으면 더욱 간결하게 만들 수 있었을 것 같다.

- collections.Counter를 이용하여 리스트 내 각 숫자가 몇 번 등장했는지를 자동으로 계산

freq.items()를 활용하여 (숫자, 횟수) 튜플을 가져오고, 정렬을 시킨다. 
정렬 방법은 lambda를 사용하여 튜플을 x로 표현하였다. 정렬 기준은 아래와 같다. 

- 첫 번째 기준: 등장 횟수 기준 내림차순 (가장 많이 나온 숫자를 우선으로) (-x[1])
- 두 번째 기준: 등장 횟수가 같을 경우, 숫자 자체는 큰 숫자 우선으로 출력하여 내림차순으로 나타낸다.  (-x[0])
이 두 개의 기준으로 정렬헀다.

\# GPT피드백

1. sorted\_items 리스트 두 번 출력했음 (중복)
1. freq.most\_common()을 쓰면 정렬 없이도 상위 항목을 얻을 수 있음


\### 04. 격자에서, 각 칸의 값만큼 이동하면서 도착지(0)까지 도달하는 가장 가까운 경로를 DFS로 찾아주는 코드

- DFS(깊이 우선 탐색) 기반 경로 탐색 → 시작점 (0, 0)부터 재귀적으로 모든 가능한 경로를 탐색함

- 백트래킹 사용 → 탐색을 마친 뒤에는 visited, path, values 리스트에서 현재 위치를 제거함으로써 다음 경로 탐색에 영향을 주지 않게 했음

- (x, y) 위치마다 누적합을 저장해서 중복 탐색을 막았음

- DFS가 모든 경로를 탐색하느라 1초 이내에 탐색을 끝내지 못해서 시간 제한을 초과했기 때문에 "FAIL"이 출력됨.

- min\_sum = [float('inf')] 대신 그냥 min\_sum = float('inf') 가능했었음

\# 총 정리

전체적으로 로직은 명확하고 구현력도 괜찮았지만, 시간 제한 조건 누락과 정의되지 않은 변수(all\_paths)로 인해 채점 시 FAIL 발생 가능성이 있었음.

간단한 조건문 수정과 DFS 제한 또는 BFS 전환으로 충분히 개선 가능


\### 05. sorted()를 활용하여 대용량 array 정렬 및 소요 시간 측정하는 코드

- 100만 개의 정수 데이터를 생성하여 정렬하고, 정렬 정확성과 3초 이내 완료 여부를 동시에 확인

- numpy를 사용해 100만개 정수 생성

- sorted()로 통해 정렬

- 정렬 시작 직전(time\_start)과 끝 시간(time\_end) 둘다 저장

-> time\_end - time\_start를 통해 전체 정렬 시간 계산

- if ar\_sorted == sorted(ar1) and time\_start - time\_end < 3:

-> 정렬 정확성, 실행 시간, 출력값을 동시에 검사하여 조건을 만족하는지 확인

- 시간 계산 오류가 있었음

-> if time\_start - time\_end < 3:

- 비효율적인 pandas 전처리

-> ar1 = pd.DataFrame(ar\_sorted)

`	 `ar1.T.to\_csv(...)




