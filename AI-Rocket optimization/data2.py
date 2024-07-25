import pandas as pd
import numpy as np

# Define the parameters
n_samples = 5000

# Payload Requirements
Payload_Requirements = {
    'payload_mass': np.random.uniform(1000, 20000, n_samples),  # Payload mass in kg
    'payload_volume': np.random.uniform(1, 100, n_samples),  # Payload volume in cubic meters
    'target_orbit': np.random.choice(['LEO', 'GEO', 'polar'], n_samples),  # Target orbit
    'deployment_mechanism': np.random.choice(['fairing', 'dispenser', 'custom'], n_samples),  # Deployment mechanism
}

# Environmental Conditions
Environmental_Conditions = {
    'wind_speed': np.random.uniform(0, 20, n_samples),  # Wind speed in m/s
    'humidity': np.random.uniform(20, 100, n_samples),  # Humidity in percentage
    'temperature': np.random.uniform(-40, 50, n_samples),  # Temperature in Celsius
    'cloud_cover': np.random.uniform(0, 100, n_samples),  # Cloud cover in percentage
    'launch_site_lat': np.random.uniform(-90, 90, n_samples),  # Launch site latitude
    'launch_site_long': np.random.uniform(-180, 180, n_samples),  # Launch site longitude
    'launch_site_alt': np.random.uniform(0, 5000, n_samples),  # Launch site altitude in meters
    'magnetic_field_strength': np.random.uniform(25, 65, n_samples),  # Magnetic field strength in microteslas 
}

# Operational Constraints
Operational_Constraints = {
    'launch_window_start': pd.date_range(start='2024-01-01', periods=n_samples, freq='H'),  # Launch window start time
    'launch_window_end': pd.date_range(start='2024-01-01', periods=n_samples, freq='H') + pd.to_timedelta(np.random.randint(1, 24, n_samples), unit='H'),  # Launch window end time
    'range_safety': np.random.choice(['low', 'medium', 'high'], n_samples),  # Range safety
    'trajectory_constraints': np.random.choice(['none', 'some', 'many'], n_samples),  # Trajectory constraints
    'regulatory_compliance': np.random.choice(['yes', 'no'], n_samples),  # Regulatory compliance
}

# Cost Factors
Cost_Factors = {
    'fuel_costs': np.random.uniform(50000, 1000000, n_samples),  # Fuel costs in USD
    'manufacturing_costs': np.random.uniform(1000000, 20000000, n_samples),  # Manufacturing costs in USD
    'operational_costs': np.random.uniform(500000, 5000000, n_samples),  # Operational costs in USD
    'maintenance_costs': np.random.uniform(100000, 1000000, n_samples),  # Maintenance costs in USD
    'insurance_costs': np.random.uniform(100000, 5000000, n_samples),  # Insurance costs in USD 
}

# Performance Metrics
Performance_Metrics = {
    'delta_v': np.random.uniform(5000, 10000, n_samples),  # Delta-v in m/s
    'burn_time': np.random.uniform(300, 1200, n_samples),  # Burn time in seconds
    'g_forces': np.random.uniform(3, 10, n_samples),  # G-forces experienced
    'trajectory_accuracy': np.random.uniform(0.9, 1.0, n_samples),  # Trajectory accuracy
    'fuel_efficiency': np.random.uniform(0.3, 0.9, n_samples),  # Fuel efficiency
}

# Safety Considerations
Safety_Considerations = {
    'failure_modes': np.random.choice(['engine_failure', 'structural_failure', 'guidance_failure'], n_samples),  # Failure modes
    'redundancy_systems': np.random.choice(['none', 'single_redundancy', 'dual_redundancy'], n_samples),  # Redundancy systems
    'emergency_procedures': np.random.choice(['abort', 'safe_mode', 'land'], n_samples),  # Emergency procedures
    'vibration_levels': np.random.uniform(0, 10, n_samples),  # Vibration levels in g
    'acoustic_levels': np.random.uniform(60, 130, n_samples),  # Acoustic levels in dB
}

# Create DataFrames
df1 = pd.DataFrame(Payload_Requirements)
df2 = pd.DataFrame(Environmental_Conditions)
df3 = pd.DataFrame(Operational_Constraints)
df4 = pd.DataFrame(Cost_Factors)
df5 = pd.DataFrame(Performance_Metrics)
df6 = pd.DataFrame(Safety_Considerations)

# Save the dataset to a CSV file
df1.to_csv('Payload_Requirements.csv', index=False)
df2.to_csv('Environmental_Conditions.csv', index=False)
df3.to_csv('Operational_Constraints.csv', index=False)
df4.to_csv('Cost_Factors.csv', index=False)
df5.to_csv('Performance_Metrics.csv', index=False)
df6.to_csv('Safety_Considerations.csv', index=False)
