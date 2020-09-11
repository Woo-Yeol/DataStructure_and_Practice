# Dictionary (dict) : 딕셔너리
price = {'콩나물해장국':4500, '갈비탕':9000, '돈가스':8000}

# 한 가지 항목을 추가
price['팟타이'] = 7000
print('\n',price,'\n',price.keys(),'\n',price.values())

# 여러 가지 항목을 추가
price.update({'순댓국':6000, '샌드위치':7500})
print('\n',price,'\n',price.keys(),'\n',price.values())
