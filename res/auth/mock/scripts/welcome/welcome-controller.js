module.exports = function WelcomeCtrl($scope, $http) {

  $scope.error = null
  $scope.isActive1=true
  $scope.isActive2=false
  $scope.isActive3=false

  $scope.mouseenter1=function() {
    $scope.isActive1=true
    $scope.isActive2=false
    $scope.isActive3=false
  }
  $scope.mouseenter2=function() {
    $scope.isActive1=false
    $scope.isActive2=true
    $scope.isActive3=false
  }
  $scope.mouseenter3=function() {
    $scope.isActive1=false
    $scope.isActive2=false
    $scope.isActive3=true
}
/*  $scope.submit = function() {
    var data = {
      name: $scope.signin.username.$modelValue
      , email: $scope.signin.email.$modelValue
    }
    $scope.invalid = false
    $http.post('/auth/api/v1/mock', data)
      .success(function(response) {
        $scope.error = null
        location.replace(response.redirect)
      })
      .error(function(response) {
        switch (response.error) {
          case 'ValidationError':
            $scope.error = {
              $invalid: true
            }
            break
          case 'InvalidCredentialsError':
            $scope.error = {
              $incorrect: true
            }
            break
          default:
            $scope.error = {
              $server: true
            }
            break
        }
      })
  }*/
}
