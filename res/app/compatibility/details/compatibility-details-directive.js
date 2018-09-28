//var patchArray = require('./../util/patch-array')

module.exports = function compabilityDetailsDirective(
  $filter
, $compile
, $rootScope
, gettext
, DeviceColumnService
, GroupService
, DeviceService
, LightboxImageService
, StandaloneService
, $timeout	
) {
  return {
    restrict: 'A'
  , link: function(scope, element,attr) {
    if (scope.$last === true) {
      $timeout(function () {
	 scope.$emit('ngRepeatFinished');
        });
      }
  }
}
}


    


