var app = angular.module('bitcoinchart', ['ui.router', 'angles', 'app.filters']);

app.config(['$stateProvider','$urlRouterProvider', '$locationProvider',
        function($stateProvider, $urlRouterProvider, $locationProvider) {
    $urlRouterProvider.otherwise('/minutely');
    
    $stateProvider
    .state('minutely', {
        url : "/minutely",
        templateUrl : "/static/partials/minutely.html",
        controller : "MinutelyController"
    })
    .state('hourly', {
        url : "/hourly",
        templateUrl : "/static/partials/hourly.html",
        controller : "HourlyController"
    })
    .state('daily', {
        url : "/daily",
        templateUrl : "/static/partials/daily.html",
        controller : "DailyController"
    });

    $locationProvider.html5Mode(false);
}]);

app.controller('MinutelyController', ['$scope', '$http', 
        function($scope, $http) {

    $http.get('/api/v1/minutely').success(function(data) {
        $scope.bitcoinData = data.data;

        var chartLabels = [];
        var bidPrice = [];
        var askPrice = [];


        for (var i = 0; i < 30; i++){
            chartLabels.push(i);
        }

        if ($scope.bitcoinData.length > 30) {
            var j = $scope.bitcoinData.length - 30;

            for (j; j < $scope.bitcoinData.length; j++) {
                bidPrice.push($scope.bitcoinData[j].bid);
                askPrice.push($scope.bitcoinData[j].ask);
            }
        } else {
            for (var k in $scope.bitcoinData){
                bidPrice.push($scope.bitcoinData[k].bid);
                askPrice.push($scope.bitcoinData[k].ask);
            }
        }

        $scope.chart = {
            labels : chartLabels,
            datasets : [
                    {
                            fillColor : "rgba(39,124,242,0)",
                            strokeColor: "rgba(39,124,242,1)",
                            pointColor: "rgba(39,124,242,1)",
                            pointStrokeColor : "#fff",
                            data : bidPrice
                    },
                    {
                            fillColor : "rgba(255,0,251,0)",
                            strokeColor: "rgba(255,0,251,1)",
                            pointColor: "rgba(255,0,251,1)",
                            pointStrokeColor : "#fff",
                            data : askPrice
                    }
            ]
        };
    });
}]);
app.controller('HourlyController', ['$scope', '$http', 
        function($scope, $http) {

    $http.get('/api/v1/hourly').success(function(data) {
        $scope.bitcoinData = data.data;

        var chartLabels = [];
        var bidPrice = [];
        var askPrice = [];


        for (var i = 1; i <= 24; i++){
            chartLabels.push(i);
        }

        if ($scope.bitcoinData.length > 24) {
            var j = $scope.bitcoinData.length - 24;
            for (j; j < $scope.bitcoinData.length; j++) {
                bidPrice.push($scope.bitcoinData[j].bid);
                askPrice.push($scope.bitcoinData[j].ask);
            }
        } else {
            for (var k=0; k < $scope.bitcoinData.length; k++) {
                bidPrice.push($scope.bitcoinData[k].bid);
                askPrice.push($scope.bitcoinData[k].ask);
            }
        }

        $scope.chart = {
            labels : chartLabels,
            datasets : [
                    {
                            fillColor : "rgba(39,124,242,0)",
                            strokeColor: "rgba(39,124,242,1)",
                            pointColor: "rgba(39,124,242,1)",
                            pointStrokeColor : "#fff",
                            data : bidPrice
                    },
                    {
                            fillColor : "rgba(255,0,251,0)",
                            strokeColor: "rgba(255,0,251,1)",
                            pointColor: "rgba(255,0,251,1)",
                            pointStrokeColor : "#fff",
                            data : askPrice
                    }
            ]
        };
    });
}]);

app.controller('DailyController', ['$scope', '$http', 
        function($scope, $http) {

    $http.get('/api/v1/daily').success(function(data) {
        $scope.bitcoinData = data.data;

        var chartLabels = [];
        var bidPrice = [];
        var askPrice = [];


        for (var i = 0; i < 30; i++){
            chartLabels.push(i);
        }

        if ($scope.bitcoinData.length > 30) {
            var j = $scope.bitcoinData.length - 30;
            for (j; j < $scope.bitcoinData.length; j++) {
                bidPrice.push($scope.bitcoinData[j].bid);
                askPrice.push($scope.bitcoinData[j].ask);
            }
        }

        $scope.chart = {
            labels : chartLabels,
            datasets : [
                    {
                            fillColor : "rgba(39,124,242,0)",
                            strokeColor: "rgba(39,124,242,1)",
                            pointColor: "rgba(39,124,242,1)",
                            pointStrokeColor : "#fff",
                            data : bidPrice
                    },
                    {
                            fillColor : "rgba(255,0,251,0)",
                            strokeColor: "rgba(255,0,251,1)",
                            pointColor: "rgba(255,0,251,1)",
                            pointStrokeColor : "#fff",
                            data : askPrice
                    }
            ]
        };
    });

}]);

angular.module('app.filters', []).filter('localtime', [function() {
        return function(input){
            var date = new Date(input);
            return String(date);
        };
}]);

