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
});