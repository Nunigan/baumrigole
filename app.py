from flask import Flask, render_template, Response, request, send_file
# import cv2
# from imutils.video import VideoStream
import glob
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from plot import plot

# def dowload_cloud():
#     t = time.time()
#     print('Download from cloud')
#     account_url = "https://baumrigole.blob.core.windows.net"
#     default_credential = DefaultAzureCredential()
#     blob_service_client = BlobServiceClient(account_url, credential=default_credential)
#     container_name = 'baumrigoledata'
#     container_client = blob_service_client.get_container_client(container=container_name)

#     filenames_local = sorted(glob.glob("data/*.csv"))

#     blob_list = container_client.list_blobs()
#     for blob in blob_list:
#         if 'data' in blob.name:
#             if blob.name in filenames_local:
#                 if os.stat(blob.name).st_size == blob.size:
#                     continue
#             name = blob.name
#             with open(file=name, mode="wb") as download_file:
#                 download_file.write(container_client.download_blob(blob.name).readall())
#     print(time.time() - t)



app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    plot()
    filenames = glob.glob("/data/data/*.csv")
    for i, files in enumerate(filenames):
        filenames[i] = files[5:]


    return render_template('index.html',data=filenames)

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('file_select')
    return send_file("/data{}".format(select), as_attachment=True)

@app.route('/show/')
def show():
    # fileList = glob.glob('static/temp2023*', recursive=True)
    # for filePath in fileList:
    #     try:
    #         os.remove(filePath)
    #     except OSError:
    #         print("Error while deleting file")
    
    # name = 'temp{}.jpg'.format(datetime.today().strftime('%Y_%m_%d_%H:%M:%S'))
    # shutil.copyfile('static/temp.jpg', 'static/'+name)
    name = 'temp.jpg'
    return render_template('show.html',  user_image=name)
    # return render_template('show.html')

# @app.route('/stream/')
# def stream():
#     return Response(gather_img(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/plot/')
# def plot():
#     return Response(gather_plot(), mimetype='multipart/x-mixed-replace; boundary=frame')

# def gather_img():
#     cap = VideoStream('http://icai:icai@169.254.179.163/mjpg/video.mjpg').start()
#     while True:
#         img = cap.read()
#         _, frame = cv2.imencode('.jpg', img)
#         yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')
#         time.sleep(0.2)

# def gather_plot():

#     img = cv2.imread('flask/static/temp.jpg')
#     cv2.imwrite('flask/static/test.jpg', img)
#     encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
#     _, frame = cv2.imencode('.jpg', img, encode_param)
#     yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')

if __name__ == '__main__':

    app.run()
    # dowload_cloud()