select Name as 建筑物名称, Shape.STEnvelope().STAsText() as 边界, Shape.STEnvelope() from buildings #查询每栋建筑物的边界

select Name as 建筑物名称, Shape.STArea() as 计算面积, Area as 导入面积 from buildings #查询每栋建筑物的面积

select Name as 道路名称, Shape.STLength() as 计算长度, Length as 导入长度 from roads #查询每条道路的长度

select Name as 道路名称, Shape.STBuffer(20).STAsText() as 缓冲区, Shape.STBuffer(20) from roads #为每条道路构建缓冲区

#每条道路构建缓冲区后会影响到的建筑物
select r.Name as 道路名称,b.Name as 建筑物名称 from roads r, buildings b   
where b.Shape.STIntersects(r.Shape.STBuffer(20)) = '1'

#查询道路穿越建筑物的部分
select r.Name as 道路名称, b.Name as 建筑物名称, r.Shape.STIntersection(b.Shape).STAsText() as 相交区域
from roads r, buildings b
where r.Shape.STIntersects(b.Shape) = '1' 

#查询与4号楼最近的医院和超市的距离
declare @shape geometry
set @shape =(select Shape from buildings where name='4号楼')
select m.Name as 超市, @shape.STDistance(m.Location) as 超市到4号楼的距离,
h.Name as 医院, @shape.STDistance(h.Location) as 医院到4号楼的距离
from markets m, hospitals h
where @shape.STDistance(m.Location) <= all(select @shape.STDistance(m2.Location) from markets m2)
and @shape.STDistance(h.Location)<=all(select @shape.STDistance(h2.Location) from hospitals h2)

select m.Name as 超市, b.Shape.STDistance(m.Location) as 超市到4号楼的距离,
h.Name as 医院, b.Shape.STDistance(h.Location) as 医院到4号楼的距离
from markets m, hospitals h,buildings b
where b.Name='4号楼' and 
b.Shape.STDistance(m.Location) <= all(select b.Shape.STDistance(m2.Location) from markets m2) and
b.Shape.STDistance(h.Location) <= all(select b.Shape.STDistance(h2.Location) from hospitals h2) 