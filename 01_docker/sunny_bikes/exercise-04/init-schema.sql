CREATE TABLE public.bike_rides (
    uuid UUID PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    location VARCHAR(80) NOT NULL,
    created TIMESTAMPTZ NOT NULL
)