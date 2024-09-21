# from stats import discount

class Microwave :
    def __init__(self, brand:str,power:str,cost:float) -> None:
        self.brand =brand
        self.power=power
        self.cost=cost
    ...

lg: Microwave= Microwave(brand='LG',power='B',cost=1000) #LG based microwave
bosh: Microwave=Microwave(brand='bosh',power='A',cost=100)
# discount_for_dress,_=discount.Cal_dicount_for_dress(100.232)
total_bosh=bosh.cost+0.30
total_lg=lg.cost+0.3

print(f"Total cost to but{bosh.brand}is = {total_bosh}")
print(f"power rating of {bosh.brand} microwave = {bosh.power}")
# print(f"discount for dress ={discount_for_dress}")
print(lg.brand)