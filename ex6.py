from itertools import permutations


def check_evidence(evidence, base_structure):
    # 检查是否满足访问结构的基
    for subset in base_structure:
        if not set(subset).issubset(set(evidence)):
            return False
    return True


def print_first_and_last_evidence(n, base_structure):
    evidence_set = set()

    # 生成所有可能的有序四元组的排列
    permutations_list = list(permutations(range(1, n + 1)))

    # 遍历排列，检查是否满足访问结构的基
    for perm in permutations_list:
        if check_evidence(perm, base_structure):
            evidence_set.add(perm)

    # 输出按照变量序号升序排列的证据中的第一行
    first_evidence = sorted(evidence_set)[0]
    print(" ".join(map(str, first_evidence)))

    # 输出按照变量序号升序排列的证据中的最后一行
    last_evidence = sorted(evidence_set)[-1]
    print(" ".join(map(str, last_evidence)))


# 手动输入示例
n = int(input())
x = int(input())

base_structure = []
for _ in range(x):
    subset = list(map(int, input().split()))
    base_structure.append(subset)

# 输出按照变量序号升序排列的证据中的第一行和最后一行
print_first_and_last_evidence(n, base_structure)
print('#')