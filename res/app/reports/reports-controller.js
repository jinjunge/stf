module.exports = function ReportsCtrl(
	$scope
	,$sce
        ,UserService
) {
    $scope.url='http://172.27.82.2:8081/SummaryReport?user='+UserService.currentUser.name
    $scope.someUrl = $sce.trustAsResourceUrl($scope.url)
}
