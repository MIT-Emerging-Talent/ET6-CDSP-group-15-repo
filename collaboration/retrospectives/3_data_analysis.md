# Milestone 3: Data Analysis Retrospective

**Dates:** July 1 - July 21, 2025  
**Syllabus Alignment:** Learning from Data  

## Stop Doing

1. **Avoiding tracking small changes**  
   - Not logging minor updates to the project board reduced visibility
2. **Over-collecting demographic data**  
   - Gathering unnecessary address/location details that were later excluded
3. **Parallel work without daily syncs**  
   - Working on separate files (accepted/rejected datasets)
     without daily check-ins caused minor integration issues

## Continue Doing

1. **Strategic feature reduction**  
   - Maintaining column reduction approach (246 → 50 columns)
     while preserving key predictors
2. **Collaborative visualization sprints**  
   - Continuing 2-day intensive teamwork sessions for cleaning/visualization
3. **SHAP interpretation**  
   - Using explainability tools to make model decisions transparent
4. **Meeting minute discipline**  
   - Keeping consistent documentation with 2-day turnaround

## Start Doing

1. **Micro-task tracking**  
   - Logging even small changes to project board for better visibility
2. **Feature change log**  
   - Documenting rationale for column inclusion/exclusion decisions
3. **Daily standups during parallel work**  
   - Brief 15-minute syncs when team members split datasets
4. **Model interpretation sessions**  
   - Dedicated meetings to review SHAP results and business implications

## Lessons Learned

1. **Feature value varies**  
   - Loan-to-income ratio outperformed many traditional features,
   while address details added little predictive value
2. **Parallel processing efficiency**  
   - Splitting datasets between team members (accepted/rejected) accelerated workflow
3. **State matters**  
   - Geographic location (state) proved valuable
     despite removing other location details
4. **Visualization > Complexity**  
   - Simple SHAP plots communicated insights better than complex model metrics alone

---

## Strategy vs. Board

### What parts of your plan went as expected?

- Successfully reduced features while preserving predictive power
- Completed SHAP analysis as planned in README
- Achieved target model performance (XGBoost AUC .72)
- Maintained 80% project progress as tracked

### What parts of your plan did not work out?

- Initial demographic analysis scope was too broad
- Age parameter gaps required unexpected workarounds
- Class imbalance handling took 25% longer than estimated
- Blockchain research direction distracted from core ML focus

### Did you need to add things that weren't in your strategy?

- Added state-level geographic analysis after discovering its value
- Implemented additional visualization techniques for stakeholder communication
- Created data reconciliation process for parallel file work
- Added feature importance documentation to repository

### Or remove extra steps?

- Eliminated detailed address collection after 7/16 meeting decision
- Removed redundant demographic columns during feature reduction
- Streamlined meeting agendas to focus on analysis roadblocks
- Deprioritized blockchain research thread to maintain focus

---

## Individual Retrospectives

### Noorelsalam Almakki  

**Visualization Architect & Documentation Specialist**  
Transformed complex model insights into intuitive SHAP visualizations
that reveal key risk predictors, while simultaneously refining our README
to showcase analytical progress to stakeholders. Balancing creative design
with technical accuracy proved challenging when simplifying XGBoost results
for diverse audiences. Through this process, I've strengthened both my explanatory
storytelling and strategic documentation skills—ensuring our work remains accessible
as we prepare for final presentations.

### Madiha Malikzada

At this milestone, we assigned tasks across the team and agreed on
who would handle what. After completing my part, I moved on to modeling
and removed some features I thought were unnecessary—without informing
the teammate who had worked on them. That was a mistake. I learned that
in teamwork, it's essential to communicate any changes, especially when
they affect someone else's work. After my teammates raised their concerns,
I acknowledged the issue, apologized, and took it as a valuable lesson in
respecting others' contributions.

### Myint Myat Zaw

- **Contributions:** Helped clean both selected and rejected datasets,
and worked on building machine learning models
all the way through to hyperparameter tuning.
- **Challenges:**  Faced occasional miscommunication and overlapping
responsibilities within the team, which made task coordination a bit tricky.
- **Progress:** Gained valuable experience in choosing appropriate ML models
for different problem types,
along with deepening my skills in model interpretation and fine-tuning.

### Al-Hassen Sabeeh

**Milestone 4 Organization Suggestion:**
> "For better workflow in Milestone 4, I propose we implement
 **structured time-boxing** from day one:
>
> - **Weekly planning sessions** every Monday to assign specific owners/due dates
> - **Daily 15-minute standups** at consistent times (9:30 AM EST?)  
> - **Task batching** by communication medium
 (e.g. Wed AM = investor materials, Thu PM = technical docs)  
> - **Buffer blocks** scheduled for unexpected revisions  
> This structured approach will prevent last-minute rushes and ensure balanced workloads."

### Dadi Ishimwe

- **What went well:** Documenting: Documenting the 'why' behind feature changes
as it is crucial for understanding the analytical process and for future reproducibility.
- **What to improve:** Focus on core ML: I allowed myself to be somewhat
distracted by the modeling research direction, which diverted focus
from the core ML objectives. I need to improve my ability to prioritize
and deprioritize tasks effectively.

### Ahmed Hussein
