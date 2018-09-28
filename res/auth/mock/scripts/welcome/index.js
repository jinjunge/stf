require('./welcome.css')
module.exports = angular.module('stf.welcome', [])
  .config(function($routeProvider) {
     $routeProvider
      .when('/auth/welcome/', {
	template: require('./welcome.pug')
        })
  })
 .controller('WelcomeCtrl', require('./welcome-controller'))
