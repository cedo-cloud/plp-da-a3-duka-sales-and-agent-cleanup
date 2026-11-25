import pandas as pd
import numpy as np

def clean_agent_data(txns, agents):
    """
    Cleans the agent transaction data and merges with agent register.
    Returns a tuple: (clean_df, log)
    """
    log = []
    df = txns.copy()
    
    # 1. Uniqueness: Remove duplicates
    initial_rows = len(df)
    df = df.drop_duplicates(subset=['txn_id'])
    log.append(f"Uniqueness: Removed {initial_rows - len(df)} duplicate transactions.")
    
    # 2. Consistency: Standardise txn_type
    df['txn_type'] = df['txn_type'].str.strip().str.title()
    
    # 3. Validity and types: amount and date
    df['amount'] = pd.to_numeric(df['amount'].replace('N/A', np.nan), errors='coerce')
    df['txn_date'] = pd.to_datetime(df['txn_date'].str.replace('/', '-', regex=False), errors='coerce')
    
    # 4. Completeness: Treat missing/invalid amounts
    missing_count = df['amount'].isna().sum()
    df['amount_imputed'] = df['amount'].isna()
    median_amount = df['amount'].median()
    df['amount'] = df['amount'].fillna(median_amount)
    log.append(f"Completeness: Imputed {missing_count} missing/invalid amounts with median ({median_amount}).")
    
    # 5. Outliers: IQR method
    q1 = df['amount'].quantile(0.25)
    q3 = df['amount'].quantile(0.75)
    iqr = q3 - q1
    upper_bound = q3 + 1.5 * iqr
    df['is_outlier'] = df['amount'] > upper_bound
    outlier_count = df['is_outlier'].sum()
    log.append(f"Outliers: Flagged {outlier_count} transactions above IQR upper bound ({upper_bound:.0f}).")
    
    # 6. Merge: Join with agents
    merged = df.merge(agents[['agent_id', 'county']], on='agent_id', how='left', indicator=True)
    unknown_agents = (merged['_merge'] == 'left_only').sum()
    log.append(f"Merge: Found {unknown_agents} transactions with unknown agents (e.g., AG099). Kept them with NaN county.")
    merged = merged.drop(columns=['_merge'])
    
    # Final column ordering
    final_cols = ['txn_id', 'agent_id', 'txn_type', 'amount', 'txn_date', 'county', 'amount_imputed', 'is_outlier']
    merged = merged[final_cols]
    
    return merged, log