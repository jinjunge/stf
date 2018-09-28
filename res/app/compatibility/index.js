
module.exports = angular.module('compatibility', [
    require('stf/user/group').name,
    require('./choice').name,
    require('stf/device').name,
    require('ui-bootstrap').name,
    require('stf/common-ui').name,
    require('./details').name
])
  .config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/compatibility', {
        template: require('./compatibility.pug'),
        controller: 'CompatibilityCtrl'
      })
  }])
  .run(function(editableOptions) {
    // bootstrap3 theme for xeditables
    editableOptions.theme = 'bs3'
  })
  .controller('CompatibilityCtrl', require('./compatibility-controller'))
