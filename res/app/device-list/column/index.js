module.exports = angular.module('stf.device-list.column', [
  require('gettext').name,
  require('angular-ui-grid').name
])
  .service('DeviceColumnService', require('./device-column-service'))
