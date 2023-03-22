import pandas as pd
import os
df = pd.read_excel("../data/raw_data.xlsx", sheet_name = "data")
#allowed_col = ["country","year","aAll_9","aUrban_9","aRural_9","aMale_9","aFemale_9","aMalUrb_9","aMalRur_9","aFemUrb_9","aFemRur_9","aQuint1_9","aQuint2_9","aQuint3_9","aQuint4_9","aQuint5_9","aQuint1M_9","aQuint2M_9","aQuint3M_9","aQuint4M_9","aQuint5M_9","aQuint1F_9","aQuint2F_9","aQuint3F_9","aQuint4F_9","aQuint5F_9"]
allowed_col = ["country", "year"]
for i in df.columns:
    if i.startswith("a") and "x_" not in i and "Quint" not in i:
        allowed_col.append(i)
attained_grades_col = []
for col in allowed_col:
    if "_" in col:
        if col.split("_")[0] not in attained_grades_col:
            attained_grades_col.append(col.split("_")[0])
new_df = df[allowed_col].copy()
new_df = new_df.sort_values("year", ascending=False).drop_duplicates(["country"])
new_df = pd.wide_to_long(new_df, attained_grades_col, i = "country", j='attained_grade', sep='_')
rename_col = []
age_group_col = []
for i in new_df.columns:
    if i in attained_grades_col:    
        need_to_append = True
        if i.startswith("a2"):
            i = i[2:] + "_20to29"
        elif i.startswith("a3"):
            i = i[2:] + "_30to39"
        elif i.startswith("a4"):
            i = i[2:] + "_40to49"
        elif i.startswith("a"):
            i = i[1:] + "_15to19"
        else:
            need_to_append = False
        if need_to_append:
            if i.split("_")[0] not in age_group_col:
                age_group_col.append(i.split("_")[0])
    rename_col.append(i)
new_df.columns = rename_col
new_df = new_df.reset_index()
new_df = pd.wide_to_long(new_df, age_group_col, i = ["country", "attained_grade"], j='age_group', sep='_', suffix = r'\w+')
output_file = "../data/processed_data.csv"
if os.path.exists(output_file):
    os.remove(output_file)
new_df.to_csv("../data/processed_data.csv")

