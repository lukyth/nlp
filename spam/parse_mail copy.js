// ลง mail parser ก่อน npm install mailparser
// ตัวอย่างการใช้ cat ~/trec07p/data/inmail.1 | node parse_mail.js > inmail.1.json
var MailParser = require("mailparser").MailParser;
var mailparser = new MailParser();
var fs = require('fs');

var email = fs.readFileSync('/dev/stdin').toString();

mailparser.on("end", function(mail_object){
  console.log(JSON.stringify(mail_object)); 
});

mailparser.write(email);
mailparser.end();