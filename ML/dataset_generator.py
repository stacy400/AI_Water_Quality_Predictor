import pandas as pd
import numpy as np

def generate_synthetic_data(n_samples=1000):
    """Generate synthetic water quality data for testing."""
    data = {
        'ph': np.random.uniform(6.0, 8.5, n_samples),
        'hardness': np.random.uniform(47.432, 323.125, n_samples),
        'solids': np.random.uniform(320.94, 61323.8, n_samples),
        'chloramines': np.random.uniform(0.35, 13.127, n_samples),
        'sulfate': np.random.uniform(129.0, 481.0, n_samples),
        'conductivity': np.random.uniform(181.48, 753.343, n_samples),
        'organic_carbon': np.random.uniform(2.2, 28.3, n_samples),
        'trihalomethanes': np.random.uniform(0.738, 124.0, n_samples),
        'turbidity': np.random.uniform(1.45, 6.7, n_samples),
        'Potability': np.random.choice([0, 1], n_samples)
    }
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = generate_synthetic_data(1000)
    df.to_csv("synthetic_water_data.csv", index=False)
    print("Synthetic data generated!")
