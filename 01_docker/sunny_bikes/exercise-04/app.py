import os
from time import sleep
from uuid import uuid4

import psycopg2 as postgres
from flask import Flask, request, render_template

max_retry_count = 20
counter = 0
while counter < max_retry_count:
    counter += 1
    try:
        print(f"Attempt database connection #{counter}")
        conn = postgres.connect(
            host=os.environ.get("PG_HOST", "postgres"),
            port=int(os.environ.get("PG_PORT", "5432")),
            user=os.environ.get("PG_USER", "postgres"),
            password=os.environ["PG_PASSWORD"],
            dbname=os.environ.get("PG_DATABASE", "postgres"),
        )
        break
    except Exception as e:
        if counter >= max_retry_count:
            print("Database connection max tries, aborting.")
            exit(1)

        print("Database connection failed, sleeping...")
        sleep(2)


app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    with conn.cursor() as cur:
        cur.execute(
            "SELECT name, location, created "
            "FROM public.bike_rides "
            "ORDER BY created DESC"
        )
        rows = cur.fetchall()
        return render_template(
            template_name_or_list="list_bike_rides.html",
            rides=[
                dict(name=row[0], location=row[1], created=row[2].isoformat())
                for row in rows
            ],
        )


@app.route("/rent", methods=["GET"])
def insert_rental():
    """
    Insert with http://localhost:8080/rent?name=bas&location=test
    :return:
    """
    name = request.args.get("name")
    location = request.args.get("location")

    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO public.bike_rides (uuid, name, location, created) "
            f"VALUES ('{str(uuid4())}', '{name}', '{location}', 'now()')"
        )
    conn.commit()
    return "OK"


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
