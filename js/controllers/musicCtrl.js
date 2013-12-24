var musicApp = angular.module('musicApp', []);

musicApp.controller('MusicCtrl', function ($scope, $http) {

	$scope.events = {};
	$http.get('philly-concerts/events.json').success(function (result) {
		$scope.events = result;
	});
});
