import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Make the data frame
soft = pd.read_csv('XtraSoft.csv')
# Maybe rename
# soft.columns = ['NA', 'NA', 'time', 'size', 'displacement', 'force']

# Raw, for checking
plt.plot(soft.Time_S, soft.Force_N)
plt.show()

# Stress Relaxation Data Trimmming It usually takes a few seconds for the machine to get to the desired displacement.
# This machine specifically takes 5 seconds. To make the code extensible for data from other machines, we are going to
# start the subset when max force is achieved

# get index of max force for: (1) Strain, (2) Data Trimming
# get max force row to verify max
maxRow = soft.loc[soft['Force_N'].idxmax()]
print(maxRow)

# get index of max force
indexMaxF = np.argmax(np.array(soft['Force_N']))
print(indexMaxF)

# (1) Strain = displacement / original length
# original length = size before compression = size @index 0
length = soft.Size_mm.iloc[0]

# Max displacement occurs at maxF
displacement = soft.Displacement_mm.iloc[indexMaxF]

# Strain is constant for stress relaxation tests
strain = displacement / length

# (2) Data Trimming
# soft.drop(soft.index[0:indexMaxF], 0, inplace=True)
# Alt. way to Trim. Take subset of data where displacement (and thus strain) is const. This trims both start and end
soft = soft[soft.Displacement_mm == displacement]

plt.plot(soft.Time_S, soft.Force_N)
plt.title("Beginning Trimmed Data")
plt.xlabel("Time (seconds)")
plt.ylabel("Force (N)")
plt.show()

# Need Stress v. Time. Stress (MPa) = Force (N) / Area (mm^2)
# Dimensions measured beforehand, maybe find a way to make this more extensible
area = 62.95*51.79
plt.plot(soft.Time_S, soft.Force_N / area)
plt.title("Experimental Data for Extra Soft Foam Specimen")
plt.xlabel("Time (seconds)")
plt.ylabel("Stress (MPa)")
plt.show()

# Calculate models
