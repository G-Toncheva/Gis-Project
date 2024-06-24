const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');
const app = express();
const port = 3000;

const pool = new Pool({
    user: '',
    host: '',
    database: '',
    password: '',
    port: ,
});

app.use(cors());

app.get('/api/points', async (req, res) => {
    try {
        const result = await pool.query('SELECT ST_AsGeoJSON(geom) as geometry, address FROM geritoncheva1020_work.Econt2');
        res.json(result.rows);
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});


app.get('/api/roads', async (req, res) => {
  try {
      const result = await pool.query('SELECT id, ST_AsGeoJSON(geometry) AS geometry FROM geritoncheva1020_work.sofia_edges4');
      const roadData = result.rows.map(row => ({
          id: row.id,
          geometry: JSON.parse(row.geometry),
      }));
      res.json(roadData);
  } catch (err) {
      console.error(err);
      res.status(500).json({ error: 'Internal server error' });
  }
});


app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
