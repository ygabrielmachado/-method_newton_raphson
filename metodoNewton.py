
def newtonMethod():
    amount_spots = int(input('Number of spots:'))
    spots, f_spots = [], []
    chart = []
    for i in range(amount_spots):
        spot = float(input('x%d =' %i))
        f_spot = float(input('x%d =' %i))
        spots.append(spot)
        f_spots.append(f_spot)
    chart.append(f_spots)
    
    x = float(input('\nPoint x to be estimated:'))
    
    step = 1
    for n in range (amount_spots -1):
        order = []
        for m in range(len(chart[n]) - 1):
            divided_difference = (chart[n][m+1]-chart[n][m])/(spots[m+step] - spots[m])
            order.append(divided_difference)
        chart.append(order)
        step += 1
    for k in range(len(chart)):
        print('Order %d'%k, chart[k])

    approach = 0
    rate = 0

    for i in range(len(chart)):
        coefficient = chart[i][0]
        for j in range(rate):
            coefficient *=(x-spots[j])
        rate += 1
        approach += coefficient
    print('\nApproach found for f(%f) = %f'%(x, approach))

if __name__ == '__main__':
    newtonMethod()