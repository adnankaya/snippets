import psycopg2
import os

DBNAME = os.environ.get('DB_NAME')


class StopUserApiException(Exception):
    pass


def userapi():
    conn = psycopg2.connect(f'dbname={DBNAME} user=postgres password=postgres')
    output = 'Send a query or None to quit!'
    while query := (yield output):
        curr = conn.cursor()
        qs = 'SELECT username, is_active FROM auth_user WHERE {}'.format(query)
        print(qs)

        curr.execute(qs)

        try:
            for single_record in curr.fetchall():
                yield single_record
        except StopUserApiException:
            continue
