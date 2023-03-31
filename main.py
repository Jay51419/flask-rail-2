from flask import Flask, jsonify,request,send_file
from flask_uploads import UploadSet, IMAGES,configure_uploads
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
@app.route('/')
def index():
    return "Jz Here"

@app.route('/upload',methods=["POST"])
def upload_image():
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return jsonify({'filename': filename})
    return jsonify({'error': 'No file uploaded'})

@app.route('/image/<filename>')
def image(filename):
    mimetype = 'image/' + str(filename.split(".")[1])
    print(mimetype)
    print()
    return send_file(os.getcwd()+"/uploads/"+filename, mimetype=mimetype)
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
