'''
Diminishing value colored balls
'''

def coloredBalls(orders,inventory):
    inventory = sorted(inventory,reverse=True)
    inventory += [0]
    result = 0
    k = 1

    for i in range(len(inventory)-1):
        if inventory[i]>inventory[i+1]:
            if k*(inventory[i]-inventory[i+1])<orders:
                difference = inventory[i]-inventory[i+1]
                result += k*(inventory[i]+inventory[i+1]+1)*difference//2
                orders -= k*difference

            else:
                q,r = divmod(orders,k)
                result += k*(inventory[i]+(inventory[i]-q+1))*q//2
                result += r*(inventory[i]-q)
                return result%(10**9+7)

        k+=1


inventory = [2,8,4,10,6]
orders = 20
print(coloredBalls(orders,inventory))
