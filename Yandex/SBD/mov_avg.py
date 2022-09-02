N = int(input())
Q = list(map(int, input().split()))
K = int(input())


def moving_average(N, Q, K):
    result = []
    current_sum = sum(Q[0:K])
    result.append(current_sum / K)
    for i in range(0, N - K):
        current_sum -= Q[i]
        current_sum += Q[i + K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result

print(" ".join(list(map(str, moving_average(N, Q, K)))))
