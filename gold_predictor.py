import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dates = np.arange(1, 11)
actual_prices = [1900, 1910, 1905, 1920, 1930, 1925, 1935, 1940, 1950, 1960]
predicted_prices = [1905, 1908, 1910, 1915, 1925, 1930, 1932, 1945, 1955, 1965]

data = {
    'Day': dates,
    'Actual Price': actual_prices,
    'Predicted Price': predicted_prices
}
df = pd.DataFrame(data)

# 👇 Correct way
print("🔹 DataFrame Head:")
print(df.head())

print("\n🔹 DataFrame Info:")
df.info()  # ✅ DO NOT use print() here

# Chart
plt.plot(dates, actual_prices, marker='o', label='Actual')
plt.plot(dates, predicted_prices, marker='x', label='Predicted')
plt.title('Gold Price Prediction')
plt.xlabel('Day')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()


