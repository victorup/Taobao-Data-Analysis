# 淘宝商品大数据分析
有些图片未显示，请见知乎：https://zhuanlan.zhihu.com/p/156003809

## 课题背景和目的
在纷繁复杂的互联网交易中，商品的选择多种多样，让人眼花缭乱，在众多商品中选择一个适合自己的非常困难。本课题目的即从淘宝网爬取商品信息，获取该商品信息后做数据处理及可视化分析，对单个商品及多个商品进行分析对比，使客户能够获得有用的信息。

## 课题的需求及主要功能
需求：该课题需要获取淘宝网的商品页面信息。

功能：获得不同商品的价格信息，如最高价最低价平均价；可寻找到交易量最多的店铺；各地区店铺分布情况；商品价格对销量的影响；以及不同商品间的销售情况；用户输入一个预期价格及预期最低交易量，可自动得到推荐商品的商品信息。

## 课题数据的收集过程及工具
- 数据收集采用web爬虫方式。
- 使用selemiun浏览器自动化测试框架。
- 请求网页的url，获取网页的源代码。

![image]()
图1 淘宝网url

- 分网页商品信息。查找商品的image, price, deal, title, shop, location等信息

![image]()
图2 淘宝商品页面信息

- 使用pyquery库解析网页源代码，利用CSS选择器获取网页元素。

![image]()
图3网页源代码

- 将爬取结果以字典形式保存。

![image]()
图4 爬取结果显示

## 课题数据的预处理过程及多源异构融合
- 将mongodb中数据导入CSV文件
- 对数据进行清洗和处理
- 缺失值处理
- 删除重复值
- 数值类型转换

![image]()
图5 数据处理

## 课题数据的存储过程及工具
- 首先安装了mongodb数据库，配置了环境变量等一系列设置

![image]()
图6 保存mongodb代码

- 然后利用上述代码将爬取到的商品数据保存到mongodb

![image]()
图7 mongodb存储结果

- 所用工具：mongodb非关系性数据库

## 课题数据的分析方法、过程及相应平台工具选择说明
- 分析方法：Kmeans聚类分析、词频统计、最大值均值计算
- 使用工具：python机器学习库、Excel、魔镜
- 分析结果：
1) 词频分析

![image](https://github.com/victorup/Taobao-Data-Analysis/blob/master/images/%E8%8B%B9%E6%9E%9C%E8%AF%8D%E4%BA%91%E5%9B%BE.png)

图8 词云分析可视化

2) 北上广店铺数量普遍较多，其中广东的店铺数量最多；

![image](https://github.com/victorup/Taobao-Data-Analysis/blob/master/images/%E5%BA%97%E9%93%BA%E5%88%86%E5%B8%83%E6%9F%B1%E7%8A%B6%E5%9B%BE.png)
图9 店铺分布柱状图

3) 第一名店铺销量最好，相比后四名要高出4倍左右；

![image](https://github.com/victorup/Taobao-Data-Analysis/blob/master/images/%E5%89%8D%E4%BA%94%E5%90%8D%E5%BA%97%E9%93%BA%E5%8F%8A%E4%BA%A4%E6%98%93%E9%87%8F%E7%82%B9%E7%BA%BF%E5%9B%BE.png)

图10 前五名店铺及交易量点线图

4) 广东的交易量是最多的，占到总体交易量的86%；

![image](https://github.com/victorup/Taobao-Data-Analysis/blob/master/images/%E5%90%84%E7%9C%81%E4%BA%A4%E6%98%93%E5%88%86%E5%B8%83%E9%A5%BC%E5%9B%BE.png)

图11 各省交易量分布饼图

5) 利用地图可清晰比较出各省的交易量分布，广东占比最大；

![image](https://github.com/victorup/Taobao-Data-Analysis/blob/master/images/%E5%90%84%E7%9C%81%E4%BA%A4%E6%98%93%E9%87%8F%E5%88%86%E5%B8%83%E5%9C%B0%E5%9B%BE.png)

图12 各省交易量分布地图

6) 根据聚类结果的数量可以看出，商品价格主要集中在2000-4000元之间，为主流销售产品（蓝色图标）；绿色五角星图标为新发布产品，价格普遍偏高；红色图标为商品的衍生物（如ipad保护膜、保护壳等）。

![image](https://github.com/victorup/Taobao-Data-Analysis/blob/master/images/ipad%E4%BB%B7%E6%A0%BCKmeans%E8%81%9A%E7%B1%BB.png)

图13 ipad价格Kmeans聚类结果

7) 江西macbook和ipad销量最大，然而dell相对较低。而甘肃价格最低，说明甘肃相对来说电子产业并不起色。

![image]()
图14 各地区最高价最低价均值对比

8) 苹果产品广受大众欢迎，其中ipad小巧方便，易携带，购买人数最多；联想相对于戴尔性价比高一些，所以购买人数也较多。

![image]()
图15商品平均交易量对比饼图

9) ipad最便宜，购买人数最多；macbook均价最高；dell价格最高，购买人数最少，lenovo性价比最高。人傻钱多戴，美帝良心想。

![image]()
图16 商品价格及交易量气泡图

10) 根据用户的输入条件，从数据库中找到与要求匹配的商品进行推荐

![image](https://github.com/victorup/Taobao-Data-Analysis/blob/master/images/%E6%B7%98%E5%AE%9D%E5%95%86%E5%93%81%E6%8E%A8%E8%8D%90.png)

图17 用户商品推荐效果图

## 课题数据的可视化过程及工具
- 将整理好的数据利用python中matplotlib库可视化
- 将数据导入到Excel表中，利用Excel图表工具可视化
- 将数据上传到魔镜及Echart可视化网站进行数据分析及可视化
- 使用工具：python语言设计、Echart、魔镜、Excel、PhotoShop

## 课题结论说明
可视化结果清晰的反应了本课题之前所希望达到的目的，将商品的各项指标及商品间的对比进行了清晰的分析。

## 课题心得体会
通过本次课题，掌握了大数据管理的全部过程，数据采集、数据融合、数据存储、数据、数据分析以及数据可视化，对每一个步骤都有了清晰的认识；学会了在大数据管理过程中各项工具的使用；对编程能力有极大的提升；将课堂上的理论知识与实际联系起来，对今后的项目及工作有极大的帮助。

## 相关参考文献
- 《Python 3网络爬虫开发实战》，崔庆才 著
- 《python语言程序设计基础（第2版）》，嵩天 礼欣 黄天羽 著
- 《用Python写网络爬虫》[澳] 理查德·劳森（Richard Lawson） 著，李斌 译
- CSDN等相关博客
