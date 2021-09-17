import pandas as pd

# TASK 1
TASK_1_OUTPUT = pd.read_csv('data/TASK_1_OUTPUT.csv')

# TASK 2
TASK_2_PART_1_OUTPUT = pd.read_csv('data/TASK_2_PART_1_OUTPUT.csv', parse_dates=[9])
TASK_2_PART_2_T10_OUTPUT = pd.read_csv('data/TASK_2_PART_2_T10_OUTPUT.csv', index_col=0, header=None, squeeze=True)
TASK_2_PART_2_BKN_OUTPUT = pd.read_csv('data/TASK_2_PART_2_BKN_OUTPUT.csv')
TASK_2_PART_2_RM_PRICES_OUTPUT = pd.read_csv("data/TASK_2_PART_2_RM_PRICES_OUTPUT.csv")

# TASK 3
TASK_3_PART_1_OUTPUT = pd.read_csv('data/TASK_3_PART_1_OUTPUT.csv')
TASK_3_PART_2_OUTPUT = pd.read_csv('data/TASK_3_PART_2_OUTPUT.csv')

# TASK 4
TASK_4_PART_1_OUTPUT = pd.read_csv('data/TASK_4_PART_1_OUTPUT.csv')

# TASK 5
TASK_5_PART_1_OUTPUT = pd.read_csv('data/TASK_5_PART_1_OUTPUT.csv')
TASK_5_PART_2_OUTPUT = pd.read_csv('data/TASK_5_PART_2_OUTPUT.csv',header=None)



# TASK 6
TASK_6_PART_1_OUTPUT_1 = pd.read_csv('data/TASK_6_PART_1_OUTPUT_1.csv')
TASK_6_PART_1_OUTPUT_2 = pd.read_csv('data/TASK_6_PART_1_OUTPUT_2.csv')
TASK_6_PART_1_OUTPUT_3 = pd.read_csv('data/TASK_6_PART_1_OUTPUT_3.csv', header=None)
TASK_6_PART_1_OUTPUT_4 = pd.read_csv('data/TASK_6_PART_1_OUTPUT_4.csv', header=None)
TASK_6_PART_2_OUTPUT = pd.read_csv('data/TASK_6_PART_2_OUTPUT.csv')
TASK_6_PART_3_OUTPUT = pd.read_csv('data/TASK_6_PART_3_OUTPUT.csv')