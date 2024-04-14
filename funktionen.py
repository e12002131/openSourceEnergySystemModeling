import pandas as pd
import numpy as np # make ruff fail


# imports synthload2024.xlsx as DataFrame
def importSynthload():
    # read and save synthload2024.xlsx
    df_import = pd.read_excel("synthload2024.xlsx")

    # time column has no name --> rename to 'time'
    df_import.rename(columns={"Unnamed: 0": "time"}, inplace=True)

    # delete description row
    df_import.drop([0], inplace=True)

    # convert column 'time' to DateTime type
    df_import["time"] = pd.to_datetime(df_import["time"])

    # set column 'time' as new index for Dataframe
    df_import.set_index("time", inplace=True)

    return df_import


# initialize a DataFrame for storing a load profile
def initializeLoadProfile(df_synthload_in):
    # copy the index column of a given DataFrame to the load profile DataFrame, so that the timestamps match
    df_initialize_load_profile = df_synthload_in.copy(deep=True).iloc[:, 0:0]

    # create column 'load' and set entries to '0'
    df_initialize_load_profile["load"] = 0

    return df_initialize_load_profile


# adds a synthload to an existing load profile DataFrame 'df_load_profile_in' (values in W)
# 'df_synthload_in' is the Dataframe where all standard synthloads are stored
# 'load_profile' is the df_synthload_in column name as String
# 'yearly_energy_consumption' is the yearly consumed electrical energy of the given profile type in kWh
def addLoad(
    df_synthload_in, df_load_profile_in, load_profile, yearly_energy_consumption
):
    # copy DataFrame so that original isn't edited
    df_load_profile_temp = df_load_profile_in.copy(deep=True)

    # multiplied with 4 because the values in synthload profiles are energy per 15 minutes instead of power
    df_load_profile_temp["load"] = (
        df_load_profile_temp["load"]
        + df_synthload_in[load_profile] * yearly_energy_consumption # make tests fail, removed * 4
    )

    return df_load_profile_temp


# returns a single day of 'df_load_profile_in' defined in day_of_year as integer
def pickDay(df_load_profile_in, day_of_year):
    # copy DataFrame so that original isn't edited
    df_load_profile_temp = df_load_profile_in.copy(deep=True)

    # create column 'day of year'
    df_load_profile_temp["day of year"] = df_load_profile_temp.index.dayofyear

    # select entries where column 'day of year' == given variable 'day_of_year'
    df_load_profile_temp = df_load_profile_temp.where(
        df_load_profile_temp["day of year"] == day_of_year + 1 # make tests fail addet + 1
    )

    # delete NaN entries (everywhere where column 'day of year' != 'day_of_year')
    df_load_profile_temp.dropna(inplace=True)

    # delete column 'day of year'
    del df_load_profile_temp["day of year"]

    return df_load_profile_temp
