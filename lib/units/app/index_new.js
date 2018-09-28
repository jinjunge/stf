var http = require('http')
var url = require('url')
var fs = require('fs')
var formidable = require('formidable')

var multer = require('multer')
var express = require('express')
var validator = require('express-validator')
var cookieSession = require('cookie-session')
var bodyParser = require('body-parser')
var serveFavicon = require('serve-favicon')
var serveStatic = require('serve-static')
var csrf = require('csurf')
var compression = require('compression')

var logger = require('../../util/logger')
var pathutil = require('../../util/pathutil')
var upload = multer({dest: 'upload/'}).any()

var auth = require('./middleware/auth')
var deviceIconMiddleware = require('./middleware/device-icons')
var browserIconMiddleware = require('./middleware/browser-icons')
var appstoreIconMiddleware = require('./middleware/appstore-icons')

var markdownServe = require('markdown-serve')

module.exports = function(options) {
  var log = logger.createLogger('app')
  var app = express()
  var server = http.createServer(app)

  app.use('/static/wiki', markdownServe.middleware({
    rootDirectory: pathutil.root('node_modules/stf-wiki')
  , view: 'docs'
  }))

  app.set('view engine', 'pug')
  app.set('views', pathutil.resource('app/views'))
  app.set('strict routing', true)
  app.set('case sensitive routing', true)
  app.set('trust proxy', true)

  if (fs.existsSync(pathutil.resource('build'))) {
    log.info('Using pre-built resources')
    app.use(compression())
    app.use('/static/app/build/entry',
      serveStatic(pathutil.resource('build/entry')))
    app.use('/static/app/build', serveStatic(pathutil.resource('build'), {
      maxAge: '10d'
    }))
  }
  else {
    log.info('Using webpack')
    // Keep webpack-related requires here, as our prebuilt package won't
    // have them at all.
    var webpackServerConfig = require('./../../../webpack.config').webpackServer
    app.use('/static/app/build',
      require('./middleware/webpack')(webpackServerConfig))
  }

  app.use('/static/bower_components',
    serveStatic(pathutil.resource('bower_components')))
  app.use('/static/app/data', serveStatic(pathutil.resource('data')))
  app.use('/static/app/status', serveStatic(pathutil.resource('common/status')))
  app.use('/static/app/browsers', browserIconMiddleware())
  app.use('/static/app/appstores', appstoreIconMiddleware())
  app.use('/static/app/devices', deviceIconMiddleware())
  app.use('/static/app', serveStatic(pathutil.resource('app')))

  app.use('/static/logo',
    serveStatic(pathutil.resource('common/logo')))
  app.use(serveFavicon(pathutil.resource(
    'common/logo/exports/STF-128.png')))

  app.use(cookieSession({
    name: options.ssid
  , keys: [options.secret]
  }))

  app.use(auth({
    secret: options.secret
  , authUrl: options.authUrl
  }))

  // This needs to be before the csrf() middleware or we'll get nasty
  // errors in the logs. The dummy endpoint is a hack used to enable
  // autocomplete on some text fields.
  app.all('/app/api/v1/dummy', function(req, res) {
    res.send('OK')
  })

  app.use(bodyParser.json())
  app.use(csrf())
  app.use(validator())

  app.use(function(req, res, next) {
    res.cookie('XSRF-TOKEN', req.csrfToken())
    next()
  })

  app.get('/', function(req, res) {
    res.render('index')
  })

  app.get('/app/api/v1/state.js', function(req, res) {
    var state = {
      config: {
        websocketUrl: (function() {
          var wsUrl = url.parse(options.websocketUrl, true)
          wsUrl.query.uip = req.ip
          return url.format(wsUrl)
        })()
      }
    , user: req.user
    }

    if (options.userProfileUrl) {
      state.config.userProfileUrl = (function() {
        return options.userProfileUrl
      })()
    }

    res.type('application/javascript')
    res.send('var GLOBAL_APPSTATE = ' + JSON.stringify(state))
  })

  app.post('/file-upload', function(req, res) {
    upload(req, res, function(err) {
      //添加错误处理
      if (err) {
        console.log(err)
        return
      }
      if(req.files.length == 0) {
        return
      }
      req.file = req.files[0]
      var tmpPath = req.file.path
      console.log(tmpPath)
      var usrId = req.body.usrId

      var targetPath = 'uploads/' + usrId + '/' + req.file.originalname
      var fullTargetPath = process.cwd() + '/uploads/' + usrId + '/' + req.file.originalname
      /** A better way to copy the uploaded file. **/
      console.log(targetPath)

      if (!fs.existsSync('uploads/' + usrId + '/')) {
        fs.mkdirSync('uploads/' + usrId + '/')
      }

      var src = fs.createReadStream(tmpPath)
      var dest = fs.createWriteStream(targetPath)
      src.pipe(dest)
      src.on('end', function() {
        var response = {
          'result':'success',
          'note':fullTargetPath
        }
        res.end(JSON.stringify(response))
        return
      })
      src.on('error', function(err) {

        res.end()
        console.log(err)
        return
      })

    })

/*    app.post('/folder-upload', function(req, res) {
      upload(req, res, function(err) {
        //添加错误处理
        if (err) {
          console.log(err)
          return
        }
        var form = new formidable.IncomingForm()
        form.keepExtensions = true
        form.encoding = 'utf-8'
        form.uploadDir = './'
        form.parse(req, function (err, fields, files) {
          res.writeHead(200, {'Content-type': 'text/plain'})
          //上传文件的名称
          var filename = files.upload.name
          var path = files.upload.path
          //更改名称
          fs.rename(path, form.uploadDir + filename);
          res.end('success')

        })
      })
    })
*/

  server.listen(options.port)
  log.info('Listening on port %d', options.port)
}
