import psycopg2
import json
from geojson import loads

# PostgreSQL connection parameters
dbname = ''
user = ''
password = ''
host = ''
port = 

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    # Read GeoJSON from file with UTF-8 encoding
    with open('data.geojson', 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    # Insert data into PostgreSQL
    for feature in geojson_data['features']:
        properties = feature['properties']
        geometry = json.dumps(feature['geometry'])
        id = properties['id']
        address = properties['ref']

        # Construct and execute the SQL query
        sql = "INSERT INTO geritoncheva1020_work.sofia_edges4 (Id, Geometry, Address) VALUES (%s, ST_SetSRID(ST_GeomFromGeoJSON(%s), 4326), %s);"
        cursor.execute(sql, (id, geometry, address))

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted successfully!")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL or inserting data:", error)
finally:
    # Closing database connection.
    if conn:
        conn.close()