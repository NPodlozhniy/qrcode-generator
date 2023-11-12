# Qrcode In Terminal
The simple tool to generate QR codes

### Getting started
```bash
$ git clone https://github.com/NPodlozhniy/qrcode-generator
$ cd qrcode-generator
$ pip install -r requirements.txt
$ python app.py
```

### Image Size

If you need a specific QR size use the following code

```python
from PIL import Image
p = Image.open('temp.png')
p.resize((1024, 1024)).save('QR.png')
```
