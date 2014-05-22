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
	$('.select').click(function(){
		var list = $('#' + this.id + ' .list');
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
});