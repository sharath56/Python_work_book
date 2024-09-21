# import numpy as np
# from class_main import Microwave
import math


class discount:

    def __init__(self,orginal_price:float,discount_percentage:float,Final_price:float,discount_amount:float) -> None:
        self.orginal_price = orginal_price
        self.discount_percentage=discount_percentage
        self.Final_price = Final_price
        self.discount_amount=discount_amount
        pass
    ...

    def Cal_dicount_for_dress(self):
        self.discount_amount=self.orginal_price*self.discount_percentage/100
        self.Final_price=self.orginal_price-self.discount_amount
        return self.Final_price,self.discount_amount
        

# discount_dress: discount= discount()