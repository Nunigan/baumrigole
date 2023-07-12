# from flask import Flask, render_template, Response, request, send_file
# # import cv2
# # from imutils.video import VideoStream
# import glob
# from azure.identity import DefaultAzureCredential
# from azure.storage.blob import BlobServiceClient
# # from plot import plot
# import time

# # def dowload_cloud():
# #     t = time.time()
# #     print('Download from cloud')
# #     account_url = "https://baumrigole.blob.core.windows.net"
# #     default_credential = DefaultAzureCredential()
# #     blob_service_client = BlobServiceClient(account_url, credential=default_credential)
# #     container_name = 'baumrigoledata'
# #     container_client = blob_service_client.get_container_client(container=container_name)

# #     filenames_local = sorted(glob.glob("data/*.csv"))

# #     blob_list = container_client.list_blobs()
# #     for blob in blob_list:
# #         if 'data' in blob.name:
# #             if blob.name in filenames_local:
# #                 if os.stat(blob.name).st_size == blob.size:
# #                     continue
# #             name = blob.name
# #             with open(file=name, mode="wb") as download_file:
# #                 download_file.write(container_client.download_blob(blob.name).readall())
# #     print(time.time() - t)



# app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     # t = time.time()
#     # plot()
#     # print(time.time() - t)
#     filenames = sorted(glob.glob("/data/data/*.csv"))
#     filenames = glob.glob("/data/data/*.csv")
#     for i, files in enumerate(filenames):
#         filenames[i] = files[11:]

#     return render_template('index.html',data=filenames)

# @app.route("/test" , methods=['GET', 'POST'])
# def test():
#     select = request.form.get('file_select')
#     return send_file("/data/data/{}".format(select), as_attachment=True)

# @app.route('/show/')
# def show():
#     # fileList = glob.glob('static/temp2023*', recursive=True)
#     # for filePath in fileList:
#     #     try:
#     #         os.remove(filePath)
#     #     except OSError:
#     #         print("Error while deleting file")
    
#     # name = 'temp{}.jpg'.format(datetime.today().strftime('%Y_%m_%d_%H:%M:%S'))
#     shutil.copyfile('/data/data/temp.jpg', 'static/temp.jpg')
#     shutil.copyfile('/data/data/cam.jpg', 'static/cam.jpg')
#     shutil.copyfile('/data/data/climavue.jpg', 'static/climavue.jpg')
#     shutil.copyfile('/data/data/soilvue.jpg', 'static/soilvue.jpg')

#     # shutil.copyfile('../../data/temp.jpg', 'static/temp.jpg')
#     # shutil.copyfile('../../data/cam.jpg', 'static/cam.jpg')
#     # shutil.copyfile('../../data/climavue.jpg', 'static/climavue.jpg')
#     # shutil.copyfile('../../data/soilvue.jpg', 'static/soilvue.jpg')

#     temp = 'temp.jpg'
#     cam = 'cam.jpg'
#     soil = 'soilvue.jpg'
#     clima = 'climavue.jpg'

#     return render_template('show.html', temp=temp, cam=cam, soil=soil, clima=clima)
#     # return render_template('show.html')

# # @app.route('/stream/')
# # def stream():
# #     return Response(gather_img(), mimetype='multipart/x-mixed-replace; boundary=frame')

# # @app.route('/plot/')
# # def plot():
# #     return Response(gather_plot(), mimetype='multipart/x-mixed-replace; boundary=frame')

# # def gather_img():
# #     cap = VideoStream('http://icai:icai@169.254.179.163/mjpg/video.mjpg').start()
# #     while True:
# #         img = cap.read()
# #         _, frame = cv2.imencode('.jpg', img)
# #         yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')
# #         time.sleep(0.2)

# # def gather_plot():

# #     img = cv2.imread('flask/static/temp.jpg')
# #     cv2.imwrite('flask/static/test.jpg', img)
# #     encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
# #     _, frame = cv2.imencode('.jpg', img, encode_param)
# #     yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')

# if __name__ == '__main__':

#     app.run()
#     # dowload_cloud()



from flask import Flask, render_template, request, send_file
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import glob
import shutil

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    # t = time.time()
    # plot()
    # print(time.time() - t)
    filenames = sorted(glob.glob("/data/data/*.csv"))
    filenames = glob.glob("/data/data/*.csv")
    for i, files in enumerate(filenames):
        filenames[i] = files[11:]

    return render_template('index.html',data=filenames)

@app.route('/show/')
def show():
    # fileList = glob.glob('static/temp2023*', recursive=True)
    # for filePath in fileList:
    #     try:
    #         os.remove(filePath)
    #     except OSError:
    #         print("Error while deleting file")
    
    # name = 'temp{}.jpg'.format(datetime.today().strftime('%Y_%m_%d_%H:%M:%S'))
    shutil.copyfile('/data/data/temp.jpg', 'static/temp.jpg')
    shutil.copyfile('/data/data/cam.jpg', 'static/cam.jpg')
    shutil.copyfile('/data/data/climavue.jpg', 'static/climavue.jpg')
    shutil.copyfile('/data/data/soilvue.jpg', 'static/soilvue.jpg')
    shutil.copyfile('/data/data/stats.jpg', 'static/stats.jpg')

    # shutil.copyfile('../../data/temp.jpg', 'static/temp.jpg')
    # shutil.copyfile('../../data/cam.jpg', 'static/cam.jpg')
    # shutil.copyfile('../../data/climavue.jpg', 'static/climavue.jpg')
    # shutil.copyfile('../../data/soilvue.jpg', 'static/soilvue.jpg')

    temp = 'temp.jpg'
    cam = 'cam.jpg'
    soil = 'soilvue.jpg'
    clima = 'climavue.jpg'
    stats = 'stats.jpg'
    return render_template('show.html', temp=temp, cam=cam, soil=soil, clima=clima, stats=stats)

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('file_select')
    return send_file("/data/data/{}".format(select), as_attachment=True)

@app.route('/plot/')
def plot():
    fig = get_fig()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('plot.html', graphJSON=graphJSON)

@app.route('/select/')
def select():
    fig = get_fig_select()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('select.html', graphJSON=graphJSON)

def get_fig():
    df = pd.read_csv('/data/data/all.csv', header=0, parse_dates=[0], index_col=[0])
    rain = df['Rain_mm_Tot']
    strikes = df['Strikes_Tot']
    df = df.resample('60T').mean().ffill()
    rain = rain.resample('60T').sum()
    strikes = strikes.resample('60T').sum()

    fig = make_subplots(rows=5, cols=1, shared_xaxes=True
                        ,specs=[[{"secondary_y": True}], 
                                [{"secondary_y": False}], 
                                [{"secondary_y": False}], 
                                [{"secondary_y": False}],
                                [{"secondary_y": False}]],
                                vertical_spacing = 0.02
                                )

    fig.add_trace(
        go.Scatter(x=df.index, y=df["AirT_C_Avg"], mode='lines', name='Temperature')
        , row=1, col=1, secondary_y=False)

    fig.add_trace(
        go.Scatter(x=df.index, y=df["RH"], mode='lines', name='Humidity')
        , row=1, col=1, secondary_y=True)

    cum_rain = np.cumsum(rain)
    fig.append_trace(go.Scatter(x=df.index , y=cum_rain, name='cumsum rain')
    , row=2, col=1)
    fig.append_trace(go.Scatter(x=rain.index , y=rain, name='rain')
    , row=2, col=1)

    for s in ["5cm","10cm","20cm","30cm","40cm","50cm"]:
        fig.append_trace(
            go.Scatter(x=df.index, y=df['T_{}_Avg'.format(s)], mode='lines', name='Temp @ {}'.format(s))
            , row=3, col=1)


    for s in ["5cm","10cm","20cm","30cm","40cm","50cm"]:
        fig.append_trace(
            go.Scatter(x=df.index, y=df["VWC_{}_Avg".format(s)], mode='lines', name='VWC @ {}'.format(s))
            , row=4, col=1)

    df_2d = pd.concat([df['VWC_10cm_Avg'], df['VWC_20cm_Avg'],df['VWC_30cm_Avg'],df['VWC_40cm_Avg'],df['VWC_50cm_Avg']], axis=1)
    z = np.swapaxes(np.array(df_2d), 0, 1)
    y = np.array([10, 20, 30, 40, 50])
    x = df_2d.index

    fig.append_trace(
        go.Contour(z=z,x=x,y=y,colorscale='Blues', showscale=False,contours=dict(showlabels = True), name='VWC'),
            row=5, col=1)


    fig.update_yaxes(title_text=r"VWC (m^3/m^3)", row=4, col=1)
    fig.update_yaxes(title_text=r"Depth (cm)", row=5, col=1)
    fig.update_yaxes(title_text=r"Soil Temp (°C)", row=3, col=1)
    fig.update_yaxes(title_text=r"Rain (mm)", row=2, col=1)
    fig.update_xaxes(title_text=r"Time", row=5, col=1)
    fig.update_yaxes(title_text=r"Temp (°C)", row=1, col=1, secondary_y=False)
    fig.update_yaxes(title_text=r"Humidity (%)", row=1, col=1, secondary_y=True)
    fig.update_yaxes(autorange="reversed", row=5, col=1)
    fig.update_xaxes(showticklabels=True) 

    fig.update_layout(height=2000, width=1700, title='Weather station and soil water content profile sensor')

    return fig



def get_fig_select():

    df = pd.read_csv('/data/data/all.csv', header=0, parse_dates=[0], index_col=[0])
    rain = df['Rain_mm_Tot']
    strikes = df['Strikes_Tot']
    df = df.resample('60T').mean().ffill()
    rain = rain.resample('60T').sum()
    strikes = strikes.resample('60T').sum()

    fig = go.Figure()

    columns = ['VWC_5cm_Avg', 'Ka_5cm_Avg', 'T_5cm_Avg', 'BulkEC_5cm_Avg', 'VWC_10cm_Avg', 'Ka_10cm_Avg', 'T_10cm_Avg', 'BulkEC_10cm_Avg', 'VWC_20cm_Avg', 'Ka_20cm_Avg', 'T_20cm_Avg', 'BulkEC_20cm_Avg', 'VWC_30cm_Avg', 'Ka_30cm_Avg', 'T_30cm_Avg', 'BulkEC_30cm_Avg', 'VWC_40cm_Avg', 'Ka_40cm_Avg','T_40cm_Avg', 'BulkEC_40cm_Avg', 'VWC_50cm_Avg', 'Ka_50cm_Avg','T_50cm_Avg', 'BulkEC_50cm_Avg', 'Temp_C_Avg', 'SlrFD_W_Avg', 'Rain_mm_Tot', 'Strikes_Tot', 'Dist_km_Avg', 'WS_ms_S_WVT', 'WindDir_D1_WVT', 'WindDir_SD1_WVT', 'MaxWS_ms_Avg', 'AirT_C_Avg', 'VP_mbar_Avg', 'BP_mbar_Avg', 'RH', 'RHT_C']
    off  =    [False        , False       , False      , False           , False         ,  False       , False       , False            , False         , False        , False       ,  False           ,False          , False        , False       , False           , False         ,  False       ,False        , False            , False         , False        , False      ,  False           ,False        , False        , False        , False        , False        , False        ,  False       , False           , False            , False         , False       , False        ,  False       , False , False]
    vwc   =   [True         , False       , False      , False           , True          ,  False       , False       , False            , True          , False        , False       ,  False           ,True           , False        , False       , False           , True          ,  False       ,False        , False            , True          , False        , False      ,  False           ,False        , False        , False        , False        , False        , False        ,  False       , False           , False            , False         , False       , False        ,  False       , False , False]
    ka    =   [False        , True        , False      , False           , False         ,  True        , False       , False            , False         , True         , False       ,  False           ,False          , True         , False       , False           , False         ,  True        ,False        , False            , False         , True         , False      ,  False           ,False        , False        , False        , False        , False        , False        ,  False       , False           , False            , False         , False       , False        ,  False       , False , False]
    bulk  =   [False        , False       , False      , True            , False         ,  False       , False       , True             , False         , False        , False       ,  True            ,False          , False        , False       , True            , False         ,  False       ,False        , True             , False         , False        , False      ,  True            ,False        , False        , False        , False        , False        , False        ,  False       , False           , False            , False         , False       , False        ,  False       , False , False]
    T    =    [False        , False       , True       , False           , False         ,  False       , True        , False            , False         , False        , True        ,  False           ,False          , False        , True        , False           , False         ,  False       ,True         , False            , False         , False        , True       ,  False           ,False        , False        , False        , False        , False        , False        ,  False       , False           , False            , False         , False       , False        ,  False       , False , False]
    Temp =    [False        , False       , False      , False           , False         ,  False       , False       , False            , False         , False        , False       ,  False           ,False          , False        , False       , False           , False         ,  False       ,False        , False            , False         , False        , False      ,  False           ,True         , False        , False        , False        , False        , False        ,  False       , False           , False            , False         , False       , False        ,  False       , False , False]
    solar=    [False        , False       , False      , False           , False         ,  False       , False       , False            , False         , False        , False       ,  False           ,False          , False        , False       , False           , False         ,  False       ,False        , False            , False         , False        , False      ,  False           ,False        , True         , False        , False        , False        , False        ,  False       , False           , False            , False         , False       , False        ,  False       , False , False]
    strike=   [False        , False       , False      , False           , False         ,  False       , False       , False            , False         , False        , False       ,  False           ,False          , False        , False       , False           , False         ,  False       ,False        , False            , False         , False        , False      ,  False           ,False        , False        , False        , False        , True        , False        ,  False       , False           , False            , False         , False       , False        ,  False       , False , False]
    rh    =   [False        , False       , False      , False           , False         ,  False       , False       , False            , False         , False        , False       ,  False           ,False          , False        , False       , False           , False         ,  False       ,False        , False            , False         , False        , False      ,  False           ,False        , False        , False        , False        , False        , False        ,  False       , False           , False            , False         , False       , False        ,  False       , True , False]
    BP   =    [False        , False       , False      , False           , False         ,  False       , False       , False            , False         , False        , False       ,  False           ,False          , False        , False       , False           , False         ,  False       ,False        , False            , False         , False        , False      ,  False           ,False        , False        , False        , False        , False        , False        ,  False       , False           , False            , False         , False       , False        ,  True       , False , False]
    vp   =    [False        , False       , False      , False           , False         ,  False       , False       , False            , False         , False        , False       ,  False           ,False          , False        , False       , False           , False         ,  False       ,False        , False            , False         , False        , False      ,  False           ,False        , False        , False        , False        , False        , False        ,  False       , False           , False            , False         , False       , True        ,  False       , False , False]
    r  =    [False        , False       , False      , False           , False         ,  False       , False       , False            , False         , False        , False       ,  False           ,False          , False        , False       , False           , False         ,  False       ,False        , False            , False         , False        , False      ,  False           ,False        , False          , True         , True         , False        , False        ,  False       , False           , False            , False         , False       , False        ,  False       , False , False]

    for column in columns:
        if column == 'Rain_mm_Tot':
            cum_rain = np.cumsum(rain)
            fig.add_trace(
                go.Scatter(
                    x = rain.index,
                    y = rain,
                    name = column
                )
            )
            fig.add_trace(
                go.Scatter(
                    x = rain.index,
                    y = cum_rain,
                    name = 'cumulative sum rain'
                )
            )
        elif column=='Strikes_Tot':
            fig.add_trace(
                go.Scatter(
                    x = strikes.index,
                    y = strikes,
                    name = column
                )
            )
        else:
            fig.add_trace(
            go.Scatter(
                x = df.index,
                y = df[column],
                name = column
            )
        )
        
    fig.update_layout(
        updatemenus=[go.layout.Updatemenu(
            active=0,
            buttons=list(
                [dict(label = 'None',
                    method = 'update',
                    args = [{'visible': off},
                            {'title': 'None',
                            'showlegend':True}]),
                dict(label = 'VWC',
                    method = 'update',
                    args = [{'visible': vwc}, # the index of True aligns with the indices of plot traces
                            {'title': 'Volumetric Water Content (m^3/m^3)',
                            'showlegend':True}]),
                dict(label = 'Permittivity',
                    method = 'update',
                    args = [{'visible': ka},
                            {'title': 'Permittivity',
                            'showlegend':True}]),
                dict(label = 'Bulk',
                    method = 'update',
                    args = [{'visible': bulk},
                            {'title': 'Bulk Electrical Conductivity (dS/m)',
                            'showlegend':True}]),
                dict(label = 'Soil_T',
                    method = 'update',
                    args = [{'visible': T},
                            {'title': 'Soil Temperature (°C)',
                            'showlegend':True}]),
                dict(label = 'Temperature',
                    method = 'update',
                    args = [{'visible': Temp},
                            {'title': 'Temperature (°C)',
                            'showlegend':True}]),
                dict(label = 'SFD',
                    method = 'update',
                    args = [{'visible': solar},
                            {'title': 'Solar Flux Density (W/m^2)',
                            'showlegend':True}]),
                dict(label = 'rH',
                    method = 'update',
                    args = [{'visible': rh},
                            {'title': 'relative Humidity (%)',
                            'showlegend':True}]),
                dict(label = 'BP',
                    method = 'update',
                    args = [{'visible': BP},
                            {'title': 'Barometric Pressure (mbar)',
                            'showlegend':True}]),
                dict(label = 'VP',
                    method = 'update',
                    args = [{'visible': vp},
                            {'title': 'Vapor Pressure (mbar)',
                            'showlegend':True}]),
            dict(label = 'Strikes',
                    method = 'update',
                    args = [{'visible': strike},
                            {'title': 'Lightning strikes (tot)',
                            'showlegend':True}]),
                dict(label = 'Rain',
                    method = 'update',
                    args = [{'visible': r},
                            {'title': 'Rain (mm, mm/h)',
                            'showlegend':True}]),
                ])
            )
        ])

    return fig

if __name__ == '__main__':

    app.run()
    # fig = get_fig()
    # fig.show()
