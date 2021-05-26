import copy

def dfs(path, depth, result):
    if len(path)-1 == depth:
        sum_ = sum(path) - path[0]
        # print(sum_, path)
        if not result.get(sum_, None):
            result[sum_] = [copy.deepcopy(path[1:])]
            # print(result)
        else:
            result[sum_].append(copy.deepcopy(path[1:]))
            # print(result)
        return
    else:
        last = path[-1]
        if last >= 0:
            curr = [last+1, -last-1]
        else:
            curr = [-last-1, last+1]
        for each in curr:
            path.append(each)
            dfs(path, depth, result)
            path.pop()
        return

result = {}
for i in range(5, 21):
    dfs([1],i,result)
    print(result.keys())
    result = {}

