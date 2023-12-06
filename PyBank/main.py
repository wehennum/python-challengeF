import pandas as pd

# Create a dictionary with the data
data = {
    'Date': ['Jan-10', 'Feb-10', 'Mar-10', 'Apr-10', 'May-10', 'Jun-10', 'Jul-10', 'Aug-10', 'Sep-10', 'Oct-10', 'Nov-10', 'Dec-10', 'Jan-11', 'Feb-11', 'Mar-11', 'Apr-11', 'May-11', 'Jun-11', 'Jul-11', 'Aug-11', 'Sep-11', 'Oct-11', 'Nov-11', 'Dec-11', 'Jan-12', 'Feb-12', 'Mar-12', 'Apr-12', 'May-12', 'Jun-12', 'Jul-12', 'Aug-12', 'Sep-12', 'Oct-12', 'Nov-12', 'Dec-12', 'Jan-13', 'Feb-13', 'Mar-13', 'Apr-13', 'May-13', 'Jun-13', 'Jul-13', 'Aug-13', 'Sep-13', 'Oct-13', 'Nov-13', 'Dec-13', 'Jan-14', 'Feb-14', 'Mar-14', 'Apr-14', 'May-14', 'Jun-14', 'Jul-14', 'Aug-14', 'Sep-14', 'Oct-14', 'Nov-14', 'Dec-14', 'Jan-15', 'Feb-15', 'Mar-15', 'Apr-15', 'May-15', 'Jun-15', 'Jul-15', 'Aug-15', 'Sep-15', 'Oct-15', 'Nov-15', 'Dec-15', 'Jan-16', 'Feb-16', 'Mar-16', 'Apr-16', 'May-16', 'Jun-16', 'Jul-16', 'Aug-16', 'Sep-16', 'Oct-16', 'Nov-16', 'Dec-16', 'Jan-17', 'Feb-17'],
    'Profit/Losses': [1088983, -354534, 276622, -728133, 852993, 563721, -535208, 632349, -173744, 950741, -785750, -1194133, -589576, -883921, 443564, 837887, 1081472, 464033, -1066544, 323846, -806551, 487053, 1128811, 791398, 739367, -197825, 666016, 589771, 489290, -471439, 120417, 175347, 855449, 605195, -235220, 347138, 298510, 163254, 1141840, 542630, 99841, 752765, -252949, 914424, 679524, 514377, 462102, 159782, 878810, -946748, 340335, 292032, 502266, 265852, 851017, -549615, 290162, 755391, 1073202, 313000, 241132, 1036589, 853904, -388932, 982952, 537759, 547784, -496214, 854181, 934719, -288531, -184383, 659541, -1149123, 355882, 662284, 518681, -748256, -910775, 951227, 898241, -729004, -112209, 516313, 607208, 382539]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('Analysis.csv', index=False)

import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Analysis.csv')

# Calculate the total number of months
total_months = len(df)

# Calculate the net total amount of "Profit/Losses"
net_profit_losses = df['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
df['Profit/Losses Change'] = df['Profit/Losses'].diff()

# Calculate the average of the changes
average_change = df['Profit/Losses Change'].mean()

# Calculate the greatest increase in profits (date and amount)
max_increase = df['Profit/Losses Change'].max()
max_increase_date = df.loc[df['Profit/Losses Change'] == max_increase, 'Date'].values[0]

# Calculate the greatest decrease in profits (date and amount)
max_decrease = df['Profit/Losses Change'].min()
max_decrease_date = df.loc[df['Profit/Losses Change'] == max_decrease, 'Date'].values[0]

# Print the results
print(f"Total Months: {total_months}")
print(f"Net Total Amount of Profit/Losses: ${net_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase:.0f})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease:.0f})")

