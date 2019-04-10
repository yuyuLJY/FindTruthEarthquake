# encoding: utf-8
import requests
import re
from bs4 import BeautifulSoup
import time
import bs4
import xlwt

def getHTMLText(url):
    print("函数"+url)
    # TODO
    # 爬取follow
    referer = 'https://s.weibo.com/weibo/%25E5%258C%2597%25E4%25BA%25AC%25E5%259C%25B0%25E9%259C%2587?topnav=1&wvr=6&b=1&sudaref=s.weibo.com&display=0&retcode=6102&page=2'
    cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; ALF=1586358280; SSOLoginState=1554822282; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6u-7_HOelcsqpfqrTXZOhqeWb4bQAdaJF78YIifNUwUo.; SUB=_2A25xqMTaDeRhGeBO6VQY-C3EyjSIHXVS37ESrDV8PUNbmtBeLWXnkW9NSjaarJRdttT86S5r2BDbvNpJEDMqYprW; SUHB=0S7C8ONv1yLast; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=7335734042472.333.1554822289004; ULV=1554822289216:106:3:3:7335734042472.333.1554822289004:1554807886111; webim_unReadCount=%7B%22time%22%3A1554822289499%2C%22dm_pub_total%22%3A4%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A4%2C%22msgbox%22%3A0%7D; wvr=6'
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'Cookie': cookie, 'Referer': referer}, timeout=10)
        #r.encoding = "utf - 8"
        r.raise_for_status()
        return r.text
    except:
        return "---------------无法连接---------------"

def parsePage(ID,commentList,name,zhuanfaList,likeList,argueList,timeList,html):
    print("调用parsePage")
    try:
        #TODO 提取评论
        soup = BeautifulSoup(html, 'html.parser')
        for i in soup.findAll(name='div', attrs={'class': 'content', 'node-type': 'like'}):
            ps = i('p')[0]
            commentList.append(ps.get_text())

            #TODO 解析是否含有地址
            #print(ps)
            #addr_whole = re.findall(r'头条新闻.*?',ps)[0]
            #if addr_whole:
            #   # 包含地址
            #   addr = addr_whole[0].replace('<i class="wbicon">','').replace('</a>','')
            #   print(addr)

        html = html.replace("\t", "").replace("\n", "").replace("\r", "").replace("\\", "")
        print("区间长度："+str(len(re.findall(r'<div class="content" node-type="like">.*?<div node-type="feed_list_repeat">',html))))
        #print(len(re.findall(r'<div class="content" node-type="like">.*?<div node-type="feed_list_repeat">',html)))
        for i in re.findall(r'<div class="content" node-type="like">.*?<div node-type="feed_list_repeat">',html):
            #TODO 提取id
            id = re.findall(r'<a href="//weibo.com/.*?class="name"', i)[0].replace( '" class="name"','').replace('"','')
            ID.append(id)

            #TODO 提取Nickname
            #.replace( 'class="name" target="_blank" nick-name="','')
            nickname = re.findall(r'class="name" target="_blank" nick-name=".*?"', i)[0].replace( 'class="name" target="_blank" nick-name="','').replace('"','')
            name.append(nickname)
            #print(nickname)
            # TODO 提取评论

            # TODO 提取时间
            time_whole = re.findall(r'click:wb_time">.*?<', i)  # > 转发 866<
            if time_whole:
                time =time_whole[0].replace(" ",'').replace('click:wb_time">','').replace('<','')
                #print(time)
                timeList.append(time)
            else:
                # print("转发量：0")
                timeList.append(0)

            #防止使用的是转发的评论、点赞、转发量
            for j in re.findall(r'<div class="card-act">.*?</div>',i):
                #print(j)
                # TODO 提取赞
                like_whole = re.findall(r'<li><a title="赞".*?</li>', j)[0]
                like_number = re.findall(r'<em>[0-9]{1,}</em>', like_whole)
                if like_number:
                    like_number = re.findall(r'[0-9]{1,}', like_number[0])[0]
                    #print(like_number)
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
                    argueList.append(0)

                # TODO 提取转发量
                zhuanfa_whole = re.findall(r'> 转发.*?<', j)[0]  # > 转发 866<
                zhuanfa_number = re.findall(r'[0-9]{1,}', zhuanfa_whole)
                if zhuanfa_number:
                    #print(zhuanfa_number[0])
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
        print("time数量：" + str(len(timeList)))
    except:
        print("解析失败")

def printComment(ID,commentList,name,zhuanfa,like,timeList,argueList):
    # -------------检测解析是否正确--------------------
    print("评论"+str(len(commentList)))
    print("ID" + str(len(ID)))
    print("name" + str(len(name)))
    style = xlwt.XFStyle()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('#')
    for i in range(len(ID)):
        worksheet.write(i, 1, name[i], style)  # name
        worksheet.write(i, 2, ID[i], style)  # id
        worksheet.write(i, 0, commentList[i], style) #言论
        worksheet.write(i, 3, zhuanfa[i], style)#转发数
        worksheet.write(i, 4, argueList[i], style)#评论数
        worksheet.write(i, 5, like[i], style)  # 点赞数
        worksheet.write(i, 6, timeList[i], style)  # 点赞数
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
    timeList = [] #该条地震微博发表的时间
    start_url = "https://s.weibo.com/weibo/%25E5%258C%2597%25E4%25BA%25AC%25E5%259C%25B0%25E9%259C%2587?topnav=1&wvr=6&b=1&sudaref=s.weibo.com&display=0&retcode=6102"

    for i in range(1, 40):
        try:
            url =  start_url + '&page={}'.format(str(i))
            print(url)
            html = getHTMLText(url)
            #print(html)
            parsePage(ID,commentList,name,zhuanfa,like,argueList,timeList,html)
            print("name:"+str(name)+" ID:"+ID+" comment:"+commentList)
            #parsePage(commentList, html)
        except:
            continue
    printComment(ID,commentList,name,zhuanfa,like,timeList,argueList)

main()