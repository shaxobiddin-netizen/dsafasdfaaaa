from xodimlar import (
    get_all_xodimlar,
    get_one_xodim,
    get_high_salary_xodimlar,
    xodim_statistics,
    top_xodim
)

print(" BARCHA XODIMLAR ")

xodimlar = get_all_xodimlar()

for emp in xodimlar:

    print(
        f"| {emp['name'].ljust(15)} "
        f"| {str(emp['salary']).ljust(10)} "
        f"| {emp['department'].ljust(10)} |"
    )

print()

print(" BIRTA XODIM ")
print(get_one_xodim(1))

print()

print(" YUQORI MAOSHLI XODIMLAR ")
print(get_high_salary_xodimlar(8000000))

print()

print(" STATISTIKA ")

stats = xodim_statistics()

print(
    f"""
Jami xodimlar: {stats['total_xodimlar']}
O'rtacha maosh: {stats['average_salary']}
Eng katta maosh: {stats['max_salary']}
"""
)

print()

print(" ENG KO'P MAOSH OLUVCHI ")
print(top_xodim())