require('./compatibility-details.css')

module.exports = angular.module('stf.compatibility.details', [
  require('stf/device').name,
  require('stf/user/group').name,
  require('stf/common-ui').name,
  require('stf/admin-mode').name
])
  .directive('compatibilityDetails', require('./compatibility-details-directive'))
