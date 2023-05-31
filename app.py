import math
def form(num_1, num_2, num_3):
        d = (num_2 * num_2) - 4 * num_1 * num_3
        if d == 0:
            ans = []
            ans.append(-num_2/2*num_1)
            return ans
        elif d < 0:
            return 'err'
        else:
            ans1 = []
            ans1.append((-num_2 + math.sqrt(d)) / (2 * num_1))
            ans1.append((-num_2 - math.sqrt(d)) / (2 * num_1))
            return ans1

