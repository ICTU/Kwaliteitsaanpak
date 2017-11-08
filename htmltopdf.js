var fs = require('fs')
var conversion = require("phantom-html-to-pdf")();
var inputfilename = process.argv.slice(2)[0];
var outputfilename = inputfilename.replace('.html','.pdf');

var file = fs.readFile(inputfilename, 'utf8', function (err,data) {
    if (err) {
      return console.log(err);
    }

    data = data.replace('</head>','<base href="'+__dirname+'/" /><meta http-equiv="content-type" content="text/html; charset=UTF-8"></head>');


    conversion({ 
        html: data,
        header: '',
        footer: '<div style="text-align:right;font-family:Arial;font-size:10px;">{#pageNum}/{#numPages}</div>',
        printDelay: 0,
        waitForJS: false,
        allowLocalFilesAccess: true,
        settings: {
            javascriptEnabled : false,
            resourceTimeout: 1000
        },
        viewportSize: {
            width: 1000,
            height: 600
        },
        format: {
            quality: 100,
        }
     }, function(err, pdf) {
        var output = fs.createWriteStream(outputfilename)
        console.log(pdf.logs);
        console.log(pdf.numberOfPages);
          // since pdf.stream is a node.js stream you can use it
          // to save the pdf to a file (like in this example) or to
          // respond an http request.
        pdf.stream.pipe(output);
        conversion.kill();
      });
  });