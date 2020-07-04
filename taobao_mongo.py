
# 从数据库读取数据
import pymongo

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

# 定义空列表存放数据
P = []  # 存放价格 price
L = []  # 存放店铺的地点城市location
D = []  # 存放成交量deal
S = []  # 存放店铺名称shop
T = []  # 存放商品名称tit1e
for i in range(1016):
    # 从 mongodb中读取数据
    price = db.products.find({})[i]['price']
    location = db.products.find({})[i]['location']
    deal = db.products.find({})[i]['deal']
    shop = db.products.find({})[i]['shop']
    title = db.products.find({})[i]['title']
    # 对数据分别进行处理
    prices = float(price[1:])  # 去掉符号,并将价格转为浮点型
    locations = location[:2]  # 地区取省份
    if deal == '':
        deal = '0人付款'  # 填充交易量缺失值
    deals = int(deal[:-3])  # 将交易量转为整型
    # 将数据添加到列表中
    P.append(prices)
    L.append(locations)
    D.append(deals)
    S.append(shop)
    T.append(title)



# 词频统计
import jieba

text = ''
for t in T:
    text += ' '.join(jieba.cut(t))

words = text.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print('{0:<10},{1:>5}'.format(word, count))



# 词云
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# 读取整个文本.
text = ''
for t in T:
    text += ' '.join(jieba.cut(t))

stopwords = set(STOPWORDS)

d = path.dirname(__file__)
alice_coloring = np.array(Image.open(path.join(d, "apple1.png")))
# img = Image.open('apple1.png')  # 打开图片
# img_array = np.array(img)  # 将图片装换为数组
# img_array = imread('apple1.png')  # 需要注意的是在设置自定义背景图片的时候只有透明部分才不会有词云的内容，如果仅仅是空白而不是透明的话也会有词云内容显示的。# 一般是图片问题
font = r'C:\Windows\Fonts\simkai.ttf'  # 导入字体
wc = WordCloud(
    background_color='white',  # 设置背景颜色
    mask=alice_coloring,  # 设置背景图片
    font_path=font,  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
    max_words=100,   # 设置最大现实的字数
    stopwords=STOPWORDS,  # 设置停用词
    max_font_size=150,  # 设置字体最大值
    random_state=30  # 设置有多少种随机生成状态，即有多少种配色方案
)
wc.generate_from_text(text)  # 绘制图片
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")

plt.show()
