import requests

serviceKey ='2DPsTu7ixNseqqbFI+vhTIxCLWm2lt9OEOIp2j2SrE+5mcp1LrVrpcy5htguUGGy8wsS5TU+Bw4PERI0+rZJfQ=='

url = 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRouteSt'
params ={'serviceKey' : serviceKey, 'busRouteId' : '', 'startOrd' : '1', 'endOrd' : '10' }

response = requests.get(url, params=params)
print(response.content)