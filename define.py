def happy_bday(name,age):
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old!")
    print("Happy bday!")

happy_bday("Julie",25)
happy_bday("Graoo",25)
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1+tax)
print(net_price(500))
print(net_price(500, 0.5))
print(net_price(500, 0, 0.10))
  