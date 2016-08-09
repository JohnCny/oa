//切换iframe里的内容用于iframe内部页面	
function iframe(page){
	window.location.href = page;
	//window.location.href = "/" + page;
	// alert(window.location.href);
}
var date=new Date();
var year=date.getFullYear();
var month=creattime(date.getMonth()+1);
var day=creattime(date.getDate()); 
function creattime(i){
	if(i<10)
		{i="0"+i};
	return i;
}
function datepicker(){
	$('.datepicker').datepicker();
	//给空的datepicker一个默认当天值
	$('.datepicker').each(function(){
		if(this.value==""){
			this.value=year+"-"+month+"-"+day;
		}
	});
}
function addTd(table){
    if(table=="bxmx"){//是否申请过贷款
        $("#"+table).append("<tr>"+
								"<td class='pull-right'>金额：</td>"+
								"<td><input type='text' class='short' name='money' onchange='totleMoney()'/>元</td>"+
								"<td class='pull-right'>报销事由：</td>"+
								"<td>"+
									"<select class='short'>"+
										"<option>--请选择--</option>"+						
									"</select>"+
								"</td>"+
								"<td class='pull-right'>描述：</td>"+
								"<td><textarea></textarea></td>"+
							"</tr>");      
    }
}
//表格删除行
function removeTd(table){  
	var tr= document.getElementById(table).getElementsByTagName("tr");
	if(tr.length>1){//至少要保留一行
		document.getElementById(table).deleteRow(tr.length-1);//删除最后一行
	}
}

/*全选*/
function checkAll(obj,name){
	var arrSon = document.getElementsByName(name);
	//alert($(obj).attr("checked"))
	if($(obj).attr("checked")!="checked"){
		for(i=0;i<arrSon.length;i++) {
			if(arrSon[i].checked!=false)
				arrSon[i].click();
		}$(obj).removeAttr("checked")
		//$(obj).attr("checked","checked")
	}
	else{
		
		for(i=0;i<arrSon.length;i++) {
			if(arrSon[i].checked!=true)
				arrSon[i].click();
		}$(obj).attr("checked","checked")
		//$(obj).removeAttr("checked")
	}//alert($(obj).attr("checked"))
}





