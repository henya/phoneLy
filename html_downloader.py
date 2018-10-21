# -*- coding: utf-8 -*-
import requests
class HtmlDownloader(object):
	def get_page(self,baseUrl):
		try:
			#设置请求头，模拟浏览器访问
			header = {
				'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                              r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
                'Referer': r'https://soft.shouji.com.cn/',
                'Connection': 'keep-alive'
			}
			result = requests.get(baseUrl,headers=header)
			data =  result.text.encode("latin1").decode("utf-8")
			# print(data)
			return data

		except Exception as err:
			print(err)
			print("获取数据失败")
			return None

