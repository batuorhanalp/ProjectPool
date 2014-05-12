'use strict';

angular.module('mean').controller('IdeasController', ['$scope', 'Global',
    function($scope, Global, Ideas) {
        $scope.global = Global;
        $scope.ideas = {
            name: 'ideas'
        };
    }
]);
