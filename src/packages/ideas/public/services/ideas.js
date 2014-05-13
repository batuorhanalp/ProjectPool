'use strict';

angular.module('mean').factory('Ideas', ['$resource',
	function($resource) {
		return $resource('ideas/:ideaId', {
			ideaId: '@_id'
		}, {
			update: {
				method: 'PUT'
			}
		});
	}
]);
