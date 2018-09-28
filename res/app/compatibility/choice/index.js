require('./compatibility-choice.css')

module.exports = angular.module('stf.compatibility.choice', [
  require('gettext').name,
  require('stf/user/group').name,
  require('stf/common-ui').name,
  require('../../device-list/column').name,
  require('../../device-list/empty').name,
  require('stf/standalone').name,
  require('ui-bootstrap').name
])
  .directive('compatibilityChoice', require('./compatibility-choice-directive'))
