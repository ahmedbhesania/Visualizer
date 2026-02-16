import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        self.current_plot = None

    def load_data(self, path):
        try:
            self.data = pd.read_csv(path)
            print("Dataset loaded successfully")
        except Exception as e:
            print("Error loading file:", e)

    def explore_data(self):
        if self.data is None:
            print("Load dataset first")
            return

        print("1. First 5 rows")
        print("2. Last 5 rows")
        print("3. Column names")
        print("4. Data types")
        print("5. Basic info")
        choice = input("Enter choice: ")

        if choice == "1":
            print(self.data.head())
        elif choice == "2":
            print(self.data.tail())
        elif choice == "3":
            print(self.data.columns)
        elif choice == "4":
            print(self.data.dtypes)
        elif choice == "5":
            print(self.data.info())
        else:
            print("Invalid choice")

    def handle_missing(self):
        if self.data is None:
            print("Load dataset first")
            return

        print("1. Show missing values")
        print("2. Fill with mean")
        print("3. Drop missing rows")
        print("4. Fill with specific value")
        choice = input("Enter choice: ")

        if choice == "1":
            print(self.data[self.data.isnull().any(axis=1)])
        elif choice == "2":
            self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
            print("Missing values filled with mean")
        elif choice == "3":
            self.data.dropna(inplace=True)
            print("Missing rows dropped")
        elif choice == "4":
            value = input("Enter value: ")
            self.data.fillna(value, inplace=True)
            print("Missing values replaced")
        else:
            print("Invalid choice")

    def dataframe_operations(self):
        if self.data is None:
            print("Load dataset first")
            return

        print("1. Add new column")
        print("2. Multiply numeric column")
        print("3. Split by column value")
        choice = input("Enter choice: ")

        if choice == "1":
            col1 = input("Enter first column: ")
            col2 = input("Enter second column: ")
            new_col = input("Enter new column name: ")
            self.data[new_col] = self.data[col1] + self.data[col2]
            print("Column added")
        elif choice == "2":
            col = input("Enter column: ")
            factor = float(input("Enter number to multiply: "))
            self.data[col] = self.data[col] * factor
            print("Column updated")
        elif choice == "3":
            col = input("Enter column to split by: ")
            groups = dict(tuple(self.data.groupby(col)))
            for key in groups:
                print("Group:", key)
                print(groups[key].head())
        else:
            print("Invalid choice")

    def descriptive_stats(self):
        if self.data is None:
            print("Load dataset first")
            return

        print(self.data.describe())
        print("Standard Deviation")
        print(self.data.std(numeric_only=True))
        print("Variance")
        print(self.data.var(numeric_only=True))

    def aggregate_functions(self):
        if self.data is None:
            print("Load dataset first")
            return

        col = input("Enter column to aggregate: ")
        print("Sum:", self.data[col].sum())
        print("Mean:", self.data[col].mean())
        print("Count:", self.data[col].count())

    def create_pivot(self):
        if self.data is None:
            print("Load dataset first")
            return

        index = input("Enter index column: ")
        values = input("Enter values column: ")
        table = pd.pivot_table(self.data, index=index, values=values, aggfunc="sum")
        print(table)

    def visualize_data(self):
        if self.data is None:
            print("Load dataset first")
            return

        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Box Plot")
        choice = input("Enter choice: ")

        if choice == "1":
            x = input("Enter x column: ")
            y = input("Enter y column: ")
            self.data.groupby(x)[y].sum().plot(kind="bar")
            plt.title("Bar Plot")
            plt.show()
        elif choice == "2":
            x = input("Enter x column: ")
            y = input("Enter y column: ")
            plt.plot(self.data[x], self.data[y])
            plt.title("Line Plot")
            plt.show()
        elif choice == "3":
            x = input("Enter x column: ")
            y = input("Enter y column: ")
            plt.scatter(self.data[x], self.data[y])
            plt.title("Scatter Plot")
            plt.show()
        elif choice == "4":
            col = input("Enter column: ")
            self.data[col].value_counts().plot(kind="pie", autopct="%1.1f%%")
            plt.title("Pie Chart")
            plt.show()
        elif choice == "5":
            col = input("Enter column: ")
            plt.hist(self.data[col])
            plt.title("Histogram")
            plt.show()
        elif choice == "6":
            col = input("Enter column: ")
            sns.boxplot(x=self.data[col])
            plt.title("Box Plot")
            plt.show()
        else:
            print("Invalid choice")

    def save_plot(self):
        name = input("Enter file name to save plot: ")
        plt.savefig(name)
        print("Plot saved")


def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("Data Analysis and Visualization Program")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Aggregate Functions")
        print("7. Create Pivot Table")
        print("8. Data Visualization")
        print("9. Save Visualization")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter CSV file path: ")
            analyzer.load_data(path)
        elif choice == "2":
            analyzer.explore_data()
        elif choice == "3":
            analyzer.dataframe_operations()
        elif choice == "4":
            analyzer.handle_missing()
        elif choice == "5":
            analyzer.descriptive_stats()
        elif choice == "6":
            analyzer.aggregate_functions()
        elif choice == "7":
            analyzer.create_pivot()
        elif choice == "8":
            analyzer.visualize_data()
        elif choice == "9":
            analyzer.save_plot()
        elif choice == "10":
            print("Exiting program")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
