weight = 41.5

# Ground Shipping

if weight <= 2:
  cost = 1.5 * weight + 20
elif weight <= 6:
  cost = 3.0 * weight + 20
elif weight <= 10:
  cost = 4.0 * weight + 20
else:
  cost = 4.75 * weight + 20

# Drone Shipping

if weight <= 2:
  drone_cost = 4.5 * weight
elif weight <= 6:
  drone_cost = 9.0 * weight
elif weight <= 10:
  drone_cost = 12.0 * weight
else:
  drone_cost = 14.25 * weight

print("Ground shipping price:", cost)
print("Ground Shipping Premium price: 125")
print("Drone Shipping price:", drone_cost)