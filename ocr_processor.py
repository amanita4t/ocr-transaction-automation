from paddleocr import PaddleOCR

def run_ocr(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    result = ocr.ocr(image_path)
    text = " ".join(line[1][0] for line in result[0])
    return text
