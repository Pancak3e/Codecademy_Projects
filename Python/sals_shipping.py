#v.1.0 
#Sal's Shipping is a coding project from Codecademy
#
#
# Sal's Shipping takes a value supplied at the weight variable
# and computes which of the three options of shipping is the
# for your package.
#
# This current project was coded by Pancak3e a.k.a sys4dmin
# The shipping rates, project name and project idea were all
# supplied by Codecademy
#
#
#BEGIN
#
#
#change weight here, to identify which shipping option is cheapest
weight = 0

#ground_shipping
def ground_shipping(weight):
  cost = 0
  flat_charge = 20
  if weight > 0 and weight <= 2:
    cost += (weight * 1.50) + flat_charge
    return cost
  elif weight > 2 and weight <= 6:
    cost += (weight * 3) + flat_charge
    return cost
  elif weight > 6 and weight <= 10:
    cost += (weight * 4) + flat_charge
    return cost
  elif weight > 10:
    cost += (weight * 4.75) + flat_charge
    return cost
  else:
    return "Error: Enter a Valid Weight"

#drone_shpping
def drone_shipping(weight):
  cost = 0
  flat_charge = 0
  if weight > 0 and weight <= 2:
    cost += (weight * 4.50) + flat_charge
    return cost
  elif weight > 2 and weight <= 6:
    cost += (weight * 9) + flat_charge
    return cost
  elif weight > 6 and weight <= 10:
    cost += (weight * 12) + flat_charge
    return cost
  elif weight > 10:
    cost += (weight * 14.25) + flat_charge
    return cost
  else:
    return "Error: Enter a Valid Weight"

ground = ground_shipping(weight)
premium_ground = 125
drone = drone_shipping(weight)

def cheapest_shipping(ground, premium_ground, drone):
  if ground < premium_ground and ground < drone:
    return "Ground shipping at a rate of $" + str(ground)
  elif premium_ground < ground and premium_ground < drone:
    return "Premium Ground at a rate of $" + str(premium_ground)
  elif drone < ground and drone < premium_ground:
    return "Drone shipping at a rate of $" + str(drone)
  else:
    return "Error: Enter a Valid Weight"

cheapest_shipping_option = cheapest_shipping(ground, premium_ground, drone)

print("The cheapest option for shipping your package is " + str(cheapest_shipping_option))
#
#
#END
