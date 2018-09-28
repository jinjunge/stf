var QueryParser = require('./util/query-parser')

module.exports = function DeviceListCtrl(
  $scope
, DeviceService
, DeviceColumnService
, GroupService
, ControlService
, SettingsService
, $location
, $http
, $upload
, UserService
) {
  $scope.tracker = DeviceService.trackAll($scope)
  $scope.control = ControlService.create($scope.tracker.devices, '*ALL')
  $scope.currentUser = UserService.currentUser
  $scope.columnDefinitions = DeviceColumnService

  var defaultColumns = [
    {
      name: 'check'
      , selected: true
    }
    , {
      name: 'state'
      , selected: true
    }
    , {
      name: 'model'
      , selected: true
    }
    , {
      name: 'name'
      , selected: true
    }
    , {
      name: 'serial'
      , selected: false
    }
    , {
      name: 'operator'
      , selected: true
    }
    , {
      name: 'releasedAt'
      , selected: true
    }
    , {
      name: 'version'
      , selected: true
    }
    , {
      name: 'network'
      , selected: false
    }
    , {
      name: 'display'
      , selected: false
    }
    , {
      name: 'manufacturer'
      , selected: false
    }
    , {
      name: 'sdk'
      , selected: false
    }
    , {
      name: 'abi'
      , selected: false
    }
    , {
      name: 'cpuPlatform'
      , selected: false
    }
    , {
      name: 'openGLESVersion'
      , selected: false
    }
    , {
      name: 'browser'
      , selected: false
    }
    , {
      name: 'phone'
      , selected: false
    }
    , {
      name: 'imei'
      , selected: false
    }
    , {
      name: 'imsi'
      , selected: false
    }
    , {
      name: 'iccid'
      , selected: false
    }
    , {
      name: 'batteryHealth'
      , selected: false
    }
    , {
      name: 'batterySource'
      , selected: false
    }
    , {
      name: 'batteryStatus'
      , selected: false
    }
    , {
      name: 'batteryLevel'
      , selected: false
    }
    , {
      name: 'batteryTemp'
      , selected: false
    }
    , {
      name: 'provider'
      , selected: true
    }
    , {
      name: 'notes'
      , selected: true
    }
    , {
      name: 'owner'
      , selected: true
    }
  ]

  $scope.columns = defaultColumns

  SettingsService.bind($scope, {
    target: 'columns'
    , source: 'deviceListColumns'
  })

  var defaultSort = {
    fixed: [
      {
        name: 'state'
        , order: 'asc'
      }
    ]
    , user: [
      {
        name: 'name'
        , order: 'asc'
      }
    ]
  }

  $scope.sort = defaultSort

  SettingsService.bind($scope, {
    target: 'sort'
    , source: 'deviceListSort'
  })

  $scope.filter = []

  $scope.activeTabs = {
    icons: true
    , details: false
  }

  SettingsService.bind($scope, {
    target: 'activeTabs'
    , source: 'deviceListActiveTabs'
  })

  $scope.toggle = function (device) {
    if (device.using) {
      $scope.kick(device)
    } else {
      $location.path('/control/' + device.serial)
    }
  }

  $scope.invite = function (device) {
    return GroupService.invite(device).then(function () {
      $scope.$digest()
    })
  }

  $scope.applyFilter = function (query) {
    $scope.filter = QueryParser.parse(query)
  }

  $scope.search = {
    deviceFilter: '',
    focusElement: false
  }

  $scope.focusSearch = function () {
    if (!$scope.basicMode) {
      $scope.search.focusElement = true
    }
  }

  $scope.reset = function () {
    $scope.search.deviceFilter = ''
    $scope.filter = []
    $scope.sort = defaultSort
    $scope.columns = defaultColumns
  }

  $scope.runAir = function () {
    var cbList = document.getElementsByClassName('airCheckBox')

    function reqDate(serialAPK, scriptDir, logDir, reportDir) {
      this.serialAPK = serialAPK
      this.scriptDir = scriptDir
      this.logDir = logDir
      this.reportDir = reportDir
    }

    var jsArry = []
    $http.get('/api/v1/devices')
      .success(function (res) {
        var devices = res.devices
        var len = cbList.length

        devices.forEach(function (device) {
          for (var i = 0; i < len; i++) {
            var cb = cbList[i]
            var serial = cb.getAttribute('serial')
          //  var apkdir = cb.getAttribute('apkdir')
            if (cb.checked && serial === device.serial) {
              var apk = device.notes
              var serialapk = {serial: apk}
              jsArry.push(serialapk)
            }
          }
        })
        var req = new reqDate(jsArry, '/opt/1.air', '/opt/1.log', '/opt/test')
        console.log(req)
        $http({
          method: "POST",
          url: "http://192.168.2.109:8080/",
          data: JSON.stringify(req),
        }).success(function (res) {
          console.log(res)
          if(res==='success'){
            alert('运行完成')
          }
        })


      })
  }

  $scope.fileUpload=function($files) {
    var cbList = document.getElementsByClassName('airCheckBox')
    var len = cbList.length
    $upload.upload({
      url: '/file-upload'
      , method: 'POST'
      , data: {
        'usrId': $scope.currentUser.name
      }
      , file: $files
    }).progress(function(evt) {//上传进度
      console.log('percent: ' + parseInt(100.0 * evt.loaded / evt.total));
    }).success(function(data, status, headers, config) {
      // 文件上传成功处理函数
      alert(data.result)
      for (var i = 0; i < len; i++) {
          var cb = cbList[i]
          if (cb.checked){
            var serial = cb.getAttribute('serial')
            DeviceService.updateNote(serial, data.note)
          }
      }
      console.log(data)
    }).error(function(data, status, headers, config) {
      //失败处理函数
      alert('上传失败')
      console.log('上传失败')
    })
  }
 
  $scope.cInput=function(){
    document.getElementById('upload').click()
  }
}
