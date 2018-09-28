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
, $interval
, UserService
, $window
) {
  $scope.tracker = DeviceService.trackAll($scope)
  $scope.control = ControlService.create($scope.tracker.devices, '*ALL')
  $scope.currentUser = UserService.currentUser
  $scope.columnDefinitions = DeviceColumnService
  $scope.reloadRoute = function () {
	      $window.location.reload();
  }

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
      name: 'scriptstatus'
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
      name: 'scripts'
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
	//var flag=true
	var checkedFlag=false
	var scriptDir=[]
	var timestamp=new Date().getTime()

        devices.forEach(function (device) {
          for (var i = 0; i < len; i++) {
            var cb = cbList[i]
            var serial = cb.getAttribute('serial')
          //  var apkdir = cb.getAttribute('apkdir')
            if (cb.checked && serial === device.serial) {
	      checkedFlag=true
              var apk = device.notes
	      var script=device.scripts
              var serialapk = {serial: apk}
	      serialapk[serial] = serialapk['serial']
	      delete serialapk['serial']
              jsArry.push(serialapk)
	      scriptDir.push(script)
	  //    if(flag&&script.length!==0){
	//	scriptDir=script
	//	flag=false
          //    }
            }
	  }
        })
	if(checkedFlag){
        var req = new reqDate(jsArry, scriptDir, '/opt/logs', '/opt/reports/'+$scope.currentUser.name)     //+ $scope.currentUser.name+'/'+timestamp)
        console.log(req)
        var r=confirm("确认运行吗？")
	if (r==true){
        $http({
          method: "POST",
          url: "http://192.168.2.24:8082/",
          data: JSON.stringify(req),
        }).success(function (res) {
          console.log(res)
          if(res==='success'){
            alert('运行完成')
          }
        })
	}else{
          alert('已取消运行')
	}
        }else{
           alert('请选中至少一个手机')
	}

      })
  }

  $scope.fileUpload=function($files) {
    var cbList = document.getElementsByClassName('airCheckBox')
    var len = cbList.length
    var myFile = $files
    console.log('-------'+myFile.length)
   if(myFile.length!=0){
    $upload.upload({
      url: '/file-upload'
      , method: 'POST'
      , data: {
        'usrId': $scope.currentUser.name
      }
      , file: $files
    }).progress(function(evt) {//上传进度
      var progress=parseInt(100.0 * evt.loaded / evt.total)
      document.getElementById('progressBar').setAttribute('style', 'width:'+progress+'%')
      document.getElementById('progressBar').innerHTML=progress + '%';
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
      return
    }).error(function(data, status, headers, config) {
      //失败处理函数
      alert('上传失败')
      console.log(data)
      return
    })
   }
  }

  $scope.cInput=function(){
    document.getElementById('upload').click()
  }
  $scope.folderUpload=function($files) {
    var cbList = document.getElementsByClassName('airCheckBox')
    var len = cbList.length
    var files=$files
    var infoArr=[]
    var info=new Object()
  /*  files.forEach(function(val){
	    info.size=val.size
	    info.webkitRelativePath=val.webkitRelativePath
	    console.log(info)
	    infoArr.push(info)
	    console.log(infoArr)
    }) */
    for (var i=0;i<files.length;i++){
      info.size=files[i].size
      info.webkitRelativePath=files[i].webkitRelativePath
      info.name=files[i].name
      console.log(info)
      infoArr.push(info)
      console.log(infoArr)
      info={}
    }
    var arr=files[0].webkitRelativePath.split('/')
    var folderPath=arr[0]
    $upload.upload({
      url: '/folder-upload'
      , method: 'POST'
      , file: files
      , data: infoArr
    }).progress(function (evt) {//上传进度
      console.log('percent: ' + parseInt(100.0 * evt.loaded / evt.total));
    }).success(function (data, status, headers, config) {
      // 文件上传成功处理函数
      alert(data.result)
      for (var i = 0; i < len; i++) {
	  var cb = cbList[i]
	  if (cb.checked){
	    var serial = cb.getAttribute('serial')
	    DeviceService.updateScript(serial, data.script+folderPath)
	  }
      }
      console.log(data)
    }).error(function (data, status, headers, config) {
      //失败处理函数
      alert('上传失败')
      console.log('上传失败')
    })
  }

  $scope.installAPK = function () {
    var cbList = document.getElementsByClassName('airCheckBox')

    function reqDate(serialAPK) {
      this.serialAPK = serialAPK
    }

    var jsArry = []
    $http.get('/api/v1/devices')
      .success(function (res) {
        var devices = res.devices
        var len = cbList.length
        //var flag=true
        var checkedFlag=false
        var scriptDir=[]
        var timestamp=new Date().getTime()

        devices.forEach(function (device) {
          for (var i = 0; i < len; i++) {
            var cb = cbList[i]
            var serial = cb.getAttribute('serial')
            if (cb.checked && serial === device.serial) {
              checkedFlag=true
              var apk = device.notes
              var serialapk = {serial: apk}
              serialapk[serial] = serialapk['serial']
              delete serialapk['serial']
              jsArry.push(serialapk)
            }
          }
        })
        if(checkedFlag){
          var req = new reqDate(jsArry)     //+ $scope.currentUser.name+'/'+timestamp)
          console.log(req)
          var r=confirm("确认运行吗？")
          if (r==true){
            $http({
              method: "POST",
              url: "http://192.168.2.24:8082/",
              data: JSON.stringify(req),
            }).success(function (res) {
              console.log(res)
              if(res==='success'){
                alert('运行完成')
              }
            })
          }else{
            alert('已取消运行')
          }
        }else{
          alert('请选中至少一个手机')
        }

      })
  }
  $scope.uninstallAPK = function () {
    var cbList = document.getElementsByClassName('airCheckBox')

    function reqDate(serialAPK,flag) {
      this.serialAPK = serialAPK
      this.flag=flag
    }

    var jsArry = []
    $http.get('/api/v1/devices')
      .success(function (res) {
        var devices = res.devices
        var len = cbList.length
        var checkedFlag=false
        var scriptDir=[]
        var timestamp=new Date().getTime()

        devices.forEach(function (device) {
          for (var i = 0; i < len; i++) {
            var cb = cbList[i]
            var serial = cb.getAttribute('serial')
            if (cb.checked && serial === device.serial) {
              checkedFlag=true
              var apk = device.notes
              var serialapk = {serial: apk}
              serialapk[serial] = serialapk['serial']
              delete serialapk['serial']
              jsArry.push(serialapk)
            }
          }
        })
        if(checkedFlag){
          var req = new reqDate(jsArry,true)     //+ $scope.currentUser.name+'/'+timestamp)
          console.log(req)
          var r=confirm("确认运行吗？")
          if (r==true){
            $http({
              method: "POST",
              url: "http://192.168.2.24:8082/",
              data: JSON.stringify(req),
            }).success(function (res) {
              console.log(res)
              if(res.message==='success'){
                alert('开始安装')
                $scope.timer=$interval(function(){
		  var len = cbList.length
		  var arf =true
		$http.get('/api/v1/devices')
		  .success(function (res) {
	            var devices = res.devices
		try{	  
		    devices.forEach(function (device) {
		      for (var i = 0; i < len; i++) {
			var cb = cbList[i]
			var serial = cb.getAttribute('serial')
			if (cb.checked && serial === device.serial) {
			  if(device.APK_status==='install_fail'||device.APK_status==='install_success'){
		            arf=true
			    console.log(device.serial)
			  }else{
		            console.log(device.serial+'---------')
			    arf=false
		            break
			  }
			   console.log(arf)
			}
		      }
			if(arf==false){
				console.log('进来了---------')
			    foreach.break=new Error("StopIteration")
			}    
		    })
		  }catch(e){
		      console.log(e.message);
		     if(e.message==="foreach is not defined") {
			console.log("跳出来了?");//
		       console.log('------'+arf)
			     if(arf==true){
			  console.log('lalala')
	                  $interval.cancel($scope.timer)
		          alert('运行完成，请查看结果')
			  $scope.reloadRoute()
			  }
		     } else throw e;
		  }
		     if(arf==true){
		        console.log('lalala')
			$interval.cancel($scope.timer)
		        alert('运行完成，请查看结果')
			$scope.reloadRoute()
	             }
		  })

		console.log('hello world')
		},500)   //间隔0.5秒定时执行

              }
            })
          }else{
            alert('已取消安装')
          }
        }else{
          alert('请选中至少一个手机')
        }

      })
  }
}
