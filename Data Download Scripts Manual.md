# 🛰️ Data Download Scripts Manual

This manual documents the behavior, inputs, and outputs for each Python script used to download satellite data for the Nabeul Water Anomaly project.

**Prerequisites before running any script:**

1. Ensure your virtual environment (`.venv`) is activated.
2. Ensure your `config.py` file is populated with the required API credentials.

---

## 1. Sentinel-1 (SAR Radar Data)

**Script Name:** `download_sentil1.py`

### 📖 What this script does

This script connects to the Alaska Satellite Facility (ASF) via the `asf_search` API. It searches for Sentinel-1 Synthetic Aperture Radar (SAR) data covering the Nabeul region. Sentinel-1 data is essential for detecting **water abstraction anomalies** because it can measure land subsidence (ground sinking due to groundwater pumping) and soil moisture, regardless of cloud cover or time of day.

### ⚙️ Inputs (What the script expects)

The script uses hardcoded variables that you can modify at the top of the function:

- **`nabeul_wkt` (String):** The Area of Interest (AOI) defined as a WKT polygon. Default is a bounding box around Nabeul.
  - _Format:_ `'POLYGON((min_lon min_lat, max_lon min_lat, max_lon max_lat, min_lon max_lat, min_lon min_lat))'`
- **`start` & `end` (String):** The date range for the search.
  - _Format:_ `'YYYY-MM-DD'` (e.g., `'2024-01-01'`).
- **`processingLevel` (API Constant):** Currently set to `asf.PRODUCT_TYPE.GRD_HD` (Ground Range Detected, High Definition). This is the standard, map-projected radar product.
- **`beamMode` (API Constant):** Currently set to `asf.BEAMMODE.IW` (Interferometric Wide Swath). This is the standard land-monitoring mode.
- **`maxResults` (Integer):** The maximum number of scenes to download.
  - _Note:_ Kept at `2` for testing. Increase this to download more data.

### 📦 Expected Outputs (What the script creates)

- **Folder:** Creates a directory named `./sentinel1_data/` in the root of the project.
- **Files:** Downloads `.zip` archives.
- **File Size:** **Large.** Each Sentinel-1 scene is approximately 800 MB to 1.5 GB.
- **File Contents (Inside the zip):** When extracted, these contain the `.tiff` raster files of radar backscatter (VV and VH polarizations) and the metadata `.xml` files necessary for processing.

---

_(Future scripts will be documented below as they are developed)_

## 2. Sentinel-2 (High-Res Optical Data)

**Script Name:** _TBD_

## 3. Landsat 8/9 (Historical Optical Data)

**Script Name:** _TBD_

## 4. NASA Earthdata (SMAP, SWOT, MODIS)

**Script Name:** _TBD_
