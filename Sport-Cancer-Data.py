import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Category': ['Healthy', 'Healthy', 'Healthy', 'Healthy', 'Healthy', 'Cancer Patients', 'Cancer Patients', 'Cancer Patients', 'Cancer Patients', 'Cancer Patients'],
    'Exercise Intensity': ['0.1', '0.5', '1.0', '0.5', '0.1', '0.1', '1.0', '0.5', '1.0', '0.1'],
    'v2pk': [63, 68, 73, 65, 60, 55, 75, 68, 80, 58]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Calculate the correlation coefficient for the "Healthy" category and the "Cancer Patients" category
healthy_df = df[df['Category'] == 'Healthy']
correlation_healthy = healthy_df['Exercise Intensity'].corr(healthy_df['v2pk'])
cancerpatients_df = df[df['Category'] == 'Cancer Patients']
correlation_cancerpatients = cancerpatients_df['Exercise Intensity'].corr(cancerpatients_df['v2pk'])

print("Correlation coefficient for Cancer Patients category: ", correlation_cancerpatients)
print("Correlation coefficient for Healthy category:", correlation_healthy)


# Create a scatter plot for the "Healthy" category and the "Cancer Patients" category
plt.scatter(healthy_df['Exercise Intensity'], healthy_df['v2pk'], label='Healthy')
plt.scatter(healthy_df['Exercise Intensity'], cancerpatients_df['v2pk'], label='Cancer Patients')
plt.xlabel('Exercise Intensity')
plt.ylabel('v2pk (Oxygen Peak Intensity)')
plt.title('Exercise Intensity vs. v2pk for Healthy and Cancer Patients')

# Show the plot
plt.show()


# Creating a sample dataset
data = {
    'Category': ['Healthy', 'Healthy', 'Healthy', 'Healthy', 'Healthy', 'Cancer Patients', 'Cancer Patients', 'Cancer Patients', 'Cancer Patients', 'Cancer Patients'],
    'Exercise Intensity': ['Low', 'Medium', 'High', 'Medium', 'Low', 'Low', 'High', 'Medium', 'High', 'Low'],
    'v2pk': [63, 68, 73, 65, 60, 55, 75, 68, 80, 58]
}

# Creating a DataFrame from the data
df = pd.DataFrame(data)

# Creating a box plot
plt.figure(figsize=(10, 6))
plt.grid(True)
plt.title('v2pk Distribution by Exercise Intensity for Healthy and Cancer Patients')

# Box plot for "Healthy" category
healthy_df = df[df['Category'] == 'Healthy']
plt.boxplot([healthy_df[healthy_df['Exercise Intensity'] == 'Low']['v2pk'], 
             healthy_df[healthy_df['Exercise Intensity'] == 'Medium']['v2pk'], 
             healthy_df[healthy_df['Exercise Intensity'] == 'High']['v2pk']],
            labels=['Low', 'Medium', 'High'],
            positions=[1, 2, 3],
            patch_artist=True,
            boxprops=dict(facecolor='skyblue'))

# Box plot for "Cancer Patients" category
cancer_df = df[df['Category'] == 'Cancer Patients']
plt.boxplot([cancer_df[cancer_df['Exercise Intensity'] == 'Low']['v2pk'], 
             cancer_df[cancer_df['Exercise Intensity'] == 'Medium']['v2pk'], 
             cancer_df[cancer_df['Exercise Intensity'] == 'High']['v2pk']],
            labels=['Low', 'Medium', 'High'],
            positions=[5, 6, 7],
            patch_artist=True,
            boxprops=dict(facecolor='lightcoral'))

plt.xlabel('Exercise Intensity')
plt.ylabel('v2pk (Oxygen Peak Intensity)')

plt.xticks([2, 6], ['Healthy', 'Cancer Patients'])
plt.show()

import pandas as pd

data = {
    'Category': ['Healthy', 'Healthy', 'Healthy', 'Healthy', 'Healthy', 'Cancer Patients', 'Cancer Patients', 'Cancer Patients', 'Cancer Patients', 'Cancer Patients'],
    'Exercise Intensity': ['0.1', '0.5', '1.0', '0.5', '0.1', '0.1', '1.0', '0.5', '1.0', '0.1'],
    'v2pk': [63, 68, 73, 65, 60, 55, 75, 68, 80, 58]
}

df = pd.DataFrame(data)
import seaborn as sns
import matplotlib.pyplot as plt

# Convert categorical variables to numeric
df['Category'] = df['Category'].astype('category')
df['Exercise Intensity'] = df['Exercise Intensity'].astype('category')

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df['Category'] = label_encoder.fit_transform(df['Category'])
df['Exercise Intensity'] = label_encoder.fit_transform(df['Exercise Intensity'])

# حالا می‌توانید نمودار کرلیشن را بسازید
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
