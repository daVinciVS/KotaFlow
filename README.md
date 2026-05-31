
---

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/daVinciVS/KotaFlow.git
cd KotaFlow
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Generate the dataset**

```bash
python generate_data.py
```

This produces `data/kotaflow_rides.csv` with 18,000 simulated ride records across Jakarta, Yogyakarta, and Surabaya. Pickup coordinates are clustered around real landmarks including Malioboro, Sudirman, Tunjungan Plaza, and Soekarno-Hatta Airport.

**4. Open the notebook**

```bash
python -m jupyterlab
```

Navigate to `notebooks/kotaflow_analysis.ipynb` and run all cells top to bottom.

---

## Output Examples

- `outputs/heatmaps/heatmap_jakarta.html` — Interactive pickup density map for Jakarta
- `outputs/heatmaps/heatmap_yogyakarta.html` — Interactive pickup density map for Yogyakarta
- `outputs/heatmaps/heatmap_surabaya.html` — Interactive pickup density map for Surabaya
- `outputs/charts/peak_hour_analysis.png` — Hourly demand curves with peak period shading
- `outputs/charts/supply_demand_gap.png` — Supply vs demand gap per city
- `outputs/charts/heatmap_dow_hour.png` — Day-of-week by hour demand heatmap

---

## Disclaimer

This project uses a simulated dataset generated with realistic statistical patterns based on publicly known urban geography of Indonesian cities. Hotspot coordinates reference real landmarks but demand volumes are entirely synthetic. This is intended for portfolio and educational purposes only.

---

## License

MIT License
