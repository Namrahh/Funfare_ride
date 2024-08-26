print("Welcome the the roller coaster funfare!")
height =int(input("What is your height in cm?"))


if height > 120:
  print("You can ride the roller coaster")
  age = int(input("For payment kindly tell your age?"))
  if age < 12:
    print("Please pay $5")
  elif age <=18:
    print("Please pay $7")

  else:
    print("Please pay $12")

else:
  print("Sorry you've to grow taller before you can ride.")