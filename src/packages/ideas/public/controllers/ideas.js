'use strict';

angular.module('mean').controller('IdeasController', ['$scope', '$stateParams', '$location', 'Global', 'Ideas',
    function($scope, $stateParams, $location,  Global, Ideas) {
        $scope.global = Global;
        //$scope.ideas = {
        //    name: 'ideas'
        //};

            console.log('inside controller: ', Ideas, $stateParams);
        /**
         * List articles
         */
        $scope.find = function() {
            console.log('inside find: ', Ideas);
            Ideas.query(function(ideas) {
                $scope.ideas = ideas;
            });
        };

        $scope.findOne = function() {
            Ideas.get({
                ideaId: $stateParams.ideaId
            }, function(idea) {
                $scope.idea = idea;
            });
        };
    }
]);
