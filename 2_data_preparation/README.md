# Data Preparation

This folder contains all Python scripts and Jupyter notebooks used to clean,
 preprocess, and prepare datasets for analysis and modeling.

The primary goal of the scripts in this directory is to ensure a reproducible
 data workflow. They read raw datasets from the `1_datasets/raw_data` folder,
  perform necessary transformations, and save the cleaned output as
 **new files** in `1_datasets/processed_data` or `1_datasets/additional_data`.

**Note:** Never modify an original dataset directly. Saving processed data to
 a new file is critical for reproducible research.

-----

## 📁 Folder Contents

This directory is organized into the current project scripts and
 older/supplementary scripts.

* **`new/`**
    This folder contains the primary notebooks for
     the **P2P Loan Default Prediction** project. These scripts cover the
     complete workflow from data cleaning and feature engineering to model
     training, tuning, and evaluation. See the
      `new/README.md` for a
     detailed breakdown of each notebook's methodology.

* **`old/`**
    This folder contains earlier data preparation scripts. These notebooks
   focus on cleaning and processing supplementary datasets related
   to **Buy Now, Pay Later (BNPL)**, **USDA Agricultural Finance**, and
    **FRBNY Credit Access surveys**. They are kept for reference and contextual
   analysis. For a full list of scripts and their outputs, please see the `old/README.md`.

* **`guide.md`**
    This file provides best practices and guidelines for adding new data
   preparation scripts to this repository, ensuring consistency and reproducibility.
