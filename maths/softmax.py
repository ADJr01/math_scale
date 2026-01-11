import math

def soft_max(z_list:list[float])->list[float]:
    result:list[float] = []
    total:float = 0.0
    for i in z_list:
        calculated_value = math.e**i
        result.append(calculated_value)
        total = total + calculated_value

    for (index,item) in enumerate(result):
        result[index] = item/total
    return result

