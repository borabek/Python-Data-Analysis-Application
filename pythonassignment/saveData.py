import pandas as pd
#data in a list
data = [[101, 50.5, 23],
        [103, 45.90, 34],
        [105, 70.90, 19]]
#create pandas Dataframe with column name
df = pd.DataFrame(data, columns= ["ID", "Weight", "Age"])
#Save the Dataframe into a CSV file
#index=False argument ensures that the DataFrame's index is not included in the CSV file.
df.to_csv("sampleData-1.csv", index= True)
print("numerical Data saved in a csv file, called sampleData-1")