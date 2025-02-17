# Get user input for the appliance name and cost
appliance_name = input("Enter the name of the appliance: ")
appliance_cost = float(input("Enter the cost of the appliance: "))
# Determine warranty cost based on price
warranty_cost = appliance_cost * 0.10 if appliance_cost > 1000 else appliance_cost * 0.05
# Calculate total cost (appliance + warranty)
total_cost = appliance_cost + warranty_cost
# Display results
print("\nAppliance Name: {}".format(appliance_name))
print("Appliance Cost: ${:.2f}".format(appliance_cost))
print("Warranty Cost: ${:.2f}".format(warranty_cost))
print("Total Cost: ${:.2f}".format(total_cost))
