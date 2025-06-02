# This script gives advice based on the weather input
weather = input("What's the weather like today? (sunny/rainy/cold):. ").lower()

# Check the weather and provide advice using match case
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")


# Check the weather and provide advice using match case
# match weather:
#     case "sunny":
#         print("Wear a t-shirt and sunglasses.")
#     case "rainy":
#         print(" Don't forget your umbrella and raincoat.")
#     case "cold":
#         print(" Make sure to wear a warm coat and a scarf..")
#     case _:
#         print(" Sorry, I don't have recommendations for this weather.")
