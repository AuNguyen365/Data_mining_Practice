import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

# Tạo dataframe
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target

# Hiển thị đặc trưng
print("Features:")
print(iris.feature_names)

# Hiển thị nhãn
print("\nLabels:")
print(iris.target_names)

# Xem dữ liệu
print("\nFirst 5 rows:")
print(df.head())

# Thông tin dataset
print("\nDataset Info:")
print(df.info())