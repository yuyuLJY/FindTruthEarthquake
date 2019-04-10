# encoding: utf-8
import requests
import re
from bs4 import BeautifulSoup
import time
import bs4
import xlwt

def getHTMLText(url):
    print("函数"+url)
    #cookie = 'cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; t=da32d1956bf7359521d4125151e0d4b0; _tb_token_=53811b8a331e1; cookie2=5a5546894533f119e57b81b85300098b; dnk=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; x=__ll%3D-1%26_ato%3D0; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bOTNBpU1g%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzYFlrtS4bkp38%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; uss=""; csg=85d576da; skt=ba4e9478f6ad60a3; whl=-1%260%260%260; x5sec=7b22726174656d616e616765723b32223a226234313136323630316336656330663034663235306532613837356333316565434e65617a2b4d46454c50566b66486b6a4f6e3155426f4d4d6a597a4d7a51774d5467304e6a7378227d; l=bBOZfxjIviwswoijBOfiCQhjnmbt2QAfGNVP2FyFKICPO7BB5HUdWZac8Kx6C3GVa6d6R3RYGVWzBVTityUCh; isg=BFNTkOBVCwlcksO-YYx8M5pH4tfRHL2WHB0yewVymHLVhHYmjdsxGlgSvrRPFj_C'
    #cookie = 'cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; t=da32d1956bf7359521d4125151e0d4b0; _tb_token_=53811b8a331e1; cookie2=5a5546894533f119e57b81b85300098b; dnk=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; x=__ll%3D-1%26_ato%3D0; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bOTNBpU1g%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzYFlrtS4bkp38%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; uss=""; csg=85d576da; skt=ba4e9478f6ad60a3; whl=-1%260%260%260; x5sec=7b22726174656d616e616765723b32223a226234313136323630316336656330663034663235306532613837356333316565434e65617a2b4d46454c50566b66486b6a4f6e3155426f4d4d6a597a4d7a51774d5467304e6a7378227d; l=bBOZfxjIviwswkkwBOfiCQhjnmbtzQdfhNVP2FyFKICPOvWe5HUdWZacDttwC3GVa6IvR3RYGVWzBS8gCy4Fh; isg=BIeH88zRl212jBeC3YhwVy4LFjv9mAEyCOHGZ1l3e5QiyKuKYV_Wv_pOasgzJzPm'
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551254824932%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D; WBStorage=f3685954b8436f62|undefined'
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551262022905%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551268319906%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    #referer = 'https://s.weibo.com/weibo?q=%23%E8%B7%9F%E9%A3%8E%E4%B9%B0%20%E5%8F%A3%E7%BA%A2%E5%A7%A8%E5%A6%88%E5%B7%BE%23&page=3'
    # TODO
    #referer = 'https://weibo.com/p/1005052102180125/follow?page=1&sudaref=s.weibo.com&display=0&retcode=6102'  # follow
    # 爬取follow
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; wb_view_log_6026983818=1920*10801.25; YF-Page-G0=8fee13afa53da91ff99fc89cc7829b07; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; ALF=1582958822; SSOLoginState=1551422823; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm62flbDF2MYl7HFYpVeHt8fDflvKwcF_lI2w1BnUkIhWw.; SUB=_2A25xfKU3DeRhGeBO6VQY-C3EyjSIHXVSC5H_rDV8PUNbmtBeLWvtkW9NSjaarCj62vanI83T_gatIyWYZXAK5RN_; SUHB=0qj0bkTHq9OB5h; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=9828838594195.492.1551422825431; ULV=1551422825554:85:2:7:9828838594195.492.1551422825431:1551399807544; YF-V5-G0=5468b83cd1a503b6427769425908497c; Ugrow-G0=7e0e6b57abe2c2f76f677abd9a9ed65d; webim_unReadCount=%7B%22time%22%3A1551442102726%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    referer = 'https://s.weibo.com/weibo/%25E5%258C%2597%25E4%25BA%25AC%25E5%259C%25B0%25E9%259C%2587?topnav=1&wvr=6&b=1&sudaref=s.weibo.com&display=0&retcode=6102&page=2'
    cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; ALF=1586358280; SSOLoginState=1554822282; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6u-7_HOelcsqpfqrTXZOhqeWb4bQAdaJF78YIifNUwUo.; SUB=_2A25xqMTaDeRhGeBO6VQY-C3EyjSIHXVS37ESrDV8PUNbmtBeLWXnkW9NSjaarJRdttT86S5r2BDbvNpJEDMqYprW; SUHB=0S7C8ONv1yLast; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=7335734042472.333.1554822289004; ULV=1554822289216:106:3:3:7335734042472.333.1554822289004:1554807886111; webim_unReadCount=%7B%22time%22%3A1554822289499%2C%22dm_pub_total%22%3A4%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A4%2C%22msgbox%22%3A0%7D; wvr=6'
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'Cookie': cookie, 'Referer': referer}, timeout=10)
        #r.encoding = "utf - 8"
        r.raise_for_status()
        return r.text
    except:
        return "---------------无法连接---------------"

def parsePage(ID,commentList,name,zhuanfaList,likeList,argueList,html):
    print("调用parsePage")
    try:

        #TODO 提取评论
        soup = BeautifulSoup(html, 'html.parser')
        for i in soup.findAll(name='div', attrs={'class': 'content', 'node-type': 'like'}):
            ps = i('p')[0]
            commentList.append(ps.get_text())
            #TODO 解析是否含有地址
            #print(ps)

        #<div class="content" node-type="like">.*?<\\/div>
        html = html.replace("\t", "").replace("\n", "").replace("\r", "").replace("\\", "")
        print("区间长度："+str(len(re.findall(r'<div class="content" node-type="like">.*?<div node-type="feed_list_repeat">',html))))
        #print(len(re.findall(r'<div class="content" node-type="like">.*?<div node-type="feed_list_repeat">',html)))
        for i in re.findall(r'<div class="content" node-type="like">.*?<div node-type="feed_list_repeat">',html):
            #TODO 提取id
            #print(i)
            #print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")
            id = re.findall(r'<a href="//weibo.com/.*?class="name"', i)[0].replace( '" class="name"','').replace('"','')
            ID.append(id)
            #print(id)

            #TODO 提取Nickname
            #.replace( 'class="name" target="_blank" nick-name="','')
            nickname = re.findall(r'class="name" target="_blank" nick-name=".*?"', i)[0].replace( 'class="name" target="_blank" nick-name="','').replace('"','')
            name.append(nickname)
            #print(nickname)
            # TODO 提取评论

            #防止使用的是转发的评论、点赞、转发量
            for j in re.findall(r'<div class="card-act">.*?</div>',i):
                #print(j)
                # TODO 提取赞
                like_whole = re.findall(r'<li><a title="赞".*?</li>', j)[0]
                like_number = re.findall(r'<em>[0-9]{1,}</em>', like_whole)
                if like_number:
                    like_number = re.findall(r'[0-9]{1,}', like_number[0])[0]
                    print(like_number)
                    likeList.append(like_number)
                else:
                    # print("点赞数0")
                    likeList.append(0)
                # print(like_whole)

                # TODO 提取评论数量
                argue_whole = re.findall(r'>评论.*?<', j)[0]  # > 转发 866<
                argue_number = re.findall(r'[0-9]{1,}', argue_whole)
                if argue_number:
                    # print(argue_number[0])
                    argueList.append(argue_number[0])
                else:
                    # print("评论量：0")
                    argueList.append(0)

                # TODO 提取转发量
                zhuanfa_whole = re.findall(r'> 转发.*?<', j)[0]  # > 转发 866<
                zhuanfa_number = re.findall(r'[0-9]{1,}', zhuanfa_whole)
                if zhuanfa_number:
                    # print(zhuanfa_number[0])
                    zhuanfaList.append(zhuanfa_number[0])
                else:
                    # print("转发量：0")
                    zhuanfaList.append(0)


        print("转发数量："+str(len(zhuanfaList)))
        print("评论数量：" + str(len(argueList)))
        print("点赞数量：" + str(len(likeList)))
        print("ID数量：" + str(len(ID)))
        print("name数量：" + str(len(name)))
        print("言论数量：" + str(len(commentList)))

    except:
        print("解析失败")

def printComment(ID,commentList,name,zhuanfa,like,argueList):
    # -------------检测解析是否正确--------------------
    print("评论"+str(len(commentList)))
    print("ID" + str(len(ID)))
    print("name" + str(len(name)))
    style = xlwt.XFStyle()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('#')
    for i in range(len(ID)):
        worksheet.write(i, 0, name[i], style)  # name
        worksheet.write(i, 1, ID[i], style)  # id
        worksheet.write(i, 2, commentList[i], style) #言论
        worksheet.write(i, 3, zhuanfa[i], style)#转发数
        worksheet.write(i, 4, argueList[i], style)#评论数
        worksheet.write(i, 5, like[i], style)  # 点赞数
    workbook.save('E:/A大三下/大创/数据/topic_id.xls')


def main():
    '''
    抓取用户的微博内容
    :return:
    '''
    # 装用户ID、name、comment的盒子
    commentList = []
    ID = []
    name = []
    zhuanfa = []
    like = []
    argueList=[] #在言论下的评论数量
    #start_url = "https://s.weibo.com/weibo?q=%23%E5%BC%80%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%89%81%20%E5%8F%A3%E7%BA%A2%E5%A7%A8%E5%A6%88%E5%B7%BE%23&nodup=1"
    start_url = "https://s.weibo.com/weibo/%25E5%258C%2597%25E4%25BA%25AC%25E5%259C%25B0%25E9%259C%2587?topnav=1&wvr=6&b=1&sudaref=s.weibo.com&display=0&retcode=6102"
    #start_url = "https://s.weibo.com/weibo/%25E5%258C%2597%25E4%25BA%25AC%25E5%259C%25B0%25E9%259C%2587?topnav=1&wvr=6&b=1"

    for i in range(1, 2):
        try:
            #地震的url，但是被replace
            #url = https://s.weibo.com/weibo?q=%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%9C%87&wvr=6&b=1&Refer=SWeibo_box&page=6
            #"https://s.weibo.com/weibo?q=%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%9C%87&wvr=6&b=1&Refer=SWeibo_box&page=23&sudaref=s.weibo.com&display=0&retcode=6102
            #url = start_url + '&page={}'.format(str(i))+"&sudaref=s.weibo.com&display=0&retcode=6102"
            url =  start_url + '&page={}'.format(str(i))
            print(url)
            html = getHTMLText(url)
            #print(html)
            parsePage(ID,commentList,name,zhuanfa,like,argueList,html)
            print("name:"+str(name)+" ID:"+ID+" comment:"+commentList)
            #parsePage(commentList, html)
        except:
            continue
    printComment(ID,commentList,name,zhuanfa,like,argueList)

main()