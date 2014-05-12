'use strict';

angular.module('mean').config(['$stateProvider',
    function($stateProvider) {
        $stateProvider.state('ideas example page', {
            url: '/ideas/example',
            templateUrl: 'ideas/views/index.html'
        });
    }
]);
