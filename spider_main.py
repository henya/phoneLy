# -*- coding: utf-8 -*-
import html_downloader,html_parser,html_outputer
# 程序的入口
if __name__ == "__main__":
	#想获取APP版本更新的数据地址 
	baseUrl = "https://soft.shouji.com.cn/down/18684.html"
    #下载网站数据
	pageLoader = html_downloader.HtmlDownloader()
	pageContent = pageLoader.get_page(baseUrl)
	# 对下载数据进行拆分组合
	pageParser = html_parser.HtmlParser()
	versionNumResult = pageParser.parse(pageContent)
	# 保存需要的数据到excel
	pageOutputer = html_outputer.HtmlOutputer()
	pageOutputer.save_to_excel(versionNumResult,'test1')


