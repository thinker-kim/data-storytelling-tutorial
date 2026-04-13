# A Data Storytelling Tutorial: Making Climate Data Visible with Streamlit

Turn climate data into meaningful stories with Python, Altair, and Streamlit.

<br>

## Overview

This tutorial provides a structured, hands-on guide to creating compelling data-driven stories. Using climate data such as temperature trends, it guides learners from raw datasets to interactive visualizations and clear narratives, communicating change, context, and significance.

<br>

## Tutorial Structure

<table>
  <tr>
    <td width="25%"><b>Category</b></td>
    <td width="37.5%"><b>Part 1 · Data Analysis & Visualization</b></td>
    <td width="37.5%"><b>Part 2 · Interactive Dashboard & Deployment</b></td>
  </tr>
  <tr>
    <td><b>Duration</b></td>
    <td>~1.5 hours</td>
    <td>~1.5 hours</td>
  </tr>
  <tr>
    <td><b>Level</b></td>
    <td>Beginner to Intermediate</td>
    <td>Beginner to Intermediate</td>
  </tr>
  <tr>
    <td><b>Focus</b></td>
    <td>Explore data, build charts, craft a narrative (Hook → Evidence → Meaning)</td>
    <td>Turn the narrative into a live online dashboard and deploy it for free</td>
  </tr>
  <tr>
    <td><b>Prerequisites</b></td>
    <td>Basic Python and pandas<br>Familiarity with data tables</td>
    <td>Part 1 completion<br>A free GitHub account</td>
  </tr>
</table>

<br>

## Tutorial Walkthrough Video

A walkthrough video for this tutorial is available here:

👉 [Watch the tutorial video]()

<br>

## What You'll Create

<table>
<tr><td><b>Time Series Analysis</b></td><td>Detect trends and patterns in historical temperature data</td></tr>
<tr><td><b>Warming Stripes</b></td><td>Recreate Ed Hawkins' iconic climate visualization</td></tr>
<tr><td><b>Decade Comparisons</b></td><td>Analyze how warming has accelerated over time</td></tr>
<tr><td><b>Interactive Dashboard</b></td><td>Build a Streamlit app with user controls and tabbed charts</td></tr>
<tr><td><b>Auto-Generated Stories</b></td><td>Create dynamic narratives that update with user selections</td></tr>
<tr><td><b>Live Deployment</b></td><td>Publish to Streamlit Community Cloud with a shareable URL</td></tr>
</table>

<br>

## Dataset

Data provided by [Berkeley Earth Surface Temperature Study](https://berkeleyearth.org/)

<table>
<tr>
<td><b>Records</b></td>
<td><b>Countries</b></td>
<td><b>Time Span</b></td>
</tr>
<tr>
<td>333,193</td>
<td>233</td>
<td>1900 – 2020</td>
</tr>
</table>

<br>

### Schema

<table>
<tr><td><code>Years</code></td><td>Year of observation</td></tr>
<tr><td><code>Month</code></td><td>Month (1-12)</td></tr>
<tr><td><code>Country</code></td><td>Country name</td></tr>
<tr><td><code>Temperature</code></td><td>Absolute temperature (°C)</td></tr>
<tr><td><code>Anomaly</code></td><td>Observed Temperature − Baseline Average (1951–1980, per country/month) (°C)</td></tr>
</table>

<br>

## Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/data-storytelling-tutorial.git
cd data-storytelling-tutorial

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

<br>

## Project Structure

```
data-storytelling-tutorial/
├── PART1_TUTORIAL.ipynb          ← Data analysis & storytelling
├── PART2_TUTORIAL.ipynb          ← Dashboard building & deployment
├── app.py                        ← Complete Streamlit dashboard
├── requirements.txt
├── data/
│   └── ddbb_surface_temperature_countries.csv
├── output/                       ← Charts and CSVs from Part 1
└── README.md
```

<br>

## Curriculum

### Part 1 · Climate Data Storytelling

<table>
<tr><td>1</td><td>Introduction to data storytelling and temperature anomalies</td></tr>
<tr><td>2</td><td>Environment setup with Python and Jupyter</td></tr>
<tr><td>3</td><td>Data exploration with pandas</td></tr>
<tr><td>4</td><td>Time series analysis — trends, moving averages, decades</td></tr>
<tr><td>5</td><td>Finding stories — extremes, comparisons, patterns</td></tr>
<tr><td>6</td><td>Altair fundamentals — declarative visualization</td></tr>
<tr><td>7</td><td>Advanced charts — warming stripes, heatmaps</td></tr>
<tr><td>8</td><td>Narrative structure — Hook → Evidence → Meaning</td></tr>
<tr><td>9</td><td>Export workflows — HTML, CSV</td></tr>
</table>

### Part 2 · Interactive Dashboard & Deployment

<table>
<tr><td>1</td><td>Map the Part 1 storyline (Hook → Evidence → Meaning) to a dashboard layout</td></tr>
<tr><td>2</td><td>Set up the project structure for Streamlit</td></tr>
<tr><td>3</td><td>Build the data layer with caching</td></tr>
<tr><td>4</td><td>Create sidebar controls — country selector, year slider, toggles</td></tr>
<tr><td>5</td><td>Build the Hook — metric cards showing key numbers</td></tr>
<tr><td>6</td><td>Build the Evidence — tabbed charts (time series, warming stripes, decades)</td></tr>
<tr><td>7</td><td>Build the Meaning — auto-generated narrative and Paris Agreement tracker</td></tr>
<tr><td>8</td><td>Add data download functionality</td></tr>
<tr><td>9</td><td>Assemble the complete app.py</td></tr>
<tr><td>10</td><td>Deploy to Streamlit Community Cloud (free)</td></tr>
<tr><td>11</td><td>Optional extensions — multi-country comparison, custom narratives</td></tr>
</table>

<br>

## Learning Outcomes

<table>
<tr>
<td width="33%">

**Technical**

Manipulate time series data with pandas. Calculate statistical trends and moving averages. Design professional visualizations with Altair. Build and deploy interactive web applications with Streamlit.

</td>
<td width="33%">

**Storytelling**

Identify compelling narratives in datasets. Structure data stories as Hook → Evidence → Meaning. Generate dynamic narrative text from data. Select appropriate visualizations for your message.

</td>
<td width="33%">

**Domain**

Understand temperature anomaly methodology. Interpret warming trends and regional patterns. Contextualize data with Paris Agreement targets.

</td>
</tr>
</table>

<br>

## Tech Stack

<table>
<tr>
<td><b>Python</b></td>
<td><b>pandas</b></td>
<td><b>Altair</b></td>
<td><b>Streamlit</b></td>
<td><b>NumPy</b></td>
<td><b>SciPy</b></td>
</tr>
<tr>
<td>Core language</td>
<td>Data manipulation</td>
<td>Visualization</td>
<td>Web apps & deployment</td>
<td>Numerical</td>
<td>Statistics</td>
</tr>
</table>

<br>

## Key Concepts

### Temperature Anomaly

```
Anomaly = Observed Temperature − Baseline Average
```

The baseline period is typically 1951–1980. Positive values indicate warmer-than-average conditions; negative values indicate cooler-than-average. Anomalies enable comparison across different regions, highlight change rather than absolute values, and follow scientific convention.

### Paris Agreement Targets

<table>
<tr><td><b>1.5°C</b></td><td>Preferred limit above pre-industrial levels</td></tr>
<tr><td><b>2.0°C</b></td><td>Upper limit to prevent catastrophic impacts</td></tr>
</table>

### Dashboard Story Structure

```
┌─────────────────────────────────────────┐
│  HOOK          Metric cards at top      │
├─────────────────────────────────────────┤
│  EVIDENCE      Tabbed charts            │
│                 ├─ Time Series          │
│                 ├─ Warming Stripes      │
│                 └─ Decade Bars          │
├─────────────────────────────────────────┤
│  MEANING       Auto-generated narrative │
│                 + Paris Agreement bar   │
├─────────────────────────────────────────┤
│  ACTION        Download data button     │
└─────────────────────────────────────────┘
```

<br>

## Deployment

### Streamlit Community Cloud (Free)

1. Push to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app" → select repository → select `app.py`
5. Deploy

Your dashboard will be available at a public URL within minutes.

<br>

## Resources

<table>
<tr>
<td><b>Data</b></td>
<td><a href="https://berkeleyearth.org/data/">Berkeley Earth</a> · <a href="https://data.giss.nasa.gov/gistemp/">NASA GISS</a> · <a href="https://www.climate.gov/maps-data">NOAA Climate</a></td>
</tr>
<tr>
<td><b>Docs</b></td>
<td><a href="https://altair-viz.github.io/">Altair</a> · <a href="https://docs.streamlit.io/">Streamlit</a> · <a href="https://pandas.pydata.org/docs/">pandas</a></td>
</tr>
<tr>
<td><b>Deployment</b></td>
<td><a href="https://share.streamlit.io/">Streamlit Community Cloud</a> · <a href="https://docs.streamlit.io/deploy/streamlit-community-cloud">Deployment Docs</a></td>
</tr>
<tr>
<td><b>Inspiration</b></td>
<td><a href="https://showyourstripes.info/">Show Your Stripes</a> · <a href="https://ourworldindata.org/climate-change">Our World in Data</a></td>
</tr>
</table>

<br>

## Citation

```
Berkeley Earth Surface Temperature Study
http://berkeleyearth.org/

Rohde, R. A. and Hausfather, Z.: The Berkeley Earth Land/Ocean Temperature Record,
Earth Syst. Sci. Data, 12, 3469–3479, https://doi.org/10.5194/essd-12-3469-2020, 2020.
```

<br>

---

<p align="center">
<sub>Built for climate awareness</sub>
</p>
