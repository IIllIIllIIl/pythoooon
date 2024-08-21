d = {}
url = {"google":"google.com", "naver":"naver.com"}
url["daum"] = "daum.com"
url["daum"] = "daum.net"
a = url.pop("google")
print(url)
print(a)
print(url.get("naver"))