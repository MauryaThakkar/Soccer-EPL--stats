import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import os

# ==========================================
# 1. CONFIGURATION
# ==========================================
# Example using English Premier League 21/22 season
DATA_URL = "https://www.football-data.co.uk/mmz4281/2122/E0.csv"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../../"))
RAW_PATH = os.path.join(PROJECT_ROOT, "data/raw/E0_2425.csv")
PROCESSED_PATH = os.path.join(PROJECT_ROOT, "data/processed/EPL_Cleaned.csv")

def load_data():
    """Download or load the dataset."""
    if not os.path.exists(RAW_PATH):
        print(f"Downloading data from {DATA_URL}...")
        df = pd.read_csv(DATA_URL)
        # Save for reproducibility
        os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)
        df.to_csv(RAW_PATH, index=False)
        print(f"Data saved to {RAW_PATH}")
    else:
        print(f"Loading local data from {RAW_PATH}...")
        df = pd.read_csv(RAW_PATH)
    return df

def feature_engineering(df):
    """
    Create predictive features from raw match stats.
    """
    # 1. Target Variable: FTR (Full Time Result) -> H, D, A
    # Already exists in dataset
    
    # 2. Key Features: Home/Away Team, Form, Historical Elo (simplified here)
    # Convert Categorical 'HomeTeam'/'AwayTeam' to codes if needed, 
    # but for Tree models, encoding is handled or we use numeric stats.
    
    # Example: Calculate 'Goal Difference' per game
    df['HomeGoalDiff'] = df['FTHG'] - df['FTAG']
    
    # Rolling Averages (The 'Form' metric)
    # Note: In a real project, you must be careful not to leak future data.
    # Group by team and shift results to get 'previous n games' stats.
    # This is complex to implement in a single snippet, but here is the logic:
    # df.sort_values('Date', inplace=True)
    
    # For simplicity of this starter, we will use basic Match Stats available pre-match?
    # Actually, football-data only has post-match stats. 
    # A real model needs 'Pre-Match Odds' (B365H, B365D, B365A) as a baseline feature.
    
    features = ['B365H', 'B365D', 'B365A'] # Betting odds are excellent predictors
    target = 'FTR'
    
    # Drop rows with missing odds
    df_clean = df.dropna(subset=features + [target])
    
    return df_clean, features, target

def train_model(df, feature_cols, target_col):
    X = df[feature_cols]
    y = df[target_col]
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluate
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    
    print(f"Model Accuracy: {acc:.4f}")
    print("\nClassification Report:\n", classification_report(y_test, preds))
    
    return clf

if __name__ == "__main__":
    # Pipeline execution
    df_raw = load_data()
    print(f"Loaded {len(df_raw)} matches.")
    
    df_processed, features, target = feature_engineering(df_raw)
    
    # Save processed data
    print(f"Saving processed data to {PROCESSED_PATH}...")
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    df_processed.to_csv(PROCESSED_PATH, index=False)
    
    model = train_model(df_processed, features, target)
    
    print("Example pipeline complete. Next steps: Implement rolling average form features.")
