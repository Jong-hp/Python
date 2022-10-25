# 가수 한 명을 탄생

# import pack2.pack2.class04 pack2.class4 import SingerType

def process():
    # youngwoung = pack2.pack2.class04ceMissingError
    youngwoung = SingerType()
    print('영웅의 타이틀 송 : ', youngwoung.title_song)
    youngwoung.sing()

def process2():
    bts = SingerType()  # 생성자를 호출해 객체를 만든것
    # bts = SingerType    # 주소를 치환하는것
    bts.sing()
    bts.title_song = '최고의 순간은 아직'
    bts.sing()
    bts.co = 'HIVE'
    print('소속사 : ', bts.co)
    print()
    blankpink = SingerType()
    blankpink.sing()
    blankpink.title_song = '셧다운'
    blankpink.sing()
    # print('소속사 : ', blankpink.co)   # 'SingerType' object has no attribute 'co'

# process()

if __name__ == '__main__':
    process()
    print('--------')
    process2()