from PIL import Image
import pyocr

# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]

texts = []
for i in range(1,61):
    imgName = "img"+ str(i) + ".png"
    try:
        # 画像の文字を読み込む
        txt = engine.image_to_string(Image.open(imgName), lang="jpn")
        print("解析済み:"+ str(imgName))
        #print(txt) # 「Test Message」が出力される
        texts.append(txt)
    except:
        print("解析失敗:"+ str(imgName))
        continue

print("\n----------------------------------\n")
try:
    with open('test.txt', 'w') as f:
        f.writelines(texts)
    print("ファイル書き込みが完了しました")
except:
    print("ファイル書き込み失敗")