# Sal's Shipping Costs - Flow conntrol lesson Project.

ground_ship_flat = 20.00
premium_ground_flat = 120.00
drone_ship_flat = 0.00
weight = 41.5

def ground_shipping(weight):
  if weight <= 2:
    return (1.50 * weight) + ground_ship_flat
  elif weight <= 6:
    return (3.00 * weight) + ground_ship_flat
  elif weight <= 10:
    return (4.00 * weight) + ground_ship_flat
  else:
    return (4.75 * weight) + ground_ship_flat
  

def drone_shipping(weight):
  if weight <= 2:
    return (4.50 * weight) + drone_ship_flat
  elif weight <= 6:
    return (9.00 * weight) + drone_ship_flat
  elif weight <= 10:
    return (12.00 * weight) + drone_ship_flat
  else:
    return (14.25 * weight) + drone_ship_flat

def cheapest_shipping(weight):
  if (ground_shipping(weight) < drone_shipping(weight)) and (ground_shipping(weight) < 125):
    return "The cheapest option is ground shipping. Price : $" + str(ground_shipping(weight))
  elif (ground_shipping(weight)) > drone_shipping(weight) and (drone_shipping(weight < 125)):
    return "The cheapest option is drone shipping. Price: $" + str(drone_shipping(weight))
  else:
    return "The best option is our Premium ground shipping service. Price: $ " + str(premium_ground_flat)
  
print(cheapest_shipping(weight))

  