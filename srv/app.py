from flask import Flask, request
from pyzbar.pyzbar import decode
import pytesseract
from PIL import Image
import io

app = Flask(__name__)


@app.route('/barcode', methods=['POST'])
def get_barcode_from_file():
    file = request.files['file']
    return str(get_barcode(file.stream.read()))


@app.route('/text', methods=['POST'])
def get_text_from_file():
    file = request.files['file']
    return str(get_text(file.stream.read()))


def get_barcode(file) -> object:
    barcode_data = decode(Image.open(fp=io.BytesIO(file)))
    """ The pyzbar function 'decode' returns a list having
    'namedtuple' object inside (from pyzbar.pyzbar, row 26):
    Decoded = namedtuple('Decoded', 'data type rect polygon quality orientation')
    To access tuple elements, use indices. 
    """
    # Get Data
    content = str(barcode_data[0][0])[2:-1]
    barcode_type = str(barcode_data[0][1])
    # Flask.make_response()
    resp = {"content": content, "barcode_type": barcode_type}
    return resp


def get_text(file) -> object:
    data = pytesseract.image_to_string(Image.open(fp=io.BytesIO(file)), lang='rus')
    return data
