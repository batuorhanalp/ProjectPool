'use strict';

angular.module('mean.system', ['mean.controllers.login','mean-factory-interceptor']);

/*
$(function(){
	$('.expand').click(function(event) {
		var parentObject = $(event.target).parent().parent();
		var detail = $(parentObject).find('.detail');
		if($(event.target).hasClass('expanded')){
			$(detail).hide(0, function() {
				$(parentObject).find('.right').height(65);
				$(parentObject).find('.settings').css('display', 'none');
				$(event.target).removeClass('expanded');
				$(parentObject).find('.settingsMenu').css('display', 'none');
				$(parentObject).find('.settings').removeClass('opened');
			});
		}else{
			$(detail).show(0, function() {
				$(parentObject).find('.right').height(parentObject.height());
				$(parentObject).find('.settings').css('display', 'block');
				$(event.target).addClass('expanded');
			});
		}
	});
	$('.settings').click(function(event) {
		var parentObject = $(event.target).parent().parent();
		if($(event.target).hasClass('opened')){
			$(parentObject).find('.settingsMenu').css('display', 'none');
			$(event.target).removeClass('opened');
		}else{
			$(parentObject).find('.right').height(parentObject.height());
			$(parentObject).find('.settingsMenu').css('margin-top', $(parentObject).find('.right').height() + 'px');
			$(parentObject).find('.settingsMenu').css('display', 'block');
			$(event.target).addClass('opened');
		}
	});
});
*/
