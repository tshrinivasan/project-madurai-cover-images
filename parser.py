import csv

import codecs

with open('index-all.csv', 'rb') as f:
    reader = f.readlines()
    for row in reader:
        no = row.split('$')[0]
        book_name =  row.split('$')[1].decode('utf-8')
        author= row.split('$')[2].decode('utf-8')

        print author

	
        file_number = '%0*d' % (3, int(no) )

        file_name = file_number  + ".html"

        meta = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <style>
        h1{
        color:MidnightBlue  ;
        font-size:50px;
        text-align:center;
        }
         h2{
        color:DarkSlateGray    ;
        font-size:30px;
        text-align:center;
        }
        
         h3{
          font-family: "Times New Roman", Times, serif;
        color:DarkRed ;
        font-size:20px;
        text-align:center;
	position:absolute;
	left:100px;
	bottom: 0;
              }
        </style>
        </head>
	<body background ="grey.png">
        
        <br/>
        <h1 >
        """

        auth = """
        </h1>
        <br/><br/>
        <h2 >
        """
        
        publisher="""
        <br/><br/>
        <h3>
        http://projectmadurai.org</h3>
        """

        

        html = codecs.open(file_name, 'w', 'utf-8')        
        html.write(meta)
        html.write(book_name)
        html.write(auth)
        html.write(author)
        html.write(publisher)
        html.close()
