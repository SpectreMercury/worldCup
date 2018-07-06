import scrapy
from scrapy import Selector
import json

class country(scrapy.Spider):
	name = "country"
	allowed_domains = ["liansai.500.com"]
	#start_urls
	start_urls = ['http://liansai.500.com/team/133', 'http://liansai.500.com/team/134', 'http://liansai.500.com/team/135', 'http://liansai.500.com/team/136', 'http://liansai.500.com/team/137', 'http://liansai.500.com/team/138', 'http://liansai.500.com/team/139', 'http://liansai.500.com/team/140', 'http://liansai.500.com/team/141', 'http://liansai.500.com/team/142', 'http://liansai.500.com/team/143', 'http://liansai.500.com/team/144', 'http://liansai.500.com/team/145', 'http://liansai.500.com/team/146', 'http://liansai.500.com/team/147', 'http://liansai.500.com/team/148', 'http://liansai.500.com/team/149', 'http://liansai.500.com/team/150', 'http://liansai.500.com/team/151', 'http://liansai.500.com/team/152', 'http://liansai.500.com/team/153', 'http://liansai.500.com/team/154', 'http://liansai.500.com/team/155', 'http://liansai.500.com/team/156', 'http://liansai.500.com/team/157', 'http://liansai.500.com/team/158', 'http://liansai.500.com/team/159', 'http://liansai.500.com/team/160', 'http://liansai.500.com/team/161', 'http://liansai.500.com/team/162', 'http://liansai.500.com/team/163', 'http://liansai.500.com/team/164', 'http://liansai.500.com/team/165', 'http://liansai.500.com/team/166', 'http://liansai.500.com/team/167', 'http://liansai.500.com/team/168', 'http://liansai.500.com/team/169', 'http://liansai.500.com/team/170', 'http://liansai.500.com/team/171', 'http://liansai.500.com/team/172', 'http://liansai.500.com/team/173', 'http://liansai.500.com/team/174', 'http://liansai.500.com/team/175', 'http://liansai.500.com/team/176', 'http://liansai.500.com/team/177', 'http://liansai.500.com/team/178', 'http://liansai.500.com/team/179', 'http://liansai.500.com/team/180', 'http://liansai.500.com/team/181', 'http://liansai.500.com/team/182', 'http://liansai.500.com/team/183', 'http://liansai.500.com/team/184', 'http://liansai.500.com/team/185', 'http://liansai.500.com/team/186', 'http://liansai.500.com/team/187', 'http://liansai.500.com/team/188', 'http://liansai.500.com/team/189']
	def parse(self, response):
		
		file = open('/Users/Francis/Documents/worldCup/data/country.json', 'r+')
		file_content = json.load(file)
		file.close()
		
		print '========================'
		country_code = response.url.split('/')[4]
		country_eng = response.xpath('//div[@class="itm_name_en"]/text()').extract()[0]
		country_chis = response.xpath('//div[@class="itm_tit"]/text()').extract()[0].strip()
		temp_save = file_content
		temp_save[country_code] = {}
		temp_save[country_code]['eng'] = country_eng
		temp_save[country_code]['chis'] = country_chis
		temp_save = json.dumps(temp_save)

		file = open('/Users/Francis/Documents/worldCup/data/country.json', 'r+')
		file.write(temp_save)
		file.close()

		print '>>>>>>>>>>>>>>>>>>>>>>>>'