weather = input("What's the weather like today?(sunny/rainy/cold): ")
if weather == "sunny":
    print("recommendation:wear a t-shirt and sunglass")
elif weather == "rainy":
    print("recommendation: don't forget your umbrella and raincoat")
elif weather == "cold":
    print("recommendation: make sure to wear a warm coat and a scarf.")
else:
    print("sorry, i don't have a recommendation for this weather")
