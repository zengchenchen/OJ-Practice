from math import tanh
import sqlite3


# 查询条件有几种情况：单词数目为1、2、3，单词组合之前匹配过或者没有经过神经网络训练过

# dtanh函数代表tanh函数的斜率
def dtanh(y):
    return 1.0 - y * y


class searchnet(object):
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname)
        self.cursor = self.con.cursor()

    def __del__(self):
        self.cursor.close()
        self.con.close()

    def maketables(self):
        self.cursor.execute(
            'create table hiddennode(id integer primary key autoincrement, create_key)')
        self.cursor.execute(
            'create table wordhidden(id integer primary key autoincrement, fromid, toid, strength)')
        self.cursor.execute(
            'create table hiddenurl(id integer primary key autoincrement, fromid, toid, strength)')
        self.con.commit()

    # 用以判断当前连接的强度，layer代表什么：一共有两层，0与1.
    def getstrength(self, fromid, toid, layer):
        if layer == 0:
            table = 'wordhidden'
        else:
            table = 'hiddenurl'
        res = self.cursor.execute('select strength from %s where fromid=%d and toid=%d' % (
            table, fromid, toid)).fetchone()
        if res == None:
            if layer == 0:
                return -0.2  # 单词层到隐藏层的连接，strength=-0.2
            if layer == 1:
                return 0     # 从隐藏层到URL的连接，strength=0
        return res[0]

    # 用以判断连接是否已存在，利用新的strength更新连接或者创造连接
    def setstrength(self, fromid, toid, layer, strength):
        if layer == 0:
            table = 'wordhidden'
        else:
            table = 'hiddenurl'
        res = self.cursor.execute('select id from %s where fromid=%d and toid=%d' % (
            table, fromid, toid)).fetchone()
        if res == None:
            self.cursor.execute('insert into %s (fromid,toid,strength) values (%d,%d,%f)' % (
                table, fromid, toid, strength))  # 创造连接
        else:
            id = res[0]
            self.cursor.execute(
                'update %s set strength=%f where id=%d' % (table, strength, id))  # 更新连接

    # 每传入一组以前从未见过的单词组合，就会在隐藏层中新建一个节点，在需要时建立新的隐藏节点会更高效、简单
    def generatehiddennode(self, wordids, urls):
        if len(wordids) > 3:  # 单词组合大于3的情况不考虑,如果是单词只有1呢？
            return None
        # 检查我们是否已经为这组单词建好一个节点
        createkey = '_'.join(sorted([str(wi) for wi in wordids]))
        res = self.cursor.execute(
            'select id from hiddennode where create_key="%s"' % createkey).fetchone()
        # 如果没有则创建之
        if res == None:
            cur = self.cursor.execute(
                'insert into hiddennode (create_key) values ("%s")' % createkey)
            hiddenid = cur.lastrowid
            # 设置默认权重
            for wordid in wordids:
                self.setstrength(wordid, hiddenid, 0, 1.0 / len(wordids))
                for urlid in urls:
                    self.setstrength(hiddenid, urlid, 1, 0.1)
                self.con.commit()

    # 从隐藏层中找出与某种查询相关的所有节点，wordids中的单词组合必须是已出现过的吗？
    def getallhiddenids(self, wordids, urlids):
        l1 = {}
        for wordid in wordids:  # 找出与查询条件关联的隐藏节点
            cur = self.cursor.execute(
                'select toid from wordhidden where fromid=%d' % wordid)
            for row in cur:
                l1[row[0]] = 1
        for urlid in urlids:  # 找出与查询URL关联的隐藏节点
            cur = self.cursor.execute(
                'select fromid from hiddenurl where toid=%d' % urlid)
            for row in cur:
                l1[row[0]] = 1
        return list(l1.keys())

    # 为searchnet定义了多个实例变量，已构造了只与查询条件中的单词有关的网络
    def setupnetwork(self, wordids, urlids):
        # 值列表
        self.wordids = wordids
        self.hiddenids = self.getallhiddenids(wordids, urlids)
        self.urlids = urlids
        # 节点输出
        self.ai = [1.0] * len(self.wordids)  # [1.0]*2=[1.0, 1.0]
        self.ah = [1.0] * len(self.hiddenids)
        self.ao = [1.0] * len(self.urlids)
        # 建立权重矩阵
        self.wi = [[self.getstrength(wordid, hiddenid, 0)
                    for hiddenid in self.hiddenids] for wordid in self.wordids]
        self.wo = [[self.getstrength(hiddenid, urlid, 1)
                    for urlid in self.urlids] for hiddenid in self.hiddenids]

    # 构造前馈算法，wordids里单词组合必须是已出现过的吗？
    def feedforward(self):
        # 查询单词是仅有的输入
        for i in range(len(self.wordids)):
            self.ai[i] = 1.0
        # 隐藏层节点的活跃程度
        for j in range(len(self.hiddenids)):
            sum = 0.0
            for i in range(len(self.wordids)):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = tanh(sum)  # tanh：激活函数，解决非线性问题
        # 输出层节点活跃程度
        for k in range(len(self.urlids)):
            sum = 0.0
            for j in range(len(self.hiddenids)):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = tanh(sum)
        return self.ao[:]  # 节点输出结果并非从0或者1？

    def getresult(self, wordids, urlids):
        self.setupnetwork(wordids, urlids)  # 第一步建立神经网络
        return self.feedforward()  # 第二步利用前馈法求解值

    # 利用反向传播算法，先计算误差再对权重加以调节
    def backPropagate(self, targets, N=0.5):  # N代表什么？
        # 计算输出层的误差
        output_deltas = [0.0] * len(self.urlids)
        for k in range(len(self.urlids)):
            error = targets[k] - self.ao[k]  # targets=[0,1,0,0,...,0]代表期望输出结果
            output_deltas[k] = dtanh(self.ao[k]) * \
                error  # 利用dtanh函数确定节点的总输入需要如何改变
        # 计算隐藏层的误差
        hidden_deltas = [0.0] * len(self.hiddenids)
        for j in range(len(self.hiddenids)):
            error = 0.0
            for k in range(len(self.urlids)):
                error = error + output_deltas[k] * \
                    self.wo[j][k]  # 初始权重wo=[0.1,0.1,...,0.1]
            hidden_deltas[j] = dtanh(self.ah[j]) * error
        # 更新输出权重
        for j in range(len(self.hiddenids)):
            for k in range(len(self.urlids)):
                change = output_deltas[k] * self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N * change
        # 更新输入权重
        for i in range(len(self.wordids)):
            for j in range(len(self.hiddenids)):
                change = hidden_deltas[j] * self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N * change

    # 神经网络训练一次
    def trainquery(self, wordids, urlids, selectedurl):
        # 如有必要，生成一个隐藏节点(id,create_key)，网络已构建好
        self.generatehiddennode(wordids, urlids)
        self.setupnetwork(wordids, urlids)  # 实例变量
        self.feedforward()
        targets = [0.0] * len(urlids)
        targets[urlids.index(selectedurl)] = 1.0
        self.backPropagate(targets)
        self.updatedatabase()

    # 更新数据库的权重值(反向传播算法更新的self.wi,self.wo是实例变量，权重储存在wordhidden,hiddenid数据库中，故需要更新数据库以保存已更新的strength)
    def updatedatabase(self):
        # 将值存入数据库中
        for i in range(len(self.wordids)):
            for j in range(len(self.hiddenids)):
                self.setstrength(
                    self.wordids[i], self.hiddenids[j], 0, self.wi[i][j])
        for j in range(len(self.hiddenids)):
            for k in range(len(self.urlids)):
                self.setstrength(
                    self.hiddenids[j], self.urlids[k], 1, self.wo[j][k])
        self.con.commit()


mynet = searchnet('nn.db')
# mynet.maketables()
wWorld, wBank = 1, 2
uWorldBank, uRiver, uEarth = 11, 12, 13
mynet.trainquery([wWorld, wBank], [uWorldBank,
                                   uRiver, uEarth], uWorldBank)
print(mynet.getresult([wWorld, wBank], [uWorldBank, uRiver, uEarth]))
