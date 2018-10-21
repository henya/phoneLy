# -*- coding: utf-8 -*-
import xlsxwriter
class HtmlOutputer(object):
	def save_to_excel(self, results, file_name):
		book = xlsxwriter.Workbook(R'E:/2018python/%s.xls' % file_name)
		tmp =  book.add_worksheet()
		# row_num = len(results)+1
		row = 0
		col = 0
		for version,Vtime,Vinfo in (results):
			tmp.write(row,col,version)
			tmp.write(row,col+1,Vtime)
			tmp.write(row,col+2,Vinfo)
			row += 1
		book.close()

			
					

