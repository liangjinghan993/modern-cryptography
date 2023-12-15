#判断a1是不是a2的子集
def ziji(a1, a2):
    if len(a1) > len(a2):
        return False
    for item in a1:
        if item not in a2:
            return False
    return True

#检查a0是否被授权
def shouquan(a0, shouquanziji):
    for subset in shouquanziji:
        if ziji(subset, a0):
            return True
    return False

#比较a1、a2大小
def compare(a1, a2):
    if len(a1) == 0:
        return True
    elif len(a2) == 0:
        return False

    for i in range(min(len(a1), len(a2))):
        if a1[i] < a2[i]:
            return True
        elif a1[i] > a2[i]:
            return False

    return len(a1) < len(a2)


def main():
    # 输入 n，n个参与者
    n = int(input())
    # 输入 x，x个授权子集
    x = int(input())


    # 输入x个授权子集
    shouquanziji = []  # 创建一个空列表用于存储授权子集
    for _ in range(x):
        subset = sorted(list(map(int, input().split())))   #输入一行以空格分隔的整数，将其映射为整数列表，并按升序排序。得到的排序后的子集被赋值给 subset
        shouquanziji.append(subset)   #将排序后的子集添加到授权子集列表中

    # 使用sort方法对授权子集列表进行排序
    shouquanziji.sort(key=lambda x: compare([], x))

    # 获取授权子集的基底（没有其他子集是当前子集的真子集的子集）。通过比较子集之间的关系，去除列表中的非基本子集。
    i = 0
    while i < len(shouquanziji):
        j = 0
        while j < len(shouquanziji):
            if i == j:
                j += 1
                continue
            if ziji(shouquanziji[i], shouquanziji[j]):
                shouquanziji.pop(j)
                i = 0
                j = 0
            else:
                j += 1
        i += 1

    # 输出经处理的基底
    for subset in shouquanziji:
        print(*subset)
    print("#")

    # 查找未被授权的集合
    unshouquanziji = []
    for i in range(1, 1 << n):
        subset = [j + 1 for j in range(n) if i & (1 << j) > 0]
        if not shouquan(subset, shouquanziji):
            unshouquanziji.append(subset)

    # 查找最大未被授权的子集
    max_unshouquan = []   #存储找到的最大未被授权的子集
    for i, subset in enumerate(unshouquanziji):   #使用 enumerate 函数遍历未授权列表中的每个未被授权的子集，并为每个子集添加一个索引值 i
        max_subst = all(not ziji(subset, other) for j, other in enumerate(unshouquanziji) if j != i)  #使用列表推导式和 all 函数判断当前子集 subset 是否是未被授权的集合中的最大集合
        if max_subst:
            max_unshouquan.append(subset)

    # 获取最大未被授权的子集的补集
    complementary_set = []
    for subset in max_unshouquan:
        complementary = [i for i in range(1, n + 1) if i not in subset] #使用列表推导式，创建一个补集complementary。对于范围在 [1, n] 内的每个元素 i，如果 i 不在当前子集 subset 中，就将其加入到 suptmp 中。
        complementary_set.append(complementary)

    # 补集自然排序
    complementary_set.sort(key=lambda x: compare([], x))

    # 输出CDF
    for subset in complementary_set[::-1]:
        print(*subset)
    print("#")

    # 密钥分发
    secret_keys = [[] for _ in range(n)] #初始化，用于存储每个参与者收到的密钥。
    #遍历补集，分发密钥，secret_keys每个子列表包含了一个参与者收到的密钥编号
    for i, subset in enumerate(complementary_set, start=1):
        for key in subset:
            secret_keys[key - 1].append(i)

    # 分发规则
    for key in secret_keys[::-1]:
        print(*key)
    print("#")

if __name__ == "__main__":
    main()
