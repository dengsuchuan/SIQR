from win10toast import ToastNotifier
from PIL import ImageGrab, Image
from pyzbar.pyzbar import decode
import time
import os,sys
import pyperclip


print("-----------------------------")
print('python Verion: ', sys.version)
print("----------------------------")

toast = ToastNotifier()
toast.show_toast(title="二维码识别", msg="程序已启动！",icon_path=r"C:\Program Files\Internet Explorer\images\bing.ico", duration=10)


def get_img_data(filename):
  img_data = []
  img = Image.open(filename)
  # barcodes = pyzbar.decode(img)
  barcodes = decode(img)
  for barcode in barcodes:
      barcodeData = barcode.data.decode("utf-8")
      img_data.append(barcodeData)
  return img_data

def get_img_data_clipboard():
  try:
    im = ImageGrab.grabclipboard()
  except:
    pyperclip.copy('')
    toast = ToastNotifier()
    toast.show_toast(title="二维码识别", msg="识别失败！",icon_path=r"C:\Program Files\Internet Explorer\images\bing.ico", duration=10)
    return None
  copy_data = []
  if not im: return None

  print('发现剪贴板图片')
  if isinstance(im, list):
    for i in im:
      img_data = get_img_data(i)
      copy_data = img_data
  else:
    filename = 'file.png'
    im.save(filename, 'PNG')
    img_data = get_img_data(filename)
    copy_data = img_data
    os.remove(filename)
  
  # 没有识别出来东西
  if copy_data:
    data_str = '\n'.join(copy_data)
    pyperclip.copy(data_str)
    print(copy_data)
    toast = ToastNotifier()
    toast.show_toast(title="二维码识别", msg="结果已交给剪切板，可直接粘贴到文本！",icon_path=r"C:\Program Files\Internet Explorer\images\bing.ico", duration=10)
    return copy_data

if __name__ == '__main__':
  while True:
    get_img_data_clipboard()
    time.sleep(0.5)


