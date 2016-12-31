import numpy as np

def market_equilibrium(initial_market_share, switch_probability):
    error =1
    # take the column value in switch_probability
    switch_probability_t = [list(x) for x in zip(*switch_probability)]

    while error >0.00001:
        res=[]
        for i in range(len(switch_probability_t)):
            prod=sum([x*y for x,y in zip(initial_market_share,switch_probability_t[i])])
            res.append(prod)
        error = sum([(x-y)**2 for x,y in zip(initial_market_share,res)])**0.5
        initial_market_share=res

    return [round(x,4)  for x in initial_market_share]


def main():
    a=[0.4,0.6]
    b=[[0.8,0.2],[0.1,0.9]]

    sln=market_equilibrium(a,b)
    print(sln)

if __name__=="__main__":
    main()