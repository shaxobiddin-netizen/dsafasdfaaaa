from db_config import get_connection
from psycopg2.extras import RealDictCursor


def get_all_xodimlar():

    with get_connection() as conn:
        with conn.cursor(
            cursor_factory=RealDictCursor
        ) as cur:

            cur.execute(
                "SELECT * FROM xodimlar"
            )

            return cur.fetchall()


def get_one_xodim(emp_id):

    with get_connection() as conn:
        with conn.cursor(
            cursor_factory=RealDictCursor
        ) as cur:

            cur.execute(
                """
                SELECT * FROM xodimlar WHERE id = %s
                """,
                (emp_id,)
            ) #SELECT * FROM xodimlar WHERE id = emp_id 

            return cur.fetchone()


def get_high_maosh_xodimlar(limit_maosh):

    with get_connection() as conn:
        with conn.cursor(
            cursor_factory=RealDictCursor
        ) as cur:

            cur.execute(
                """
                SELECT *
                FROM xodimlar
                WHERE maosh > %s
                """,
                (limit_maosh,)
            )

            return cur.fetchall()


def xodim_statistics():

    with get_connection() as conn:
        with conn.cursor(
            cursor_factory=RealDictCursor
        ) as cur:

            cur.execute(
                """
                SELECT
                    COUNT(*) as total_xodimlar,
                    AVG(maosh) as average_maosh,
                    MAX(maosh) as max_maosh
                FROM xodimlar
                """
            )

            return cur.fetchone()


def top_xodim():

    with get_connection() as conn:
        with conn.cursor(
            cursor_factory=RealDictCursor
        ) as cur:

            cur.execute(
                """
                SELECT *
                FROM xodimlar
                ORDER BY maosh DESC
                LIMIT 1
                """
            )

            return cur.fetchone()