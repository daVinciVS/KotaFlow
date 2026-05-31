# KotaFlow

A ride-hailing demand heatmap and insights analyzer focused on three Indonesian cities: Jakarta, Yogyakarta, and Surabaya. Built to replicate the kind of operational analytics a city operations team would run to understand demand patterns, peak hours, and supply gaps.

---

## Business Context

Ride-hailing platforms operating in Indonesia face a core operational challenge: demand is highly uneven across time and geography. Morning and evening commute spikes, weekend tourism surges, and weather-driven demand jumps all create windows where supply falls short and wait times spike.

KotaFlow provides a self-contained analytical workflow to identify these patterns using interactive heatmaps, time-series visualizations, and a structured internal report — all runnable locally with no deployment required.

---

## Key Findings

| Finding | Detail |
|---------|--------|
| Bi-modal peaks | Morning 07–09 and evening 17–20 account for 60–70% of daily volume across all cities |
| Weekend midday shift | Demand moves to 10–14 on weekends; Yogyakarta shows +30% uplift driven by tourism |
| Rain premium | Rainy conditions increase demand 20–35%; Jakarta is most weather-sensitive |
| Worst supply gap | 08:00 and 18:00 show the largest unmet demand; Surabaya industrial zones most affected |
| City scale difference | Jakarta average demand is 2.6x Yogyakarta and 1.4x Surabaya |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| Pandas / NumPy | Data manipulation and simulation |
| Folium | Interactive demand heatmaps |
| Matplotlib / Seaborn | Static charts and EDA visualizations |
| Jupyter Notebook | Interactive analysis environment |

---

## Folder Structure

KotaFlow/
├── data/
│ └── kotaflow_rides.csv # Simulated dataset (18,000 rides, 3 cities)
├── notebooks/
│ └── kotaflow_analysis.ipynb # Main analysis notebook
├── outputs/
│ ├── heatmaps/ # Folium HTML heatmaps per city
│ └── charts/ # PNG chart exports
├── src/
│ ├── _init_.py
│ └── utils.py # Shared helper functions
├── generate_data.py # Dataset generation script
├── requirements.txt
└── .gitignore

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
