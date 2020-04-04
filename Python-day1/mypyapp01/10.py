'''
练习：项目中需要保存一个新闻数组，每个新闻有“nid”、‘title’、‘pubTime’三个属性；先创建一个空白的列表，然后向其中添加一个新闻、再添加一个新闻、再添加一个新闻；最后输出所有的新闻	
分析：每个新闻有属性，属性名就是下标名——dict；多个新闻组成的集合有顺序，且可以添加新元素——list
'''
newsList = [ ]
n1 = {'nid':101,'title':'标题1','pubTime':0}
n2 = {'nid':102,'title':'标题2','pubTime':0}
n3 = {'nid':103,'title':'标题3','pubTime':0}
newsList.append(n1)
newsList.append(n2)
newsList.append(n3)

#print(newsList)
#Python中for循环很特别——今天仅做了解
for  i  in  range(0, 3, 1):
  print(newsList[i]['nid'])
  print(newsList[i]['title'])
  print(newsList[i]['pubTime'])

print('==程序运行结束==')
