list = ["Game of thrones  ", "Wheel of time", "Money Heist", "The Witcher"]


K = "o"


print("The original list : " + str(list))


res = [idx for idx, val in enumerate(list) if K in val]


print("The indices list : " + str(res))