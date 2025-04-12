#!/usr/bin/env python3
import os
import sys
import json
import shutil
import importlib

def main():
    # ----------------------------------------------------------------------
    # 1. Load config.json
    # ----------------------------------------------------------------------
    config_path = "/Users/johnle/Downloads/DTSP_discover/config.json"  # Adjust if needed
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Error: config.json not found at {config_path}")
        sys.exit(1)

    capstone_dir = config.get("capstone_project_dir")
    env_file_path = config.get("env_file_path")
    if not capstone_dir or not env_file_path:
        print("Error: 'capstone_project_dir' or 'env_file_path' missing from config.json")
        sys.exit(1)

    # Prepare the output data directory
    data_dir = os.path.join(capstone_dir, "data")
    if os.path.exists(data_dir):
        print(f"Overwriting existing directory: {data_dir}")
        shutil.rmtree(data_dir)
    os.makedirs(data_dir, exist_ok=True)
    print(f"Data will be saved to: {data_dir}")

    # ----------------------------------------------------------------------
    # 2. Load the API key from env.txt
    # ----------------------------------------------------------------------
    try:
        with open(env_file_path, "r") as f:
            content = f.read().strip()
            if '=' in content:
                _, api_key = content.split("=", 1)
                api_key = api_key.strip().strip('"')
            else:
                api_key = content.strip().strip('"')
    except FileNotFoundError:
        print(f"Error: env file not found at {env_file_path}")
        sys.exit(1)

    if not api_key:
        print("Error: API key is empty.")
        sys.exit(1)

    print("Using API key:", api_key)

    # ----------------------------------------------------------------------
    # 3. Attempt to import each table class dynamically
    # ----------------------------------------------------------------------
    # These are the class names from the library's table inventory.
    # We'll try to import each one. If it fails, we skip it.
    table_class_names = [
        "AgeDownloader",
        "AncestryDownloader",
        "ClassofworkerDownloader",
        "DisabilityDownloader",
        "DisabilitypovertyDownloader",
        "CognitivedifficultyDownloader",
        "EducationDownloader",
        "EducationshortDownloader",
        "EmploymentstatusDownloader",
        "ForeignbornDownloader",
        "CitizenstatusDownloader",
        "GiniDownloader",
        "HousingvalueDownloader",
        "MedianmonthlyhousingcostsDownloader",
        "MedianhousingvalueDownloader",
        "MediangrossrentDownloader",
        "TenurepopDownloader",
        "TenureDownloader",
        "TenurelatinoDownloader",
        "TenurewhiteDownloader",
        "TenureblackDownloader",
        "TenureasianDownloader",
        "MediangrossrentbybedroomDownloader",
        "GrossrentbybedroomDownloader",
        "HouseholdincomeDownloader",
        "HouseholdincomelatinoDownloader",
        "HouseholdincomewhiteDownloader",
        "HouseholdincomeblackDownloader",
        "HouseholdincomeasianDownloader",
        "InternetDownloader",
        "HouseholdlanguageDownloader",
        "LanguageshortformDownloader",
        "LanguagelongformDownloader",
        "LatinoDownloader",
        "MedianageDownloader",
        "MedianhouseholdincomeDownloader",
        "MedianhouseholdincomelatinoDownloader",
        "MedianhouseholdincomewhiteDownloader",
        "MedianhouseholdincomeblackDownloader",
        "MedianhouseholdincomeasianDownloader",
        "MobilityDownloader",
        "MobilitybysexDownloader",
        "MobilitywhiteDownloader",
        "MobilityblackDownloader",
        "MobilityasianDownloader",
        "MobilitylatinoDownloader",
        "MobilitybycitizenshipDownloader",
        "OccupancyDownloader",
        "PercapitaincomeDownloader",
        "PercapitaincomelatinoDownloader",
        "PercapitaincomewhiteDownloader",
        "PercapitaincomeblackDownloader",
        "PercapitaincomeasianDownloader",
        "PopulationDownloader",
        "PovertyDownloader",
        "PovertystatusbygenderDownloader",
        "PovertystatusbyageDownloader",
        "PovertylatinoDownloader",
        "PovertywhiteDownloader",
        "PovertyblackDownloader",
        "PovertyasianDownloader",
        "RaceDownloader",
        "AianaloneorincomboDownloader",
        "AsianDownloader",
        "SnapDownloader",
        "SnaplatinoDownloader",
        "SnapwhiteDownloader",
        "SnapblackDownloader",
        "SnapasianDownloader",
        "VeteransDownloader",
        "YearstructurebuiltDownloader",
        "AgehouseholderbyyearbuiltDownloader",
        "TenurebyyearbuiltDownloader",
        "VotersDownloader",
    ]

    # We'll store successfully imported classes here
    downloaded_classes = []

    # Attempt dynamic import from "census_data_downloader.tables"
    for class_name in table_class_names:
        try:
            module = importlib.import_module("census_data_downloader.tables")
            cls = getattr(module, class_name)
            downloaded_classes.append(cls)
        except (ImportError, AttributeError) as e:
            print(f"Skipping {class_name}: {e}")

    print("\nSuccessfully imported these classes:")
    for c in downloaded_classes:
        print("  -", c.__name__)

    # ----------------------------------------------------------------------
    # 4. Download data for each successfully imported table
    # ----------------------------------------------------------------------
    # Choose year(s)
    year = 2021

    for cls in downloaded_classes:
        table_name = cls.__name__
        print(f"\n=== Downloading data for {table_name} ===")
        try:
            downloader = cls(api_key=api_key, data_dir=data_dir, years=year)

            # Attempt states & counties, if those methods exist
            if hasattr(downloader, "download_states"):
                print(f"{table_name}: Downloading states...")
                downloader.download_states()
            if hasattr(downloader, "download_counties"):
                print(f"{table_name}: Downloading counties...")
                downloader.download_counties()

            # Add more as needed: .download_tracts(), etc.
        except Exception as e:
            print(f"Error downloading {table_name}: {e}")

    print("\nAll table downloads (for existing classes) complete!")
    print(f"Check your CSV files in: {data_dir}")

if __name__ == "__main__":
    main()
