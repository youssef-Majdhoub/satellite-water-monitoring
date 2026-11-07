# PFA2027 - Water Anomaly Detection (Nabeul, Tunisia)

This repository contains the code for detecting water pollution and abstraction anomalies in Nabeul using Satellite Data (Sentinel-1 & Sentinel-2).

## ⚠️ Prerequisites

- **Python:** Requires **Python 3.10 or higher**.
- **VS Code:** [Visual Studio Code](https://code.visualstudio.com/).

---

## 🚀 First Time Setup

1. Open VS Code, go to `File` > `Open Folder...` and select the `PFA2027` folder.
2. Open the file **`setup_environment.py`**.
3. Click the **Play button** ▶️ in the top right corner.

**What it does:** It creates the `.venv` folder and installs all the required libraries.
_(Note: If VS Code asks you to select an interpreter, select the one that says `.venv`)_.

---

## 🛰️ Data Harvest Workflow

Our data harvesting strategy uses a two-step approach: **Visual Exploration** followed by **Automated Harvesting**.

### Phase 1: Lock in the Location (Copernicus Browser)

Before writing any code, we need to know exactly where we are looking and what the data looks like.

1. Go to the [Copernicus Browser](https://browser.dataspace.copernicus.eu/).
2. Navigate to our study area (Nabeul, Tunisia).
3. Explore the Sentinel-1 and Sentinel-2 imagery to visually confirm your area of interest (e.g., specific well clusters, coastal zones, or agricultural fields).
4. Extract the exact coordinates (Latitude/Longitude or a WKT Polygon) for your target zone. These coordinates will be used in the automation script.

### Phase 2: Automated Harvesting (Alaska Satellite Facility - ASF)

Clicking "download" on a web browser is fine for one image, but we need continuous, automated data for our AI models. For this, we use **ASF**, the NASA-funded center for SAR data.

1. **Why ASF?** It provides a powerful API (`asf_search`) that allows us to programmatically search and download Sentinel-1 data based on our locked-in coordinates.
2. **Credentials:** You must have a free [NASA Earthdata](https://urs.earthdata.nasa.gov/) account.
3. **The Secret File:** Create a file named `config.py` in your root folder (this is ignored by Git for security) and add your credentials:
   ```python
   EARTHDATA_USERNAME = "your_username"
   EARTHDATA_PASSWORD = "your_password"
   ```
