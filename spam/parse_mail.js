// npm install mailparser
// node parse_mail.js
var MailParser = require('mailparser').MailParser
var fs = require('fs')
var dirname = 'sample/'
var resultDir = 'result/'

if (!fs.existsSync(resultDir)){
  fs.mkdirSync(resultDir)
}

var filenames = fs.readdirSync(dirname)

filenames.forEach(function (filename) {
  var mailparser = new MailParser()
  mailparser.filename = filename
  mailparser.on('end', function(mail_object){
    fs.writeFile(resultDir + mailparser.filename + '.json', JSON.stringify(mail_object))
  })
  mailparser.write(fs.readFileSync(dirname + filename).toString())
  mailparser.end()
})
