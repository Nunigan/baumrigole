import matplotlib.pyplot as plt
import glob
import matplotlib.dates as mdates
import pandas as pd

def plot():

    measurement_names = ['TIMESTAMP', 'RECORD', 'BattV_Avg', 'PTemp_C_Avg', 'VWC_5cm_Avg', 'Ka_5cm_Avg', 'T_5cm_Avg', 'BulkEC_5cm_Avg', 'VWC_10cm_Avg', 'Ka_10cm_Avg', 'T_10cm_Avg', 'BulkEC_10cm_Avg', 'VWC_20cm_Avg', 'Ka_20cm_Avg', 'T_20cm_Avg', 'BulkEC_20cm_Avg', 'VWC_30cm_Avg', 'Ka_30cm_Avg', 'T_30cm_Avg', 'BulkEC_30cm_Avg', 'VWC_40cm_Avg', 'Ka_40cm_Avg', 'T_40cm_Avg', 'BulkEC_40cm_Avg', 'VWC_50cm_Avg', 'Ka_50cm_Avg', 'T_50cm_Avg', 'BulkEC_50cm_Avg', 'Temp_C_Avg', 'SlrFD_W_Avg', 'Rain_mm_Tot', 'Strikes_Tot', 'Dist_km_Avg', 'WS_ms_S_WVT', 'WindDir_D1_WVT', 'WindDir_SD1_WVT', 'MaxWS_ms_Avg', 'AirT_C_Avg', 'VP_mbar_Avg', 'BP_mbar_Avg', 'RH', 'RHT_C']

    filenames = sorted(glob.glob("/data/data/*.csv"))
    # filenames = sorted(glob.glob("../../data/*.csv"))

    dfs = []
    for f in filenames:
        dfs.append(pd.read_csv(f))

    df = pd.concat(dfs)
    df.columns = measurement_names
    df = df.astype({"TIMESTAMP": 'datetime64[s]'})
    df = df.drop_duplicates(keep='first')
    df.sort_values(by='TIMESTAMP', inplace = True)

    plt.rcParams.update({'font.size': 20})
    fig, ax = plt.subplots(1, 1, sharex=True, figsize=(16,9))
    ax.plot(df['TIMESTAMP'], df['Temp_C_Avg'])
    ax.set_title('Temperature')
    ax.set_ylabel(r"Temperature $\it{°C}$")
    ax.grid()
    ax.set_xlabel(r"Time")
    ax.tick_params(axis='x', rotation=20)
    ax.xaxis.set_major_locator(mdates.HourLocator(range(0,24,2)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    plt.savefig('static/temp.jpg', dpi=300)
    plt.close()