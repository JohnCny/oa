//切换iframe里的内容用于主页面
function Iframe(src){
	$('#iframe').attr('src',src)
}

function showMenu(obj){//一级菜单
	if($(obj).html().indexOf("ul")>0){//单击项如果有二级菜单
		$(obj).parent().find(".second-nav").slideUp("100");//隐藏菜单中所有二级菜单
		$(obj).parent().find(".active").each(function(){//遍历菜单中已选择项是否有二级菜单
			if($(this).html().indexOf("ul")>0)//已选中项有二级菜单
				$(this).attr("class","menu-list");//取消选中样式，否则不取消
		});
		
		$(obj).find(".second-nav").slideDown("200");//显示单击项的二级菜单	
		$(obj).attr("class","active");//单击项样式改为选中	
	}		
	else{//如果单击项没二级菜单
		$(obj).parent().find(".second-nav").slideUp("100");//隐藏所有二级菜单
		$(obj).parent().find(".active").attr("class","menu-list")//取消一级菜单所有选中样式
		$(obj).parent().find(".second-active").attr("class","")//取消二级菜单所有选中样式			
		$(obj).attr("class","active")//单击项样式改为选中
	}
}

function checkSecond(obj,e){//二级菜单
	$(obj).parent().parent().parent().find(".active").attr("class","menu-list")//取消一级菜单所有选中样式
	$(obj).parent().parent().parent().find(".second-active").attr("class","")//取消二级菜单所有选中样式			
	$(obj).parent().parent().attr("class","active")//单击项所在一级菜单样式改为选中
	$(obj).attr("class","second-active")////单击项所在二级菜单样式改为选中
	//e.cancelBubble(); 
	e.stopPropagation();//取消冒泡，不执行父类showMenu(obj)事件
}