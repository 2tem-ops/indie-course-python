print(f"Current dollar rate is {(rate := float(input()))}. You want to buy {(amount := int(input()))} dollars",
      f"You must pay {rate * amount}",
      sep="\n")