# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import numpy as np
class HtmlParser(object):
	def parse(self,html_content):
		if html_content is None:
			return None
		soup = BeautifulSoup(html_content)
		#获取到版本号和时间等信息
		versionNums = soup.find_all('li',class_="sne")
		versionNumsArry = []

		for VN in versionNums:
			res = self.get_versionNums(VN)
			versionNumsArry.append(res)
			
		#获取版本的详细信息
		versionDetails = soup.find_all('div',class_="softqx")
		versionDetailsArry = []
		for VD in versionDetails:
			det = self.get_versionDetails(VD)
			versionDetailsArry.append(det)
		versionInfoCon = np.hstack((versionNumsArry,versionDetailsArry))
		# print(versionDetailsArry)
		versionAllInfo = []
		for VI in versionInfoCon:
			VAI = []
			VAI.append(VI[0])
			VAI.append(VI[1])
			VAI.append("|".join(VI[2]))
			versionAllInfo.append(VAI)
		# print(versionAllInfo)
		return versionAllInfo

	def get_versionNums(self,soup):
		#版本号
		vnVersion = soup['title']
		#更新时间等信息
		vnInfo = soup.font.contents[0]
		return[vnVersion,vnInfo]
	def get_versionDetails(self,soup):
		vdDetailsResult = soup.find_all("p")
		vdDetailsArry = []
		for vd in vdDetailsResult:
			vdstr = vd.get_text()
			vdDetailsArry.append(vdstr)
			# print(vdDetailsArry)
		return [vdDetailsArry]
		


