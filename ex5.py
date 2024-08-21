import  wikipedia 
wiki=wikipedia.page('Artificial intelligence') 
text="""
Song Min Jae Programming Hello World Game Play 
"""
print(text)
from wordcloud import WordCloud
wd=WordCloud(width =2000, height = 1500).generate(text)
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(wd)
plt.show()
#송민재