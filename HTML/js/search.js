var mouse_is_inside = false;
$(function(){
	$('.search > .inner-wrapper > .right > a').click(function(){
		if(!$('.search > .detail').is(':visible')){
			$('.search > .detail').show(0);
		}else{
			closeSearchDetail();
		}
	});
	$('.search > .detail > .close').click(function(){
		closeSearchDetail();
	});
	function closeSearchDetail(){
		$('.search > .detail').hide(0);
	}
	$('.scroller').mCustomScrollbar();
	$('.select').hover(function(){ 
        mouse_is_inside=true; 
    }, function(){ 
        mouse_is_inside=false; 
    });

    $("body").mouseup(function(){ 
        if(! mouse_is_inside) $('.list').hide();
    });
	$('.select').click(function(){
		var list = $('#' + this.id + ' .list');
		$('.list').hide();
		if($(list).is(':visible')){
			$(list).hide(0);
		}else{
			$(list).show(0);
		}
	});
	$.datepicker.regional['tr'] = {
                closeText: 'kapat',
                prevText: '&#x3c;geri',
                nextText: 'ileri&#x3e',
                currentText: 'bugün',
                monthNames: ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran',
                'Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık'],
                monthNamesShort: ['Oca','Şub','Mar','Nis','May','Haz',
                'Tem','Ağu','Eyl','Eki','Kas','Ara'],
                dayNames: ['Pazar','Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi'],
                dayNamesShort: ['Pz','Pt','Sa','Ça','Pe','Cu','Ct'],
                dayNamesMin: ['Pz','Pt','Sa','Ça','Pe','Cu','Ct'],
                weekHeader: 'Hf',
                dateFormat: 'dd.mm.yy',
                firstDay: 1,
                isRTL: false,
                showMonthAfterYear: false,
                yearSuffix: ''};
        $.datepicker.setDefaults($.datepicker.regional['tr']);
	$( ".datepicker" ).datepicker();
	$("#bttnSearch").click(function(){
		var brands = new Array();
		var brandsSold = new Array();
		var categories = new Array();
		var budgets = new Array();
		var dtFirst = $('#dtFirst').val();// == undefined ? '':$('#dtFirst').val();
		var dtSecond = $('#dtSecond').val();// == undefined ? '':$('#dtSecond').val();
		var details = $('#txtDetail').val();// == undefined ? '':$('#txtDetail').val();
		$('#ddlBrands input:checkbox').each(function(){
			if(this.checked){
				brands.push($(this).data('id'));
			}
		});
		$('#ddlBrandsSold input:checkbox').each(function(){
			if(this.checked){
				brandsSold.push($(this).data('id'));
			}
		});
		$('#ddlCategories input:checkbox').each(function(){
			if(this.checked){
				categories.push($(this).data('id'));
			}
		});
		$('#ddlBudgets input:checkbox').each(function(){
			if(this.checked){
				budgets.push($(this).data('id'));
			}
		});
		var data = {brands:brands,brandsSold:brandsSold,categories:categories,dtFirst:dtFirst,dtSecond:dtSecond,details:details};
		var dataJson = JSON.stringify(data);
	});
});