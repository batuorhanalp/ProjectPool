'use strict';

angular.module('mean').config(['$stateProvider',
    function($stateProvider) {
        $stateProvider
            .state('all ideas', {
                url: '/ideas',
                templateUrl: 'ideas/views/list.html'
            })
            .state('idea by id', {
                url: '/ideas/:ideaId',
                templateUrl: 'idea/views/view.html'
            })
            .state('ideas example page', {
                url: '/ideas/example',
                templateUrl: 'ideas/views/index.html'
            });
    }
]);
