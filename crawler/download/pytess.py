import ddddocr

ocr = ddddocr.DdddOcr()
with open(r'./img/72.jpg', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)

print(res)