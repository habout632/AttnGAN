import pandas as pd

attrs_df = pd.read_csv('~/Downloads/list_attr_upperbody.txt', header=0, sep=" ")
header = attrs_df.columns.tolist()
print(header)
print(len(header))

first = attrs_df.iloc[3]
print(first)
print(first["无袖"])
print()

# 衣服种类
clothes = ["连衣裙", "女式背心", "女式马夹", "女式针织衫", "女式毛衣", "女式POLO衫", "女式卫衣", "女式衬衫", "女式T恤", "女式皮草", "女式皮衣", "女式羽绒", "女式大衣",
           "女式风衣/长外套", "女式夹克", "女式西服", "女式短外套", "其他", "泳衣泳裤", "连体裤", "卫衣", "冲锋衣／抓绒衣", "家居服/睡衣", "其他"]
# 袖长
sleeve = ["无袖", "短袖", "盖肩袖", "中袖/5分袖", "6分袖/7分袖/8分袖", "9分袖", "长袖"]

# 领口
collar = ["翻领", "高领", "立领", "毛领", "西装领（平驳领/创驳领）", "翻领(西装)", "娃娃领/公主领", "荡领", "衬衫领/衬衣领", "POLO领/T恤领", "连帽领", "棒球领",
          "围脖领/堆领/堆堆领", "系带领", "青果领", "圆领", "V领", "小V领", "方领", "U领", "一字领", "吊带领", "其他无领", "露肩一字领/抹胸", "斜肩领", "其他有领"]

# 主要颜色
color = ["红色", "粉色", "橙色", "黄色", "绿色", "蓝色", "紫色", "灰色", "黑色", "白色", "米色", "棕色", "褐色", "咖色", "驼色", "杏色", "青色", "藏青色",
         "银色", "花色", "其他", "金色"]

# 次颜色
["红色.1", "粉色.1", "橙色.1", "黄色.1", "绿色.1", "蓝色.1", "紫色.1", "灰色.1", "黑色.1", "白色.1", "米色.1", "棕色.1", "褐色.1", "咖色.1", "驼色.1",
 "杏色.1", "青色.1", "藏青色.1", "银色.1",
 "花色.1", "其他.1", "金色.1"]

# 材质 *
material = ["棉/麻/棉麻", "雪纺", "丝绸", "牛仔", "毛呢", "毛线", "皮/pu", "皮草", "其他"]

# 图案 *
pattern = ["图案", "方块印图", "字母数字", "字母数字+其他", "植物花卉", "人脸人像", "动物卡通", "骷髅头", "建筑风景", "其他图案"]

# 纹理
texture = ["无纹理", "全蕾丝", "全镂空", "全网纱/透视", "蕾丝拼接", "镂空拼接", "网纱/拼接", "铰花", "绒毛", "压线", "压线拼接", "多层花边", "褶皱", "百褶", "其他纹理",
           "其他纹理拼接"]

# 裙型
["裙型", '鱼尾裙', "蛋糕裙", "节裙/塔裙", "百褶裙", "泡泡裙", "花苞裙", "蓬蓬裙", "A字裙", "伞裙／喇叭裙", "包臀裙／一步裙", "直筒裙", "其他"]

# 主花色模式
["素色", "拼色", "渐变色", "混杂色", "细横条纹", "粗横条纹", "竖条纹", "暗纹", "小方格", "大方格", "菱形格", "千鸟格", "波点", "个性印花", "图案", "印花", "几何印花",
 "豹纹", "虎纹", "斑马纹", "蛇纹", "迷彩", "提花", "其他", "大理石纹"]

# 次花色模式
["躯干素色", "局部素色", "拼色", "渐变色", "混杂色", "细横条纹", "粗横条纹", "竖条纹", "暗纹", "小方格", "大方格", "菱形格", "千鸟格", "波点", "个性印花", "图案", "印花",
 "几何印花", "豹纹", "虎纹", "斑马纹", "蛇纹", "迷彩", "提花", "其他", "大理石纹"]

# 衣服大小
sizes = ["腰部", "髋部", "裆部(超短裙)", "大腿(短裙)", "膝盖(中裙)", "小腿(中长裙)", "脚踝（及踝裙）", "脚(及地裙)", "前短后长", "其它不规则"]

with open("descriptions.txt", "w") as f:
    for index, row in attrs_df.iterrows():
        print(row['filename'], row['连衣裙'])

        clothes_type = ""
        for ct in clothes:
            if row[ct] == 1:
                clothes_type = ct

        sleeve_len = ""
        for s in sleeve:
            if row[s] == 1:
                sleeve_len = s

        collar_type = ""
        for c in collar:
            if row[c] == 1:
                collar_type = c

        cloth_color = ""
        for cc in color:
            if row[cc] == 1:
                cloth_color = cc

        attrs = {
            "sleeve_len": sleeve_len,
            "cloth_color": cloth_color,
            "collar_type": collar_type,
            "clothes_type": clothes_type,
        }
        # print("颜色{cloth_color}　袖长{sleeve_len}　领子{collar_type}　女式毛衣{女式毛衣}".format(**attrs))
        desp = "{collar_type} {sleeve_len} 的 {cloth_color} {clothes_type}".format(**attrs)
        print(desp)
        f.write("{} {}".format(row['filename'], desp))
        f.write("\n")

