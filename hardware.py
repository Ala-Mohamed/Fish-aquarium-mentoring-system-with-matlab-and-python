import numpy as np
import matplotlib.pyplot as plt

# Import the data
temperature_readings = np.array([25.00, 25.01, 25.02, 25.03, 25.04, 25.05, 25.06, 25.07, 25.08, 25.09, 25.10, 25.11, 25.12, 25.13, 25.14, 25.15, 25.16, 25.17, 25.18, 25.19, 25.20, 25.21, 25.22, 25.23, 25.24])
pH_readings = np.array([7.00, 7.01, 7.02, 7.03, 7.04, 7.05, 7.06, 7.07, 7.08, 7.09, 7.10, 7.11, 7.12, 7.13, 7.14, 7.15, 7.16, 7.17, 7.18, 7.19, 7.20, 7.21, 7.22, 7.23, 7.24])

# Plot the data
plt.plot(temperature_readings, pH_readings, 'o')
plt.xlabel('Temperature')
plt.ylabel('pH')
plt.show()

# Fit a line to the data
line = np.polyfit(temperature_readings, pH_readings, 1)

# Print the slope and y-intercept
print('Slope:', line[0])
print('Y-intercept:', line[1])

# Predict the pH for a given temperature
temperature = 25
pH = line[0] * temperature + line[1]
print('pH at 25 degrees Celsius:', pH)