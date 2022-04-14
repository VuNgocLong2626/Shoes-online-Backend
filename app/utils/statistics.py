from app.db.database import engine
import pandas as pd


def test():
    f = pd.read_sql_query(
        'SELECT * FROM bill b join bill_details bd on b.id_bill = bd.id_bill',
        engine
    )

    print(f)
