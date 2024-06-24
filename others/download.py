import overpy
import pandas as pd
import psycopg2

# Initialize the Overpass API
api = overpy.Overpass()

# Define the query to get roads data for Sofia, Bulgaria
query = """
[out:json];
area[name="София"]->.searchArea;
way(area.searchArea)["highway"~"^(motorway|trunk|primary|secondary|tertiary|unclassified|residential|living_street|service|motorway_link|trunk_link|primary_link|secondary_link)$"];
out body;
>;
out skel qt;
"""

# Execute the query
result = api.query(query)

# Prepare data for a DataFrame
roads_data = []
for way in result.ways:
    node_coords = [(node.lon, node.lat) for node in way.nodes]
    if node_coords:  # Only process if there are nodes
        roads_data.append({
            "osmid": way.id,
            "u": way.nodes[0].id,
            "v": way.nodes[-1].id,
            "highway": way.tags.get("highway", "unknown"),
            "length": way.tags.get("length", "unknown"),  # Length is not directly available, needs calculation
            "geometry": f"LINESTRING({','.join([f'{lon} {lat}' for lon, lat in node_coords])})"
        })

# Create a DataFrame
df = pd.DataFrame(roads_data)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="",
    port=
)

cursor = conn.cursor()

# Create table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS geritoncheva1020_work.sofia_edges3 (
    osmid BIGINT,
    u BIGINT,
    v BIGINT,
    highway VARCHAR,
    length VARCHAR,
    geometry GEOMETRY
);
"""
cursor.execute(create_table_query)
conn.commit()

# Insert data into the table
for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO geritoncheva1020_work.sofia_edges3 (osmid, u, v, highway, length, geometry) VALUES (%s, %s, %s, %s, %s, ST_GeomFromText(%s, 4326))",
        (row['osmid'], row['u'], row['v'], row['highway'], row['length'], row['geometry'])
    )

conn.commit()
cursor.close()
conn.close()

print("Data imported successfully")
