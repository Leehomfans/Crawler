# Crawler
爬取博客园文章/批量导出微信公众号文章/导出知识星球精华主题

平时我们可能需要把感兴趣的公众号的文章保存为pdf，方便离线查看，也可以避免某些文章被删除后看不到。所以我们需要把该公众号的文章批量导出为pdf。这里我们使用python来实现该功能。

### 导出该公众号的所有文章链接等信息为CSV文件。

     首先我们安装chrome的webscrapyer插件，用来爬取自己感兴趣的公众号的文章导出为CSV文件。文件保存文章的标题，时间和链接。具体插件的使用细节自己百度。

### 根据第一步生成的CSV文件批量导出为pdf
  首先我们安装wkhtmltopdf工具程序。然后编写程序来读取上一步得到的csv文件批量导出为pdf。这里由于微信的图片防盗链措施，直接根据url导出pdf会发现图片缺失。 
  所以我们需要对请求得到的html文件进行处理后，再导出为pdf。具体核心代码如下
 ```python
      def process(item):
          url = str(item[2])
          name = item[1] + item[0] + '.pdf'
          response = requests.get(url)
          html = response.text
          html = html.replace('data-src', 'src')

          try:
              pdfkit.from_string(html, name)
          except:
              pass

      with open("weixin.csv","r",encoding="gbk") as f:
          f_csv=csv.reader(f)
          next(f_csv)
          pool = ThreadPool(processes=20)
          pool.map(process, (i for i in f_csv))
          pool.close()
 ```
 
其中使用了线程池来加速处理生成pdf，本地测试一分钟可以导出90+篇文章。
* [博客](https://www.cnblogs.com/wzf-Learning/p/11153963.html)
* ![3c9095308e58b7c90aace2fe02a1e90](https://user-images.githubusercontent.com/16174175/223343159-551f8954-3153-4c96-9aae-dd8fbcdfca97.jpg)


