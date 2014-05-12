'use strict';

angular.module('mean.system', ['mean.controllers.login','mean-factory-interceptor']);

angular.element(function(){
	angular.element('.expand').click(function(event) {
		var parentObject = angular.element(event.target).parent().parent();
		var detail = angular.element(parentObject).find('.detail');
		if(angular.element(event.target).hasClass('expanded')){
			angular.element(detail).hide(0, function() {
				angular.element(parentObject).find('.right').height(65);
				angular.element(parentObject).find('.settings').css('display', 'none');
				angular.element(event.target).removeClass('expanded');
				angular.element(parentObject).find('.settingsMenu').css('display', 'none');
				angular.element(parentObject).find('.settings').removeClass('opened');
			});
		}else{
			angular.element(detail).show(0, function() {
				angular.element(parentObject).find('.right').height(parentObject.height());
				angular.element(parentObject).find('.settings').css('display', 'block');
				angular.element(event.target).addClass('expanded');
			});
		}
	});
	angular.element('.settings').click(function(event) {
		var parentObject = angular.element(event.target).parent().parent();
		if(angular.element(event.target).hasClass('opened')){
			angular.element(parentObject).find('.settingsMenu').css('display', 'none');
			angular.element(event.target).removeClass('opened');
		}else{
			angular.element(parentObject).find('.right').height(parentObject.height());
			angular.element(parentObject).find('.settingsMenu').css('margin-top', angular.element(parentObject).find('.right').height() + 'px');
			angular.element(parentObject).find('.settingsMenu').css('display', 'block');
			angular.element(event.target).addClass('opened');
		}
	});
});
