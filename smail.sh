#!/bin/bash

TO="olyeaov@lifecell.com.ua,penn@lifecell.com.ua,vladskiy@lifecell.com.ua,ext_an.ay@lifecell.com.ua,vitach@lifecell.com.ua,anaand@lifecell.com.ua,taryna@lifecell.com.ua"

#CC="vitach@life.com.ua"
FROM="ericsson-o2@lifecell.com.ua"
SUBJECT="Ericcson RBS data (licenses, e_tilt) report"
BODY="Pls, find attached archive file. There is UNIX end of line at the txt files into it. Windows\DOS uses carriage return and line feed ("\\r\\n") as a line ending, which Unix uses just line feed ("\\n")"
(echo 'From: '$FROM;echo 'To:'$TO;echo 'Cc:'$CC;echo 'Subject: '$SUBJECT;  echo $BODY ;uuencode $1 $1)| /usr/sbin/sendmail -f vitch@lifecell.com.ua -t
exit

