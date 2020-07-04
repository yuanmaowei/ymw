import  csv
import  matplotlib . pyplot  as  plt
from  matplotlib  import  pyplot
#读取数据
csvfile  =  open ( "spider.csv" )
reader  =  csv . reader ( csvfile )
#data存取每个单元格的数据
data  = []
#lit记录行数
lit  =  0
for  line  in  reader :
    lit  =  lit  +  1
    data . append ( line )
i  =  1
#本想用if data[i][0] == str("湖北省") 这样的方式来做if限制，但是实施不了，所以用字典di来引用代替
di  = {
    1 : "湖北省" ,
    2 : "广东省" ,
    3 : "河南省" ,
    4 : "浙江省" ,
    5 : "中国香港" ,
    6 : "湖南省" ,
    7 : "安徽省" ,
    8 : "黑龙江省" ,
    9 : "江西省" ,
    10 : "北京市" ,
    11 : "山东省" ,
    12 : "上海市" ,
    13 : "江苏省" ,
    14 : "四川省" ,
    15 : "重庆市" ,
    16 : "中国台湾" ,
    17 : "福建省" ,
    18 : "河北省" ,
    19 : "陕西省" ,
    20 : "广西壮族自治区" ,
    21 : "内蒙古自治区" ,
    22 : "山西省" ,
    23 : "云南省" ,
    24 : "海南省" ,
    25 : "甘肃省" ,
    26 : "吉林省" ,
    27 : "辽宁省" ,
    28 : "贵州省" ,
    29 : "新疆维吾尔自治区" ,
    30 : "宁夏回族自治区" ,
    31 : "中国澳门" ,
    32 : "青海省" ,
    33 : "天津市"
    }

#统计每个省份的确诊人数，死亡人数，治愈人数
total_qz = []; n_qz = 0 ;
total_sw = []; n_sw = 0 ;
total_zy = []; n_zy = 0 ;
#用di[j]来判断省份
j  =  1
while  j < 34 :
    #用i来移动行数
    i = 1
    n_qz  =  0 ;
    n_sw  =  0 ;
    n_zy  =  0 ;
    while  i < lit :
        if  data [ i ][ 0 ] ==  di [ j ]:
            n_qz += int ( data [ i ][ 2 ])
            n_sw += int ( data [ i ][ 4 ])
            n_zy += int ( data [ i ][ 5 ])
        i  +=  1
    total_qz . append ( n_qz )
    total_sw . append ( n_sw )
    total_zy . append ( n_zy )
    j  +=  1
