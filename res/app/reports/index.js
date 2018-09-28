
module.exports = angular.module('reports', [
    require('stf/user/group').name
])
  .config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/reports', {
        template: require('./reports.pug'),
        controller: 'ReportsCtrl'
      })
  }])
  .run(function(editableOptions) {
    // bootstrap3 theme for xeditables
    editableOptions.theme = 'bs3'
  })
  .controller('ReportsCtrl', require('./reports-controller'))
