from db_config import get_connection


def insert_many_xodimlar():
    xodimlar_list = [
        ("Ali", "Dasturlash", 12000000, "ali@gmail.com"),
        ("Vali", "Marketing", 7500000, "vali@gmail.com"),
        ("Olim", "Dasturlash", 15000000, "olim@gmail.com"),
        ("Hasan", "Moliya", 11000000, "hasan@gmail.com"),
        ("Husan", "HR", 8000000, "husan@gmail.com"),
        ("Anvar", "Logistika", 7000000, "anvar2@gmail.com"),
        ("Sardor", "Dasturlash", 17000000, "sardor@gmail.com"),
        ("Nodira", "Moliya", 10500000, "nodira@gmail.com"),
        ("Madina", "Design", 9000000, "madina@gmail.com"),
        ("Bobur", "Logistika", 6500000, "bobur@gmail.com"),
    ]
    conn = get_connection()
    cursor = conn.cursor()
    yangi_id_lar = []
    query = "INSERT INTO xodimlar (ism, bo_lim, maosh, email) VALUES (%s, %s, %s, %s) RETURNING id;"
    for x in xodimlar_list:
        cursor.execute(query, x)
        yangi_id_lar.append(cursor.fetchone()[0])
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Yangi ID-lar: {yangi_id_lar}")


def upsert_xodim(ism, bo_lim, maosh, email):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO xodimlar (ism, bo_lim, maosh, email) VALUES (%s, %s, %s, %s)
        ON CONFLICT (email) DO UPDATE SET ism = EXCLUDED.ism;
    """
    cursor.execute(query, (ism, bo_lim, maosh, email))
    conn.commit()
    cursor.close()
    conn.close()


def get_all():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM xodimlar ORDER BY id;")
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res


def get_by_id(xodim_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM xodimlar WHERE id = %s;", (xodim_id,))
    res = cursor.fetchone()
    cursor.close()
    conn.close()
    return res


def create(ism, bo_lim, maosh, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO xodimlar (ism, bo_lim, maosh, email) VALUES (%s, %s, %s, %s);",
        (ism, bo_lim, maosh, email),
    )
    conn.commit()
    cursor.close()
    conn.close()


def update(xodim_id, yangi_ism, yangi_bo_lim, yangi_maosh):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE xodimlar SET ism=%s, bo_lim=%s, maosh=%s WHERE id=%s;",
        (yangi_ism, yangi_bo_lim, yangi_maosh, xodim_id),
    )
    conn.commit()
    cursor.close()
    conn.close()


def delete(xodim_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM xodimlar WHERE id = %s;", (xodim_id,))
    conn.commit()
    cursor.close()
    conn.close()


def create_xodim_with_project(ism, bo_lim, maosh, email, loyiha_nomi):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO xodimlar (ism, bo_lim, maosh, email) VALUES (%s, %s, %s, %s) RETURNING id;",
        (ism, bo_lim, maosh, email),
    )
    yangi_id = cursor.fetchone()[0]
    cursor.execute(
        "INSERT INTO loyihalar (loyiha_nomi, xodim_id) VALUES (%s, %s);",
        (loyiha_nomi, yangi_id),
    )
    conn.commit()
    cursor.close()
    conn.close()