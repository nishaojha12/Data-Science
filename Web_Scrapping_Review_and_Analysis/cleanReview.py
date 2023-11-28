import pandas as pd

# Read the CSV file into a DataFrame
input_file = 'D:/data science project/BA_reviews.csv'  # Replace with your actual file name
df = pd.read_csv(input_file)

# Define a function to replace the specified words in a column
def replace_words(text):
    text = text.replace('âœ… Trip Verified |', 'Not Verified | ')
    text = text.replace(' ', ' ')
    return text

# Apply the replacement function to the specified columns
columns_to_replace = ['reviews']  # Replace with your actual column names
for column in columns_to_replace:
    df[column] = df[column].apply(replace_words)

# Store the transformed DataFrame into a new CSV file
output_file = 'output.csv'  # Replace with your desired output file name
df.to_csv(output_file, index=False)
