# 🛰️ Technical Data Download Manual: Accounts & APIs

This manual provides the technical specifications for downloading the satellite datasets used in this project. It lists the required accounts, how to securely store your credentials, and the programmatic methods (APIs/Python libraries) for each data source.

---

## 1. Account Registry & Prerequisites

You must register for these free accounts before downloading data.

| Account Service                            | URL                                                          | Used For                                                |
| :----------------------------------------- | :----------------------------------------------------------- | :------------------------------------------------------ |
| **Copernicus Data Space Ecosystem (CDSE)** | [dataspace.copernicus.eu](https://dataspace.copernicus.eu)   | Sentinel-1, Sentinel-2, Sentinel-3, Sentinel-5P         |
| **NASA Earthdata Login (EDL)**             | [urs.earthdata.nasa.gov](https://urs.earthdata.nasa.gov)     | MODIS, SMAP, GRACE, PACE, SWOT, and ASF data            |
| **USGS EROS Registration System (ERS)**    | [ers.cr.usgs.gov/register](https://ers.cr.usgs.gov/register) | Landsat, declassified imagery (requires M2M API access) |

---

## 2. 🔐 Credential Management (`config.py`)

To prevent accidentally uploading your passwords to GitHub, **we never hardcode credentials directly into our Python scripts**. Instead, we use a local `config.py` file. This file is explicitly listed in `.gitignore` and will remain only on your local machine.

Create a file named exactly `config.py` in the root folder of your project and paste this template:

```python
# config.py

# NASA Earthdata Credentials (Used for ASF, MODIS, SMAP, etc.)
EARTHDATA_USERNAME = "your_nasa_earthdata_username"
EARTHDATA_PASSWORD = "your_nasa_earthdata_password"

# NASA Earthdata Token (Optional but Recommended)
# Our scripts prioritize this token over the username/password.
# Leave as "" if you only want to use your username/password.
EARTHDATA_TOKEN = "your_nasa_bearer_token"

# Copernicus CDSE Credentials (Used for Sentinel-2, Sentinel-3, etc.)
# (Generate these in your CDSE Account Settings under OAuth2)
CDSE_CLIENT_ID = "your_client_id"
CDSE_CLIENT_SECRET = "your_client_secret"

# USGS EarthExplorer Credentials (Used for Landsat)
USGS_USERNAME = "your_usgs_username"
USGS_TOKEN = "your_m2m_api_token" # Note: This is the token, not your password
```
