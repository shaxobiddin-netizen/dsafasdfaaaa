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

import xodimlar_crud


def menu():
    while True:
        print("\n1. Ko'rish\n2. Qo'shish\n3. Yangilash\n4. O'chirish\n5. Qidirish")
        print("6. Executemany\n7. UPSERT\n8. Tranzaksiya\n0. Chiqish")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            for x in xodimlar_crud.get_all():
                print(x)
        elif tanlov == "2":
            xodimlar_crud.create(
                input("Ism: "),
                input("Bo'lim: "),
                float(input("Maosh: ")),
                input("Email: "),
            )
        elif tanlov == "3":
            xodimlar_crud.update(
                int(input("ID: ")),
                input("Yangi Ism: "),
                input("Yangi Bo'lim: "),
                float(input("Yangi Maosh: ")),
            )
        elif tanlov == "4":
            xodimlar_crud.delete(int(input("ID: ")))
        elif tanlov == "5":
            print(xodimlar_crud.get_by_id(int(input("ID: "))))
        elif tanlov == "6":
            xodimlar_crud.insert_many_xodimlar()
        elif tanlov == "7":
            xodimlar_crud.upsert_xodim(
                input("Ism: "),
                input("Bo'lim: "),
                float(input("Maosh: ")),
                input("Email: "),
            )
        elif tanlov == "8":
            xodimlar_crud.create_xodim_with_project(
                input("Ism: "),
                input("Bo'lim: "),
                float(input("Maosh: ")),
                input("Email: "),
                input("Loyiha: "),
            )
        elif tanlov == "0":
            break


if __name__ == "__main__":
    menu()