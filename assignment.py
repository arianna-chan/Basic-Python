def savings(gross_pay, tax_rate, expenses):
    after_tax_pay = int(gross_pay * (1 - tax_rate))
    savings = after_tax_pay - expenses
    return savings

def material_waste(total_material, material_units, num_jobs, job_consumption):
    waste = num_jobs * job_consumption
    remaining_material = total_material - waste
    result = f"{remaining_material}{material_units}"
    return result

def interest(principal, rate, periods):
    final_value = int(principal + (principal * rate * periods))
    return final_value

def body_mass_index(weight, height):
    weight_kg = weight * 0.453592
    height_m = (height[0] * 0.3048) + (height[1] * 0.0254)
    bmi = weight_kg / (height_m ** 2)
    return bmi

result1 = savings(100000, 0.2, 3000)
print("Result of savings:", result1)

result2 = material_waste(1000, "kg", 5, 20)
print("Result of material_waste:", result2)

result3 = interest(1000, 0.05, 3)
print("Result of interest:", result3)

result4 = body_mass_index(160, [5, 10])
print("Result of body_mass_index:", result4)

