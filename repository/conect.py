
import psycopg2
from psycopg2.extras import RealDictCursor



DATABASE_URL = "postgresql://tms:L8RPvApI7wAfyUNA7rv8aXpExM6qrnFD@dpg-db8vbce7bikc73bdo8v0-a.virginia-postgres.render.com/tms_project_s9vw"

try:
    conn = psycopg2.connect(
        DATABASE_URL,
        cursor_factory=RealDictCursor,
        sslmode="require"
    )

    cur = conn.cursor()

    print("Connected to Render PostgreSQL successfully!")

except psycopg2.Error as e:
    print(f"Database connection failed: {e}")
    raise
