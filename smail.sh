#!/bin/bash

TO="oleksiy.yevstratov@lifecell.com.ua,petr.fedyankin@lifecell.com.ua,vladislav.samborskiy@lifecell.com.ua,ext_huawei_erhan.ay@lifecell.com.ua,vitaliy.danevych@lifecell.com.ua,anastasia.gerliand@lifecell.com.ua,taras.chagayna@lifecell.com.ua"

#CC="vitaliy.danevych@life.com.ua"
FROM="ericsson-oss-rc2@lifecell.com.ua"
SUBJECT="Ericcson RBS data (licenses, e_tilt) report"
BODY="Pls, find attached archive file. There is UNIX end of line at the txt files into it. Windows\DOS uses carriage return and line feed ("\\r\\n") as a line ending, which Unix uses just line feed ("\\n")"
(echo 'From: '$FROM;echo 'To:'$TO;echo 'Cc:'$CC;echo 'Subject: '$SUBJECT;  echo $BODY ;uuencode $1 $1)| /usr/sbin/sendmail -f vitaliy.danevych@lifecell.com.ua -t
exit

