# Milestone 2 Retrospective

## Stop Doing

- Assuming datasets are clean without validation checks
- Writing data prep scripts without saving intermediate versions
- Postponing README updates until final documentation phase
- Exploring data without clear objectives ("fishing expeditions")

## Continue Doing

- Maintaining strict folder structure for data/code separation
- Collaborative debugging of data preparation scripts
- Using version control for dataset iterations
- Sharing visualizations during exploration for team feedback

## Start Doing

- Using Google Colab for shared tasks
- Creating data validation checklists before processing
- Automating dataset documentation (e.g., data dictionaries)
- Holding "data walkthroughs" when introducing new datasets
- Setting exploration timeboxes (2-hour focused sessions)

## Lessons Learned

We learned that data quality issues surface much later without upfront validation,
causing rework. The folder structure saved significant time when multiple scripts
were developed concurrently. Most importantly, we discovered that exploration
without concrete questions leads to wasted effort - focused hypotheses yield
better insights.

## Strategy vs. Reality

### What worked

- Folder organization prevented code/data mixups
- Separation of prep/exploration phases was effective
- README documentation helped trace data lineage
- Raw/processed data versioning proved valuable

### What didn't work

- Underestimated time for data cleaning (2x longer)
- Some exploration notebooks became unfocused
- Late discovery of critical missing data fields
- READMEs lagged behind code development

### Added to strategy

- Implemented data hash verification for integrity checks
- Added automated data profiling reports
- Created script dependency diagram
- Introduced data quality dashboard

### Removed

- Removed redundant visualizations in exploration phase
- Consolidated similar data prep scripts
- Eliminated planned dataset (irrelevant to research Q)

## Google Colab Integration Suggestions

We recommend using Google Colab for these tasks next milestone:

1. **Collaborative Exploration**
   - Create shared Colab notebooks in `/3_data_exploration`
   - Use `!git clone` to pull datasets directly from repo
   - Simultaneously visualize findings with team members

2. **Data Preparation Sandbox**

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   !cp "/content/drive/MyDrive/project/1_datasets/raw.csv" .
   # Shared cleaning script development

## Individual Retrospectives

### Noorelsalam Almakki  

Transformed raw data insights into intuitive visual schemas for
stakeholder comprehension. Simultaneously refined README architecture
to reflect evolving research focus and data collection methodology.

### Madiha Malikzada

During this milestone, I learned how to better organize our project.
Someone shared a helpful template that broke tasks into smaller
steps with clear timelines. Each team member could choose and assign
themselves to specific tasks, which made the work more manageable and efficient.

### Myint Myat Zaw

During the data collection phase, our focus on BNPL-related datasets made
things pretty overwhelming. The topic itself was niche, and finding datasets
that were both available and actually relevant turned out to be tougher than expected.
We explored a bunch of different angles and sources, trying to branch outas much
as possible, but even then, it felt like we never quite landed on the perfect fit.
At one point, we even considered using synthetic data just to move forward.
This phase taught me how challenging it can be to collect meaningful data for
specific topics, and how important it is to be flexible and creative with sourcing.

### Al-Hassen Sabeeh

Restructured repository organization by implementing intuitive folder taxonomy
and documenting file conventions. Authored comprehensive milestone retrospective
while balancing dataset reconciliation tasks across parallel workflows.

### Dadi Ishimwe

- **What went well:** Understanding the problem domain: I believe I gained a solid
  understanding of how to model our problem domain with data, considering the advice
  of domain experts. This was crucial in identifying relevant data points.

- **What to improve:**Early identification of data limitations: It's critical
  to identify potential data limitations and missing information as early as possible
  to inform data collection strategies and avoid roadblocks.

### Ahmed Hussein
