from funktionen import importSynthload, initializeLoadProfile, addLoad, pickDay
import pandas as pd

#def test_importSynthload():
#    assert importSynthload().iloc[0,0] == 0.02713
#    assert importSynthload().iloc[100,20] == 0.10164
#    assert importSynthload().iloc[0,26] == 0.05906
#    assert importSynthload().iloc[35135,26] == 0.05906


def test_initializeLoadProfile():
    df_test = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]})
    df_test.set_index('col1', inplace=True)

    assert initializeLoadProfile(df_test).reset_index().iloc[0,0] == 1
    assert initializeLoadProfile(df_test).reset_index().iloc[3,0] == 4
    assert initializeLoadProfile(df_test).reset_index().iloc[0,1] == 0
    assert initializeLoadProfile(df_test).reset_index().iloc[3,1] == 0

def test_addLoad():
    df_synth_test = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8], 'col2': [9, 10, 11, 12], 'col3': [13, 14, 15, 16], 'col4': [17, 18, 19, 20]})
    df_synth_test.set_index('col1', inplace=True)

    df_load_test = pd.DataFrame({'col1': [1, 2, 3, 4], 'load': [1, 2, 3, 4]})
    df_load_test.set_index('col1', inplace=True)

    assert addLoad(df_synth_test, df_load_test, 'col2', 1).iloc[0,0] == 37
    assert addLoad(df_synth_test, df_load_test, 'col2', 1).iloc[3,0] == 52
    assert addLoad(df_synth_test, df_load_test, 'col4', 2).iloc[0,0] == 137
    assert addLoad(df_synth_test, df_load_test, 'col4', 2).iloc[3,0] == 164

def test_pickDay():
    df_load_test = pd.DataFrame({'time': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03', '2024-01-04', '2024-01-04'], 'load': [1, 2, 3, 4, 5, 6, 7, 8]})
    df_load_test['time'] = pd.to_datetime(df_load_test['time'])
    df_load_test.set_index('time', inplace=True)

    assert pickDay(df_load_test, 2).iloc[0,0] == 3
    assert pickDay(df_load_test, 2).iloc[1,0] == 4
    assert pickDay(df_load_test, 4).iloc[0,0] == 7
    assert pickDay(df_load_test, 4).iloc[1,0] == 8





