select * from geritoncheva1020_work.kurieri_all_2018 where tradename like '%Econt%' or  tradename like '%Еконт%';
CREATE TABLE geritoncheva1020_work.Econt
  AS (SELECT *
      from geritoncheva1020_work.kurieri_all_2018 where tradename like '%Econt%' or  tradename like '%Еконт%');

select * from geritoncheva1020_work.Econt;

SELECT ST_AsGeoJSON(geom) as geometry, address FROM geritoncheva1020_work.econt

CREATE TABLE geritoncheva1020_work.Econt2
  AS (SELECT ST_Transform(geom, 'EPSG:7801', 'EPSG:4326') as geom, address
      from geritoncheva1020_work.kurieri_all_2018 where tradename like '%Econt%' or  tradename like '%Еконт%');
      
ALTER TABLE geritoncheva1020_work.Econt2 
ALTER COLUMN geom TYPE geometry(MultiPoint, 4326) 
USING ST_SetSRID(geom, 4326);


drop table geritoncheva1020_work.Econt

UPDATE geritoncheva1020_work.Econt2 
SET geom = ST_Transform(geom, 'EPSG:7801', 'EPSG:4326');

UPDATE geritoncheva1020_work.Econt2 
SET geom = 
ST_Transform(geom,  'EPSG:4326')


drop table geritoncheva1020_work.Econt2

CREATE TABLE geritoncheva1020_work.Econt2
  AS (SELECT ST_Transform(geom, 'EPSG:7801', 'EPSG:4326') as geom, address
      from geritoncheva1020_work.kurieri_all_2018 where tradename like '%Econt%' or  tradename like '%Еконт%');
      

UPDATE geritoncheva1020_work.Econt2
SET address = REPLACE(address, '"""', '');

CREATE TABLE geritoncheva1020_work.municipality_roads_api
  AS (SELECT ST_Transform(geom, 'EPSG:7801', 'EPSG:4326') as geom, road_categ, road_name
      from municipality_roads_api);
   

select * from geritoncheva1020_work.sofia_edges ;

SELECT ST_AsGeoJSON(geometry) as geometry FROM geritoncheva1020_work.sofia_edges
