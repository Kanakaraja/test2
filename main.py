
import pandas as pd

def load_page():

    # Create a sample DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
            'Age': [25, 30, 28, 25, 32],
            'City': ['New York', 'London', 'Paris', 'New York', 'London'],
            'Salary': [60000, 75000, 68000, 62000, 80000]}

    df = pd.DataFrame(data)

    # Display the DataFrame
    print("Original DataFrame:\n", df)

    # Get information about the DataFrame
    print("\nDataFrame Info:\n", df.info())

    # Get descriptive statistics
    print("\nDescriptive Statistics:\n", df.describe())

    # Accessing data
    print("\nFirst 3 rows:\n", df.head(3))
    print("\nName column:\n", df['Name'])
    print("\nAge of Bob:\n", df.loc[df['Name'] == 'Bob', 'Age']) # More robust way

    # Filtering data
    print("\nPeople older than 28:\n", df[df['Age'] > 28])
    print("\nPeople from New York:\n", df[df['City'] == 'New York'])

    # Grouping and aggregation
    print("\nAverage salary by city:\n", df.groupby('City')['Salary'].mean())
    print("\nNumber of people in each city:\n", df.groupby('City').size())

    # Sorting data
    print("\nSorted by age:\n", df.sort_values('Age'))

    # Adding a new column
    df['Bonus'] = df['Salary'] * 0.1  # 10% bonus
    print("\nDataFrame with Bonus column:\n", df)

    # Applying a function to a column
    def categorize_salary(salary):
        if salary < 70000:
            return 'Low'
        elif salary < 80000:
            return 'Medium'
        else:
            return 'High'

    df['Salary Category'] = df['Salary'].apply(categorize_salary)
    print("\nDataFrame with Salary Category:\n", df)

    # Dealing with missing values (if any) - Example
    # df['Missing_Column'] = [None, 1, None, 3, None]  # Introduce some NaNs
    # print("\nDataFrame with Missing Values:\n", df)
    # print("\nFilling NaN with 0:\n", df.fillna(0))
    # print("\nDropping rows with NaN:\n", df.dropna())

    # Saving to a CSV file
    # df.to_csv('output.csv', index=False)  # index=False prevents writing the DataFrame index to the file

    print("\nDataFrame after all operations:\n", df)

if __name__ == "__main__":
    load_page()
