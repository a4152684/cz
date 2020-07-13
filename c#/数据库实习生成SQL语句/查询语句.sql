select Name as ����������, Shape.STEnvelope().STAsText() as �߽�, Shape.STEnvelope() from buildings #��ѯÿ��������ı߽�

select Name as ����������, Shape.STArea() as �������, Area as ������� from buildings #��ѯÿ������������

select Name as ��·����, Shape.STLength() as ���㳤��, Length as ���볤�� from roads #��ѯÿ����·�ĳ���

select Name as ��·����, Shape.STBuffer(20).STAsText() as ������, Shape.STBuffer(20) from roads #Ϊÿ����·����������

#ÿ����·�������������Ӱ�쵽�Ľ�����
select r.Name as ��·����,b.Name as ���������� from roads r, buildings b   
where b.Shape.STIntersects(r.Shape.STBuffer(20)) = '1'

#��ѯ��·��Խ������Ĳ���
select r.Name as ��·����, b.Name as ����������, r.Shape.STIntersection(b.Shape).STAsText() as �ཻ����
from roads r, buildings b
where r.Shape.STIntersects(b.Shape) = '1' 

#��ѯ��4��¥�����ҽԺ�ͳ��еľ���
declare @shape geometry
set @shape =(select Shape from buildings where name='4��¥')
select m.Name as ����, @shape.STDistance(m.Location) as ���е�4��¥�ľ���,
h.Name as ҽԺ, @shape.STDistance(h.Location) as ҽԺ��4��¥�ľ���
from markets m, hospitals h
where @shape.STDistance(m.Location) <= all(select @shape.STDistance(m2.Location) from markets m2)
and @shape.STDistance(h.Location)<=all(select @shape.STDistance(h2.Location) from hospitals h2)

select m.Name as ����, b.Shape.STDistance(m.Location) as ���е�4��¥�ľ���,
h.Name as ҽԺ, b.Shape.STDistance(h.Location) as ҽԺ��4��¥�ľ���
from markets m, hospitals h,buildings b
where b.Name='4��¥' and 
b.Shape.STDistance(m.Location) <= all(select b.Shape.STDistance(m2.Location) from markets m2) and
b.Shape.STDistance(h.Location) <= all(select b.Shape.STDistance(h2.Location) from hospitals h2) 