import requests

#serviceKey='2DPsTu7ixNseqqbFI%2BvhTIxCLWm2lt9OEOIp2j2SrE%2B5mcp1LrVrpcy5htguUGGy8wsS5TU%2BBw4PERI0%2BrZJfQ%3D%3D'
serviceKey='2DPsTu7ixNseqqbFI+vhTIxCLWm2lt9OEOIp2j2SrE+5mcp1LrVrpcy5htguUGGy8wsS5TU+Bw4PERI0+rZJfQ=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : serviceKey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '울산', 'ver' : '1.0' }

response = requests.get(url, params=params)
air = response.text
print(air)
