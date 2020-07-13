import pandas as pd


def find_id(end, node_id):
    for j in range(length):
        if end == Node_first[j]:
            node_id.append(Node_last[j])
            find_id(Node_last[j], node_id)
    return

spl="--"
data = pd.read_excel(r"E:\曹臻个人\专业课\城市规划原理\用水量计算.xlsx", header=0 ,sheet_name="Sheet2")
Q = data['沿线流量'].tolist()
ID = data['管段编号'].tolist()
length = len(Q)
Node_first = [int(i.split(spl)[0]) for i in ID]
Node_last = [int(i.split(spl)[1]) for i in ID]

Node_num = max(Node_last)
a = list(range(1, Node_num + 1))#节点
b = []#连接管道
c = []#节点流量
d = [0] * Node_num #存储集中流量
e = []#节点总流量
Q_data = input('请输入集中流量,用--隔开,例如（5--14,4--5--15):\n')
Q_d = Q_data.split(',')
for i in Q_d:
    d[int(i.split(spl)[0]) - 1] = float(i.split(spl)[1])

for i in range(Node_num):
    Nodes = [
        j for j in range(length)
        if ((i + 1) == Node_first[j]) or ((i + 1) == Node_last[j])
    ]
    s = '0.5 * ('
    ss = ''
    num = 0
    for Node in Nodes:
        num += 0.5 * Q[Node]
        s = s + format(Q[Node], '.1f')
        s += ' + '
        ss += ID[Node]
        ss += " "
    e0 = d[i] + num
    s = s[:-3] + ') = ' + format(num, '.1f')
    b.append(ss)
    c.append(s)
    e.append(format(e0, '.2f'))

""" writer = pd.ExcelWriter(r"E:\曹臻个人\专业课\城市规划原理\计算题结果.xlsx")
df = {'节点': a, '连接管道': b, '节点流量': c, '集中流量': d, '节点总流量': e}
df = pd.DataFrame(df)
df.to_excel(writer, index=None)
writer.save()
print("end") """

side = input('请输入你想计算的管道编号,逗号分隔:\n')
sides = side.split(',')

for i in sides:
    end = int(i.split(spl)[1])
    node_id = []
    node_id.append(end)
    find_id(end, node_id)
    q = 0
    for j in node_id:
        q += float(e[j - 1])
    print(i + '管道的流量为' + format(q, '.2f') + '\n')
