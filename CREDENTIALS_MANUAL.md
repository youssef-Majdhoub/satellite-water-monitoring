# 🔑 Credential Obtaining Manual

This manual provides the exact step-by-step instructions to obtain the API credentials required for this project. You will need to create three free accounts and generate specific access keys.

---

## 1. NASA Earthdata Login (EDL)

**Used For:** Downloading Sentinel-1 (via ASF), MODIS, SMAP, GRACE, SWOT.
**What you will get:** Username, Password, and a Bearer Token.

1. **Register:**
   - Go to [urs.earthdata.nasa.gov](https://urs.earthdata.nasa.gov/).
   - Click **"Register"** in the top right corner.
   - Fill out the required information and click **"Register for Earthdata Login"**.
   - Check your email and click the verification link.
2. **Accept the ASF EULA (Required for Sentinel-1):**
   - Go to [urs.earthdata.nasa.gov/profile](https://urs.earthdata.nasa.gov/profile) and log in.
   - Scroll down to the **"Applications"** section.
   - Click **"Approve More Applications"**.
   - Search for **"Alaska Satellite Facility (ASF)"** and click **"Authorize"**.
3. **Generate Token (Optional but recommended for API use):**
   - On the same profile page, look for the **"Generate Token"** section.
   - Click **"Generate Token"**. Copy this long string of characters.
   - **Save this:** This is your `EARTHDATA_TOKEN` (you can also just use your username and password in the code, but tokens are safer).

---

## 2. Copernicus Data Space Ecosystem (CDSE)

**Used For:** Downloading Sentinel-1, Sentinel-2, Sentinel-3, Sentinel-5P.
**What you will get:** Client ID and Client Secret.

1. **Register:**
   - Go to [dataspace.copernicus.eu](https://dataspace.copernicus.eu/).
   - Click **"Register"** in the top right and create a free account.
2. **Create OAuth Client:**
   - Once logged in, click on your username in the top right and select **"User Settings"**.
   - In the left-hand menu, click on **"OAuth clients"**.
   - Click the **"➕ Create client"** button.
3. **Configure the Client:**
   - **Name:** Give it a name (e.g., "Nabeul-Water-Project").
   - **Supported Flow:** Select **"Client Credentials"**.
   - Click **"Create client"**.
4. **Save the Credentials:**
   - A pop-up window will appear showing your **Client ID** and **Client Secret**.
   - **⚠️ CRITICAL:** Copy the **Client Secret** immediately. The portal will **never show it to you again**. If you lose it, you must delete the client and make a new one.

---

## 3. USGS EROS Registration System (ERS)

**Used For:** Downloading Landsat 8/9.
**What you will get:** Username, Password, and an Application Token (M2M).

1. **Register:**
   - Go to [ers.cr.usgs.gov/register](https://ers.cr.usgs.gov/register).
   - Fill out the form to create your account.
2. **Request Machine-to-Machine (M2M) Access:**
   - Go to [ers.cr.usgs.gov](https://ers.cr.usgs.gov) and log in.
   - In the left-hand menu, click on **"Access Request"**.
   - Click the **"Request Access"** button.
   - Select **"Access to EE's Machine to Machine interface (MACHINE)"**.
   - You will be asked a few questions (e.g., "What is the primary application..."). Answer them honestly (e.g., "Research", "Water Resources"). Submit the request.
3. **Wait for Approval:**
   - This is not instant. It usually takes 24–48 hours. You will receive an email when approved.
4. **Generate Application Token:**
   - Once approved, log in to ERS and go to your **"Profile"** (or Home page).
   - Look for the **"Application Token"** section. Click **"Generate Token"**.
   - **Save this:** This long string is your `USGS_TOKEN`. You will also need your `USGS_USERNAME` (the one you just created).

---

## ✅ Summary Checklist

Once you have completed all three steps, you should have a list of credentials that looks like this. You will put these into your local `config.py` file.

- [ ] NASA Earthdata Username & Password (and/or Token)
- [ ] CDSE Client ID & Client Secret
- [ ] USGS Username & Application Token (Wait for approval email first!)
