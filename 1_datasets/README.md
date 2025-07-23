# Datasets Overview

This folder contains all datasets used in the project, organized to support
 reproducible research and clear data provenance. Datasets are grouped by their
  stage in the workflow: raw and processed. Due to an evolution in the
   project's primary research question, datasets are further categorized into
    those relevant to the **current focus on Peer-to-Peer (P2P) lending** and
     those from the **previous focus on Buy Now, Pay Later (BNPL)** that are no
     longer in active use.

## 📁 Folder Structure

- `raw_data/` — Original, unmodified datasets as downloaded from their sources.
 **Never edit these files.**
  - `new/` - Raw datasets relevant to the current P2P lending research question.
  - `old/` - Raw datasets from the previous BNPL research question (deprecated).
- `processed_data/` — Cleaned and transformed datasets, ready for analysis or
 modeling. These are generated
 by scripts or notebooks in the `2_data_preparation/` directory.
  - `new/` - Processed datasets derived from raw data relevant to the current
   P2P lending research question.
  - `old/` - Processed datasets derived from raw data from the previous BNPL
   research question (deprecated).
- `additional_data/` — Supplementary or reference datasets, such as historical
 or contextual data, not used directly for modeling but useful for exploration
 or comparison.

## 📊 Dataset Overview

This section provides a high-level overview of the datasets, categorized by
 their relevance to the project's research questions and their processing stage.

### Raw Data

Raw datasets are the original files downloaded from their sources. They are
 stored in `raw_data/` and its subfolders.

### Relevant Raw Data (Current P2P Lending Focus - `raw_data/new/`)

These datasets form the core of the current research on default risk in P2P
lending systems. For detailed documentation, see
`raw_data/new/README.md`.

- `accepted_2007_to_2018Q4.csv`
  - **Description**: Detailed loan-level data from LendingClub for accepted
        loan applications (2007-2018 Q4), including borrower info, loan
        terms, and statuses.
  - **Relevance**: **Primary dataset** for modeling loan default risk in P2P
        lending. Enables building models using real-world financial features.

-----

### 🗑️ Deprecated Raw Data (Previous BNPL Focus - `raw_data/old/`)

These datasets were collected during the original BNPL-focused research and
are no longer used for the current P2P lending research. For detailed
documentation, see `raw_data/old/README.md`.

- `BNPL.csv`

  - **Description**: Survey data on BNPL usage, indebtedness, and
        financial stress.
  - **Reason for Deprecation**: Focused on BNPL user behavior, not related
        to P22P lending.

- `BNPL Intention to use.xlsx`

  - **Description**: Survey results on consumer intentions and attitudes
        toward BNPL services.
  - **Reason for Deprecation**: BNPL-specific attitudinal data, not
        relevant to P2P lending.

- `afdr_a8.csv`

  - **Description**: Historical agricultural loan characteristics and volumes.
  - **Reason for Deprecation**: Sector-specific (agriculture), not related
        to P2P platforms.

- `afdr_charts.csv`

  - **Description**: Quarterly stats on non-real-estate farm loans.
  - **Reason for Deprecation**: Agriculture-focused, not relevant to P2P systems.

- `FRBNY-SCE-Credit-Access-complete_microdata.xlsx`

  - **Description**: Microdata from the FRBNY Survey on consumer credit
        access and usage.
  - **Reason for Deprecation**: General credit survey, not focused on P2P
        lending.

- `FRBNY-SCE-Credit-Access-Data.xlsx`

  - **Description**: Aggregated results from the FRBNY credit access survey.
  - **Reason for Deprecation**: Credit market data, not P2P-specific.

- `loan_default_dataset.csv`

  - **Description**: Default data, likely from traditional lenders.
  - **Reason for Deprecation**: Not tied to P2P platforms; used in earlier
        research.

- `loan_default_prediction_dataset.csv`

  - **Description**: Dataset for modeling loan defaults from non-P2P sources.
  - **Reason for Deprecation**: Not aligned with P2P lending objectives.

- `public2024.csv`

  - **Description**: General lending or credit data, open source (SHED survey).
  - **Reason for Deprecation**: Not directly related to P2P lending.

- `sce-household-spending-chart-data.xlsx`

  - **Description**: Household spending stats from SCE (aggregated).
  - **Reason for Deprecation**: Macroeconomic focus, not related to P2P defaults.

-----

### 🛠️ Processed Data

Processed datasets are located in `processed_data/` and its subfolders.
These files are generated from the raw data through cleaning, transformation,
and feature engineering steps documented in the `2_data_preparation/`
directory.

#### Processed Data (Current P2P Lending Focus - `processed_data/new/`)

Processed datasets derived from raw data relevant to the current P2P
lending research question.

- `accepted_2007_to_2018Q4.csv`

  - **Description**: Processed version of `accepted_2007_to_2018Q4.csv`.
  - **Derived From**: `raw_data/new/accepted_2007_to_2018Q4.csv`

- *(To be added)*

  - **Description**: Processed version of other relevant raw data in
        `raw_data/new/` (if any).
  - **Derived From**: *(Specify source raw file)*

#### Deprecated Processed Data (Previous BNPL Focus - `processed_data/old/`)

Processed datasets from the previous BNPL research focus that are no longer
used.

- `BNPL_cleaned.csv`

  - **Description**: Cleaned BNPL usage and financial stress data.
  - **Derived From**: `raw_data/old/BNPL.csv`

- `BNPL_intention_to_use_cleaned.csv`

  - **Description**: Cleaned survey on BNPL user intentions.
  - **Derived From**: `raw_data/old/BNPL Intention to use.xlsx`

- `FRBNY_SCE_Credit_Access_cleaned.csv`

  - **Description**: Processed FRBNY SCE credit access data.
  - **Derived From**: `raw_data/old/FRBNY-SCE-Credit-Access-complete_microdata.xlsx`

- `afdr_cleaned.csv`

  - **Description**: Cleaned data on farm loan characteristics.
  - **Derived From**: `raw_data/old/afdr_a8.csv`

- `public2024_cleaned.csv`

  - **Description**: Cleaned version of public lending dataset (SHED).
  - **Derived From**: `raw_data/old/public2024.csv`

-----

### supplemental Data (`additional_data/`)

This folder contains supplementary or reference datasets.

- `afdr_charts_cleaned_historical_match.csv`
  - **Description**: Historical farm loan statistics – volume, rates, etc.
  - **Source/Purpose**: Derived from `raw_data/old/afdr_charts.csv`.
  - **Relevance**: Agriculture-focused, not directly relevant to consumer
        P2P lending, but could provide broad economic context.

-----

### ✅ Best Practices and Guidance

As outlined in `guide.md`:

- **Never modify or overwrite files in `raw_data/`.** Always save cleaned or
    transformed data to `processed_data/` or `additional_data/`.
- **Document each dataset**: Include source, description, and relevance in this
    README and in subfolder READMEs.
- **Use clear, descriptive filenames** for all processed and additional datasets.
- **Ensure reproducibility**: All processing steps should be documented in
    scripts or notebooks in `2_data_preparation/`.

For more detailed guidance, refer to `guide.md`.

-----

**Note:** The tables for "Processed Data (Current P2P Lending Focus)" will need
to be updated as you clean and process the raw data in `raw_data/new/`. Please
add rows to this table with the filenames and descriptions of the processed
files you create.
