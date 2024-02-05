name = str(input())
salary = float(input())
total_vendas = float(input())

comission = total_vendas * 0.15
final_salary = salary + comission

print(f"TOTAL = {final_salary:.2f}")