import asf_search as asf
import os

try:
    import config
except ImportError:
    print("❌ ERROR: 'config.py' not found. Please create it with your credentials.")
    exit()


def download_nabeul_data():
    print("🚀 Starting Sentinel-1 download for Nabeul...")

    # --- SMART AUTHENTICATION BLOCK ---
    session = asf.ASFSession()
    auth_success = False

    # 1. Try Token Authentication First (if token exists and isn't a placeholder)
    token = getattr(config, "EARTHDATA_TOKEN", "")
    if token and token not in ["your_earthdata_token", "YOUR_TOKEN_HERE"]:
        print("Attempting authentication using NASA Bearer Token...")
        try:
            # asf_search supports token auth in newer versions
            if hasattr(session, "auth_with_token"):
                session.auth_with_token(token)
            else:
                # Fallback for older versions
                session.headers.update({"Authorization": f"Bearer {token}"})
            auth_success = True
            print("✅ Token authentication successful.")
        except Exception as e:
            print(
                f"⚠️ Token authentication failed: {e}. Falling back to credentials..."
            )

    # 2. Fallback to Username/Password
    if not auth_success:
        username = getattr(config, "EARTHDATA_USERNAME", "")
        password = getattr(config, "EARTHDATA_PASSWORD", "")

        if username and password:
            print("Attempting authentication using Username/Password...")
            try:
                session.auth_with_creds(username, password)
                auth_success = True
                print("✅ Credential authentication successful.")
            except Exception as e:
                print(f"❌ Credential authentication failed: {e}")
        else:
            print("❌ No valid Token OR Credentials found in config.py.")
            return

    if not auth_success:
        print(
            "❌ Could not authenticate with NASA Earthdata. Please check your config.py."
        )
        return
    # ----------------------------------

    # 3. Define Area of Interest (Nabeul)
    nabeul_wkt = "POLYGON((10.672 36.424, 10.752 36.424, 10.752 36.477, 10.672 36.477, 10.672 36.424))"

    # 4. Search for Data
    print("\nSearching for Sentinel-1 GRD data (Jan 2024)...")
    try:
        results = asf.geo_search(
            platform=asf.PLATFORM.SENTINEL1,
            intersectsWith=nabeul_wkt,
            start="2024-01-01",
            end="2024-01-31",
            processingLevel=asf.PRODUCT_TYPE.GRD_HD,
            beamMode=asf.BEAMMODE.IW,
            maxResults=2,  # Limit to 2 so it downloads fast for today
        )
        print(f"✅ Found {len(results)} scenes.")
    except Exception as e:
        print(f"❌ Search failed: {e}")
        return

    # 5. Download the Data
    if len(results) > 0:
        download_dir = "./sentinel1_data"
        os.makedirs(download_dir, exist_ok=True)

        for i, result in enumerate(results):
            filename = result.properties["fileName"]
            print(f"\nDownloading {i+1}/{len(results)}: {filename}")
            print(
                "(This may take a few minutes depending on your internet connection)..."
            )

            try:
                result.download(path=download_dir, session=session)
                print(f"✅ Successfully downloaded {filename}")
            except Exception as e:
                print(f"❌ Failed to download {filename}. Error: {e}")

        print(f"\n🎉 Download complete! Check the '{download_dir}' folder.")
    else:
        print(
            "No scenes found for this date range. Try changing the dates in the script."
        )


if __name__ == "__main__":
    download_nabeul_data()
