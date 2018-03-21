from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import sqlite3
import re
import nn

mynet = nn.searchnet('nn.db')

ignorewords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])


class crawler(object):
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname)
        self.cursor = self.con.cursor()

    def __del__(self):
        self.cursor.close()
        self.con.close()

    def dbcommit(self):
        self.con.commit()

    def getentryid(self, table, field, value, createnew=True):
        self.cursor.execute(
            "select id from %s where %s='%s'" % (table, field, value))
        res = self.cursor.fetchone()
        if res == None:
            self.cursor.execute(
                "insert into %s(%s) values('%s')" % (table, field, value))
            return self.cursor.lastrowid
        else:
            return res[0]

    def addtoindex(self, url, soup):
        if self.isindexed(url):
            return
        # print('Indexing %s' % url)
        # 获取每个单词
        text = self.gettextonly(soup)
        words = self.separatewords(text)
        # 得到URL的id
        urlid = self.getentryid('urllist', 'url', url)
        # 将每个单词与该url关联
        for i in range(len(words)):
            word = words[i]
            if word in ignorewords:
                continue
            wordid = self.getentryid('wordlist', 'word', word)
            self.cursor.execute(
                "insert into wordlocation(urlid,wordid,location) values (%d,%d,%d)" % (urlid, wordid, i))

    def gettextonly(self, soup):
        v = soup.string
        if v == None:
            c = soup.contents
            if c != []:
                resulttext = ''
                for t in c:
                    subtext = self.gettextonly(t)
                    resulttext += subtext + '\n'
                return resulttext
            else:
                return ''
        else:
            return v.strip()

    def separatewords(self, text):
        return [s.lower() for s in re.split(r'\W*', text) if s != '']

    def isindexed(self, url):
        u = self.cursor.execute(
            "select id from urllist where url='%s'" % url).fetchone()
        if u != None:
            v = self.cursor.execute(
                "select * from wordlocation where urlid=%d" % u[0]).fetchone()
            if v != None:
                return True
        return False

    def addlinkref(self, urlFrom, urlTo, linkText):
        words = self.separatewords(linkText)
        fromid = self.getentryid('urllist', 'url', urlFrom)
        toid = self.getentryid('urllist', 'url', urlTo)
        if fromid == toid:
            return
        cur = self.cursor.execute(
            "insert into link(fromid,toid) values (%d,%d)" % (fromid, toid))
        linkid = cur.lastrowid
        for word in words:
            if word in ignorewords:
                continue
            wordid = self.getentryid(
                'wordlist', 'word', word)  # linkwords的作用是什么呢？
            self.cursor.execute(
                "insert into linkwords(linkid,wordid) values (%d,%d)" % (linkid, wordid))

    def crawl(self, pages, depth):  # 爬虫利用广度优先搜索，但注意栈溢出问题
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c = request.urlopen(page)
                except:
                    # print('Could not open %s' % page)
                    continue
                soup = BeautifulSoup(c.read(), 'html.parser')
                # print(soup.prettify())
                self.addtoindex(page, soup)

                links = soup('a')  # 对link处理得到URL
                # print(type(links))
                for link in links:
                    if 'href' in link.attrs:
                        url = parse.urljoin(page, link['href'])
                        if url.find(" ' ") != -1:
                            continue
                        url = url.split('#')[0]
                        # print(url)
                        if url[:4] == 'http' and not self.isindexed(url):
                            # 判断是否已做过索引
                            newpages.add(url)
                        linkText = self.gettextonly(link)
                        self.addlinkref(page, url, linkText)

                    self.dbcommit()
                pages = newpages

    def calculatepagerank(self, iterations=20):
        # 清除当前的pagerank
        self.con.execute('drop table if exists pagerank')
        self.con.execute('create table pagerank(urlid primary key,score)')

        # 初始化每一个url，令它等于1
        self.con.execute('insert into pagerank select rowid,1.0 from urllist')
        self.dbcommit()

        for i in range(iterations):
            #print("Iteration %d" % (i))
            for (urlid,) in self.con.execute('select rowid from urllist'):
                pr = 0.15
                # 循环所有指向这个页面的外部链接
                for (linker,) in self.con.execute('select distinct fromid from link where toid=%d' % urlid):
                    linkingpr = self.con.execute(
                        'select score from pagerank where urlid=%d' % linker).fetchone()[0]

                    # 根据链接源，求得总的连接数
                    linkingcount = self.con.execute(
                        'select count(*) from link where fromid=%d' % linker).fetchone()[0]
                    pr += 0.85 * (linkingpr / linkingcount)
                self.con.execute(
                    'update pagerank set score=%f where urlid=%d' % (pr, urlid))
        self.dbcommit()

    def createindextables(self):
        self.cursor.execute(
            'create table urllist (id integer primary key autoincrement, url)')
        self.cursor.execute(
            'create table wordlist (id integer primary key autoincrement, word)')
        self.cursor.execute(
            'create table wordlocation (id integer primary key autoincrement, urlid, wordid, location)')
        self.cursor.execute(
            'create table link (id integer primary key autoincrement, fromid integer, toid interger)')
        self.cursor.execute(
            'create table linkwords (id integer primary key autoincrement, wordid, linkid)')
        self.cursor.execute('create index wordidx on wordlist(word)')
        self.cursor.execute('create index urlidx on urllist(url)')
        self.cursor.execute('create index wordurlidx on wordlocation(wordid)')
        self.cursor.execute('create index urltoidx on link(toid)')
        self.cursor.execute('create index urlfromidx on link(fromid)')
        self.dbcommit()


class searcher(object):
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname)  # 在已经建立好的searchindex.db上进行操作
        self.cursor = self.con.cursor()

    def __del__(self):
        self.cursor.close()
        self.con.close()

    def getmatchrows(self, q):
        # 构造查询的字符串
        fieldlist = 'w0.urlid'
        tablelist = ''
        clauselist = ''
        wordids = []
        # 根据空格拆分单词
        words = q.split(' ')
        tablenumber = 0

        for word in words:
            # 获取单词的ID
            wordrow = self.cursor.execute(
                "select id from wordlist where word='%s'" % word).fetchone()
            if wordrow != None:
                wordid = wordrow[0]
                wordids.append(wordid)
                if tablenumber > 0:
                    tablelist += ','
                    clauselist += ' and '
                    clauselist += 'w%d.urlid=w%d.urlid and ' % (
                        tablenumber - 1, tablenumber)
                fieldlist += ',w%d.location' % tablenumber
                tablelist += 'wordlocation w%d' % tablenumber
                clauselist += 'w%d.wordid=%d' % (tablenumber, wordid)
                tablenumber += 1

        # 根据各个分组，建立查询
        fullquery = 'select %s from %s where %s' % (
            fieldlist, tablelist, clauselist)
        cur = self.cursor.execute(fullquery)
        rows = [row for row in cur]

        return rows, wordids

    def getscoredlist(self, rows, wordids):
        totalscores = dict([(row[0], 0) for row in rows])

        # 此处放置评价函数
        weights = [(1.0, self.frequencyscore(rows)), (1.5, self.locationscore(rows)), (2.0, self.distancescore(
            rows)), (2.0, self.pagerankscore(rows)), (5.0, self.nnscore(rows, wordids))]

        for weight, scores in weights:
            for url in totalscores:
                totalscores[url] += weight * scores[url]
        return totalscores

    def geturlname(self, id):
        return self.cursor.execute("select url from urllist where id=%d" % id).fetchone()[0]

    def query(self, q):
        rows, wordids = self.getmatchrows(q)
        scores = self.getscoredlist(rows, wordids)
        rankedscores = sorted([(score, url)
                               for url, score in scores.items()], reverse=1)
        for (score, urlid) in rankedscores[0:10]:
            print('%f\t%s' % (score, self.geturlname(urlid)))
        # 该结果可直接被传入到trainquery中进行神经网络训练
        # return wordids, [r[1] for r in rankedscores[0:10]]

    def frequencyscore(self, rows):  # 单词频度
        counts = dict([(row[0], 0) for row in rows])
        for row in rows:
            counts[row[0]] += 1
            return self.normalizescores(counts)

    def locationscore(self, rows):  # 单词位置
        locations = dict([(row[0], 1000000) for row in rows])
        for row in rows:
            loc = sum(row[1:])
            if loc < locations[row[0]]:
                locations[row[0]] = loc
        return self.normalizescores(locations, smallIsBetter=1)

    def distancescore(self, rows):  # 单词距离
        # 如果仅有一个单词则得分一样
        if len(rows[0]) <= 2:
            return dict([(row[0], 1.0) for row in rows])
        # 初始化字典，并且填入一个很大的数字
        mindistance = dict([(row[0], 1000000) for row in rows])

        for row in rows:
            dist = sum([abs(row[i] - row[i - 1]) for i in range(2, len(row))])
            if dist < mindistance[row[0]]:
                mindistance[row[0]] = dist
        return self.normalizescores(mindistance, smallIsBetter=1)

    def inboundlinkscore(self, rows):  # 外部回指链接
        uniqueurls = set([row[0] for row in rows])
        inboundcount = dict([(u, self.cursor.execute(
            "select count(*) from link where toid=%d" % u).fetchone()[0]) for u in uniqueurls])
        return self.normalizescores(inboundcount)

    def pagerankscore(self, rows):  # 根据PageRank算法结果进行排序
        pageranks = dict([(row[0], self.cursor.execute(
            'select score from pagerank where urlid=%d' % row[0]).fetchone()[0]) for row in rows])
        maxrank = max(pageranks.values())
        normalizedscores = dict([(u, float(l) / maxrank)
                                 for (u, l) in pageranks.items()])
        return normalizedscores

    def linktextscore(self, rows, wordids):
        linkscores = dict([(row[0], 0) for row in rows])
        for wordid in wordids:
            cur = self.cursor.execute(
                'select link.fromid,link.toid from linkwords,link where wordid=%d and linkwords.linkid=link.id' % wordid)
            for (fromid, toid) in cur:
                if toid in linkscores:
                    pr = self.cursor.execute(
                        'select score from pagerank where urlid=%d' % fromid).fetchone()[0]
                    linkscores[toid] += pr
        maxscore = max(linkscores.values())
        normalizedscores = dict([(u, float(l) / maxscore)
                                 for (u, l) in linkscores.items()])
        return normalizedscores

    # 归一化处理：使评价值介于0-1之间(1代表最佳结果)，因此能将不同方法返回的结果进行比较
    def normalizescores(self, scores, smallIsBetter=0):
        vsmall = 0.00001  # 避免被零整除
        if smallIsBetter:
            minscore = min(scores.values())
            return dict([(u, float(minscore) / max(vsmall, l)) for (u, l) in scores.items()])
        else:
            maxscore = max(scores.values())
            if maxscore == 0:
                maxscore = vsmall
            return dict([(u, float(c) / maxscore) for (u, c) in scores.items()])

    def nnscore(self, rows, wordids):
        # 获得一个由唯一的URL ID构成的有序列表
        urlids = [urlid for urlid in set([row[0] for row in rows])]
        nnres = mynet.getresult(wordids, urlids)  # 之前已经做过大量的不同样例训练，训练是如何进行的呢
        scores = dict([(urlids[i], nnres[i]) for i in range(len(self.urlids))])
        return self.normalizescores(scores)


test = crawler('searchindex.db')
test.createindextables()  # 建立完table就可以不再运行了
test.crawl(['https://en.wikipedia.org/wiki/2018_Hualien_earthquake'], 1)
test.calculatepagerank()
# mynet.maketables()
# mynet.trainquery([wWorld, wBank], [uWorldBank,
#                                    uRiver, uEarth], uWorldBank)  # 从点击中学习，但无法获取用户的实际点击情况

test1 = searcher('searchindex.db')
test1.query('ready user')
