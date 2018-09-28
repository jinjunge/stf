module.exports = function MenuCtrl($scope, $rootScope, SettingsService,$window,
  $location) {

  SettingsService.bind($scope, {
    target: 'lastUsedDevice'
  })

  SettingsService.bind($rootScope, {
    target: 'platform',
    defaultValue: 'native'
  })

  $scope.$on('$routeChangeSuccess', function() {
    $scope.isControlRoute = $location.path().search('/control') !== -1
  })
  
  $scope.logout=function(){
    $window.location.href='/auth/mock/'
    $window.close()
  }

}
