// JavaScript Document
/**
        * 通过后台查询数据
        */
        function selectData() {
            var opType = "select";  //查询数据
            var tableName = "疫情数据";  //数据表名称
            var date="2020-";

            var month_select=document.getElementById("select_month");
            var month_index=month_select.selectedIndex;
            var month=month_select.options[month_index].value;

            var day_select=document.getElementById("select_day");
            var day_index=day_select.selectedIndex;
            var day=day_select.options[day_index].value;

            date=date+month+"-"+day;

            $.ajax({
                url: 'ReadData.ashx', //请求地址
                type: 'POST',  //请求方式为post
                data: { 'type': opType, 'table': tableName,'date':date }, //传入参数
                dataType: 'json', //返回数据格式
                //请求成功完成后要执行的方法
                success: showData,
                error: function (err) {
                    alert("执行失败");
                }
            });
        }

function test()
{
    alert("22");
    $.ajax({
                url: 'china.geojson', //请求地址
                type: 'GET',  //请求方式为post
                 //传入参数
                dataType: 'json', //返回数据格式
                //请求成功完成后要执行的方法
                success: test2,
                error: function (err) {
                    alert("执行失败");
                }
            });
}
function test2(data)
{
	var obj=eval(data);
	alert(obj);
}

function showData(data)
{
	alert("3");
    var obj=eval(data);
    for(var i=0;i<obj.length;i++)
    {
        item=obj[i];
        //alert(item.省份+",新增确诊"+item.新增确诊);
        var feature = new ol.Feature({                  
            name: item.省份,
            confirm: item.累积确诊,
            heal: item.治愈,
            death: item.死亡,
            new_confirm: item.新增确诊
        });
        vectSource.addFeature(feature);
	}
    map.on('pointermove', showTest, this); //添加鼠标移动事件监听，捕获要素时添加热区功能
	document.getElementById("text").value='222';
}
function showTest(e)
{
    var pixel = map.getEventPixel(e.originalEvent);
            var hit = map.hasFeatureAtPixel(pixel);
            map.getTargetElement().style.cursor = hit ? 'pointer' : '';//改变鼠标光标状态
            if (hit) {
                //当前鼠标位置选中要素
                var feature = map.forEachFeatureAtPixel(e.pixel,
                    function (feature, layer) {
                        return feature;
                    });
                //如果当前存在热区要素
                if (feature) {
                    //显示热区图层
                    hotSpotsLayer.setVisible(true);
                    //控制添加热区要素的标识（默认为false）
                    if (preFeature != null) {
                        if (preFeature === feature) {
                            flag = true; //当前鼠标选中要素与前一个选中要素相同
                        }
                        else {
                            flag = false; //当前鼠标选中要素不是前一个选中要素
                            hotSpotsSource.removeFeature(preFeature); //前一热区要素移除
                            preFeature = feature; //更新前一个热区要素对象
                        }
                    }
                    //如果当前选中要素与之前选中要素不同，在热区绘制层添加当前要素
                    if (!flag) {
                        $(element).popover('destroy'); //销毁popup
                        flashFeature = feature; //当前热区要素
                        flashFeature.setStyle(flashStyle); //设置要素样式
                        hotSpotsSource.addFeature(flashFeature); //添加要素
                        hotSpotsLayer.setVisible(true); //显示热区图层
                        preFeature = flashFeature; //更新前一个热区要素对象
                    }

                    popup.setPosition(e.coordinate); //设置popup的位置
                    $(element).popover({
                        placement: 'top',
                        html: true,
                        content: '省名：' + feature.get('name') + '</br>' +
                            '累积确诊：' + feature.get('confirm') + '</br>' +
                             '治愈：' + feature.get('heal') + '</br>' +
                              '死亡：' + feature.get('death')+ '</br>' +
                              '新增确诊：'+feature.get('new_confirm')
                    });
                    $(element).css("width", "200px");
                    $(element).popover('show'); //显示popup
                }

                else {
                    hotSpotsSource.clear(); //清空热区图层数据源
                    flashFeature = null; //置空热区要素
                    $(element).popover('destroy'); //销毁popup
                    hotSpotsLayer.setVisible(false); //隐藏热区图层
                }
            }
            else {
                $(element).popover('destroy'); //销毁popup
                hotSpotsLayer.setVisible(false); //隐藏热区图层
            }
}
