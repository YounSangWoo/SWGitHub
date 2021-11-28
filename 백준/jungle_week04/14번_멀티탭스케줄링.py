# https://www.acmicpc.net/problem/1700
""" 
예제 입력 1
2 7
2 3 2 3 1 2 7
예제 출력 1
2 """

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

p = list(map(int, input().split()))  # 제품들 순서

concent = [0]*n
indexlist = [0]*(k+1)
count = 0

for i in range(n):
    for j in range(k):
        if p[j] not in concent:
                concent[i] = p[j]
                break

if 0 in concent:
    print(0)

else:

    for i in range(n, k):
        if p[i] in concent:
            continue
        else:
            index = [0, 0]
            flag = False
            for j in range(n):
                # 콘센트에 사용중인제품중 다음 제품리스트에 없다면 해당제품 뽑는다.
                if concent[j] not in p[i:]:
                    concent[j] = p[i]
                    count += 1
                    flag = True
                    break
                elif index[1] < p[i:].index(concent[j]):  # 콘센트에 사용중이라면
                    index = [j, p[i:].index(concent[j])]
            if not flag:
                concent[index[0]] = p[i]
                count += 1
    print(count)



""" 
N, K = map(int, input().split())

multitap = list(map(int, input().split()))

plugs = []
count = 0

for i in range(K):
  # 있으면 건너 뛴다.
  if multitap[i] in plugs:
    continue

  # 플러그가 1개라도 비어 있으면 집어넣는다.
  if len(plugs) < N:
    plugs.append(multitap[i])
    continue

  multitap_idxs = []  # 다음 멀티탭의 값을 저장.
  hasplug = True

  for j in range(N):
	# 멀티탭 안에 플러그 값이 있다면
    if plugs[j] in multitap[i:]:
      # 멀티탭 인덱스 위치 값 가져오기.
      multitap_idx = multitap[i:].index(plugs[j])
    else:
      multitap_idx = 101
      hasplug = False

    # 인덱스에 값을 넣어준다.
    multitap_idxs.append(multitap_idx)

    # 없다면 종료
    if not hasplug:
      break

  # 플러그를 뽑는다.
  plug_out = multitap_idxs.index(max(multitap_idxs))
  del plugs[plug_out]  # 플러그에서 제거
  plugs.append(multitap[i])  # 플러그에 멀티탭 값 삽입
  count += 1  # 뽑았으므로 1 증가

print(count)
 """