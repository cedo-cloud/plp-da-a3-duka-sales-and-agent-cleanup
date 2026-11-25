# Data Analytics Week 3 Assignments

## Summary of Engagements
This repository contains the deliverables for two client engagements:
1. **Duka Electronics:** Explored half-year sales data to identify top branches, products, and channel performance, culminating in an executive summary and Excel dashboard.
2. **Mobile Money Agent Network:** Audited and cleaned an unreliable legacy transaction extract, merged it with an agent register, and produced validated county-level summaries.

## How to Regenerate Data and Run Notebooks
1. Ensure you have Python installed along with the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Generate the synthetic datasets by running:
    ```bash
    python generate_data.py
    ```
   This creates duka_sales.csv, agents.csv, and agent_transactions.csv.


3. Run the Duka exploration notebook:
    ```bash
    jupyter notebook duka_sales_exploration.ipynb
    ```

4. Run the Agent cleanup notebook:
    ```bash
    jupyter notebook agent_cleanup.ipynb
    ```

 ## Duka Executive Summary
- Nairobi contributes 36.4% of total revenue, almost double the next highest branch.
- Laptops generated KES 41.5M in revenue, more than twice the revenue of the second-ranked product.
- In-store and online orders have nearly identical average order values of approximately KES 71,000.
- Weekend orders make up roughly 29% of total transactions, indicating steady weekend footfall and online activity.
- March was the best month for revenue, outperforming the worst month by 12.5%.
- Agent Data: Before and After Row Counts
- Before Cleaning: 612 rows (600 original + 12 duplicates)
- After Cleaning: 600 rows (12 duplicates removed)