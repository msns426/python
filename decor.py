def offer_price(func):
    def discount_price():
        func()
        print("your saving almost 20000")
        print("Congratulations to got this offer")
    return discount_price


@offer_price
def normal_fun():
    print("mobile name is : nokia")
    print("mobile base price is :50000")
    print("only one  piece available")


normal_fun()



