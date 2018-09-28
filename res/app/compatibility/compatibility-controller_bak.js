module.exports = function  CompatibilityCtrl(
	$scope
	,$http
	,$sce
        ,UserService
	,DeviceService
	,ControlService
	,SettingsService
        ,DeviceColumnService
        ,$interval
	,$window
	,$upload
) {
	$scope.url='http://172.27.82.2:8000/'+UserService.currentUser.name
	$scope.someUrl = $sce.trustAsResourceUrl($scope.url)
	$scope.userName = UserService.currentUser.name
	$scope.tracker = DeviceService.trackAll($scope)
	$scope.control = ControlService.create($scope.tracker.devices, '*ALL')
	$scope.columnDefinitions = DeviceColumnService

        var context = $scope;
	$scope.reloadData = reloadData;//(重要：需要与页面的事件进行绑定)
	function reloadData(page) {
		    context.params.pageNumber = page || 1;//将参数变为点击的page，默认为1
		    getPackageList(context.params);//请求后端分页接口(根据业务todo)
	}

	$scope.reloadRoute = function () {
		$window.location.reload();
	}
//	$scope.isActive1 = false
	$http.get('/reports')
	        .success(function (res) {
		var a=new Array()
		for(var i=0;i<res.reports.length;i++){
		  if (res.reports[i].user===UserService.currentUser.name){
		    a.push(res.reports[i])
		  }
		}
		$scope.reports=a
		})
	$scope.selectedName={text:""};
	$http.get('/apklist?user='+UserService.currentUser.name)
	            .success(function (res) {
                             $scope.names=res
			     $scope.apk_ip1={
			       ip:'172.27.82.2',
			       apk:res
			     }
			    console.log($scope.apk_ip1.apk)
			    //之后注释放开
//			     $http.get('http://172.27.82.3:7100/apklist?user='+UserService.currentUser.name)
//			       .success(function(res1){
//			          $scope.names=$scope.names.concat(res1)
//				  $scope.apk_ip2={
//				    ip:'172.27.82.3',
//				    apk:res1
//				  }
//			       })
			                })
       //apk不对应手机隐藏
       $scope.myFun1=function(){
	       Array.prototype.in_array = function (element) {
		 for (var i = 0; i < this.length; i++) {
		   if (this[i] == element) {
			return true;
		        console.log('11111')
		   }
		}
		return false;
		console.log('222')
	}
	var cbList = document.getElementsByClassName('monkey')
	var len = cbList.length
	if($scope.apk_ip1.apk.in_array($scope.selectedName.text)){
	  for (var i = 0; i < len; i++) {
	    var cb = cbList[i]
	    if(cb.getAttribute('ip')!=$scope.apk_ip1.ip){
	      cb.parentNode.parentNode.classList.add("dn")
	      console.log('add')
	    }
	    console.log(cb.getAttribute('ip')+'--------'+$scope.apk_ip1.ip)
	    if(cb.getAttribute('ip')==$scope.apk_ip1.ip){
	      console.log('remove')
	      cb.parentNode.parentNode.classList.remove("dn")
	    }
	  }
	}
	if($scope.apk_ip2.apk.in_array($scope.selectedName.text)){
	  for (var i = 0; i < len; i++) {
	     var cb = cbList[i]
             if(cb.getAttribute('ip')!=$scope.apk_ip2.ip){
	       cb.parentNode.parentNode.classList.add("dn")
	       console.log('add')
	     }
	  console.log(cb.getAttribute('ip')+'--------'+$scope.apk_ip1.ip)
	  if(cb.getAttribute('ip')==$scope.apk_ip2.ip){
	    console.log('remove')
	    cb.parentNode.parentNode.classList.remove("dn")
	   }
	 }
	} 
	
       }

        $scope.runTest = function(){
	  var loading = document.getElementsByClassName('sk-fading-circle')
          for (var q = 0; q < loading.length; q++) {
	    loading[q].classList.remove("dn")
	  }
	  var cbList = document.getElementsByClassName('monkey')
	  var len = cbList.length
	  function reqDate(serialAPK,ip,flag,user) {
	   this.serialAPK = serialAPK
	   this.ip=ip
           this.flag=flag
	   this.user=user
	  }
	  var jsArry = []
	  var ipArry = []
	  if($scope.selectedName.text!=''){
	  var apk=$scope.selectedName.text
	  console.log('apk---'+apk)
          var checkFlag=false
	  var usingFlag=false
	  for (var i = 0; i < len; i++) {		  
	    var cb = cbList[i]
            if(cb.checked){
	      cb.parentNode.parentNode.classList.add("dn")
	      var serial = cb.getAttribute('serial')
	      var ip = cb.getAttribute('ip')
//暂时修改内容		    
	      if (ip==='172.27.82.2') {
	        apk1='/root/WebstormProjects/stf/uploads/'+$scope.userName+'/'+apk
	      }
	      if (ip==='172.27.82.3') {
                apk1='/opt/project/untitled/bin/uploads/'+$scope.userName+'/'+apk   
	      }
		    
	      var serialapk = {serial: apk1}
	      serialapk[serial] = serialapk['serial']
	      delete serialapk['serial']
	      jsArry.push(serialapk)
	      ipArry.push(ip)
	      checkFlag=true
//	      var state=device.APK_status
//	      if(state=='install_start'||state=='runAir_start'||state=='monkey_start'){
//	        usingFlag=true
//	      }
	    }
	  }
	  if(!usingFlag){
          if(checkFlag==true){
	  var req = new reqDate(jsArry,ipArry,true,UserService.currentUser.name)
	  console.log(req)
	  var r=confirm("确认运行吗？")
	  if (r==true){
	    document.getElementById('run').innerHTML='运行中...'
	    $http({
	       method: "POST",
	       url: "http://172.27.82.2:8082/",
	       data: JSON.stringify(req),
	    }).success(function (res) {
	      console.log(res)
//暂时注释	      if(res.message==='success'){
	        $scope.timer=$interval(function(){
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
					      if(device.APK_status==='monkey_end'){
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
//暂时注释	      }
	    }).error(function(data, status, headers, config) {
		 //alert('服务器错误')
	     })
	  }else{
	    alert('已取消运行')
	  }
	  }else{
	    alert('ERROR: [未选中手机]')
	  }
	  }else{
	    alert('ERROR:[所选手机正在使用中，请刷新重试]')
	  }
	  }else{
	    alert('ERROR: [请先选择apk]')
	  }
	}
       
        $scope.fileUpload=function($files) {
	cbList = document.getElementsByClassName('serverIp')
	var len = cbList.length
	var arrIp=[]
	for (var i = 0; i < len; i++) {
		var cb = cbList[i]
		if(cb.checked){
			arrIp.push(cb.getAttribute('ip'))
		}
	}
	if(arrIp.length!=0){
	var myFile = $files
	  if(myFile.length!=0){
          for(var j=0;j<arrIp.length;j++){
	    $upload.upload({
	      url: 'http://'+arrIp[j]+':7100/file-upload'
		    , method: 'POST'
		    , data: {
			    'usrId': $scope.userName
			    ,'ip': arrIp[j]
		    }
		    , file: $files
	    }).progress(function(evt) {
	      $scope.isShow=true
	      var progress=parseInt(100.0 * evt.loaded / evt.total)
	      document.getElementById('progressBar').setAttribute('style', 'width:'+progress+'%')
	      document.getElementById('progressBar').innerHTML=progress + '%';
	      }).success(function(data, status, headers, config) {
	        alert(data.result)
                $scope.reloadRoute()
		return
	      }).error(function(data, status, headers, config) {
		alert('上传失败')
		console.log(data)
		return
	      })
	  }  
	}
	}else{
	  alert('请选中一个ip')
	}
		
	}
      $scope.$on('ngRepeatFinished', function(ngRepeatFinishedEvent) {
	function goPage(pno,psize){
		    var itable = document.getElementById("mytable");
		    var num = itable.rows.length;//表格所有行数(所有记录数)
		    console.log(num);
		    var totalPage = 0;//总页数
		    var pageSize = psize;//每页显示行数
		    //总共分几页 
		    if(num/pageSize > parseInt(num/pageSize)){   
			    totalPage=parseInt(num/pageSize)+1;   
		    }else{   
			    totalPage=parseInt(num/pageSize);   
		    }   
		var currentPage = pno;//当前页数
		var startRow = (currentPage - 1) * pageSize+1;//开始显示的行  31 
		var endRow = currentPage * pageSize;//结束显示的行   40
		endRow = (endRow > num)? num : endRow;   // 40
		console.log(endRow);
		//遍历显示数据实现分页
		for(var i=1;i<(num+1);i++){    
			var irow = itable.rows[i-1];
			if(i>=startRow && i<=endRow){
				irow.style.display = "table-row";    
			}else{
				irow.style.display = "none";
			}
		}
		var pageEnd = document.getElementById("pageEnd");
		var tempStr = "共"+(num-1)+"条记录 分"+totalPage+"页 当前第"+currentPage+"页";
		if(currentPage>1){
			tempStr += "<a href=\"#\" onClick=\"goPage("+(1)+","+psize+")\">首页</a>";
			tempStr += "<a href=\"#\" onClick=\"goPage("+(currentPage-1)+","+psize+")\"><上一页</a>"
		}else{
			tempStr += "首页";
			tempStr += "<上一页"; 
		}
		if(currentPage<totalPage){
			tempStr += "<a href=\"#\" onClick=\"goPage("+(currentPage+1)+","+psize+")\">下一页></a>";
			tempStr += "<a href=\"#\" onClick=\"goPage("+(totalPage)+","+psize+")\">尾页</a>";
		}else{                                                                                                                                                                                                                                 tempStr += "下一页>";
			tempStr += "尾页";    
		}                                                                                                                                                                                                                                                 document.getElementById("barcon").innerHTML = tempStr;                                                                                                                                         
	}
      })
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
/*	function createRow(test) {
	  var id = test.id
	  var tr = document.createElement('tr')
	  var td
	  tr.id = id
          for (var i = 0, l = columns.length; i < l; ++i) {
	  td = $scope.testCell[columns[i].name].build()
          $scope.testCell[columns[i].name].update(td, test)
	  tr.appendChild(td)
	  }
		  return tr
	}

	function updateRow(test)
	{	
		var tr = tbody.children[test.id]
		  if (tr) {
		    for (var i = 0, l = columns.length; i < l; ++i) {
		      $scope.testCell[columns[i].name].update(tr.cells[i], test) 
		    }
		    return tr
		 }
}
*/
}
