from random import randint


def maior(nums:list):
    maior = nums[0]
    indice = 0
    for c in range(len(nums)):
        if(nums[c] > maior):
            maior = nums[c]
            indice = c
        print(f"{nums[c]}", end="-")
        if (c == len(nums)-1):
            print(f"{nums[c]}")
    print(f"\n\nMaior numero = {maior}\nIndice = {indice}")


nums = list()
for c in range(0,20):
    nums.append(randint(1, 100))
maior(nums)

