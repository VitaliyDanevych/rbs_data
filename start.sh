#!/bin/sh

echo "start!"
wdir=/home/fmuser2/scripts/rbs_data

echo "removing old files"
cd ${wdir}/temp
rm -rf *
cd ${wdir}/log
rm -rf *
cd ${wdir}/response
rm -rf *
cd ${wdir}
rm *.tar.gz

echo "removing old database"
rm ${wdir}/ipdatabase.txt
rm ${wdir}/list_rbs.txt

echo "The script has been started to work at" `date` > ${wdir}/response/script_time.log
echo "getting new databases..."
/opt/ericsson/ddc/util/bin/listme | grep RBS_NODE_MODEL | sed -e 's/[@=,]/ /g' | grep KIER  | awk '{print $6 "   " $7 "   "	"rbs"}' | sort| uniq > ${wdir}/ipdatabase.txt
#for test
#tail -25 ${wdir}/ipdatabase.txt | awk '{print $1}' > ${wdir}/list_rbs.txt
# prod
cat ${wdir}/ipdatabase.txt | awk '{print $1}' > ${wdir}/list_rbs.txt
#/opt/ericsson/ddc/util/bin/listme | grep RBS_NODE_MODEL | sed -e 's/[@=,]/ /g' | grep KIER  | awk '{print $7 " " $6 " " $4}' | sort| uniq > list_ne.txt
#GOOD
echo "getting data from NEs..."
/opt/ericsson/bin/amosbatch -p 10 -t 5 -v ip_database=${wdir}/ipdatabase.txt ${wdir}/list_rbs.txt "lt all;s+;prox;license server;license iu status;lst cell;st ret;lget . electricalAntennaTilt;q" ${wdir}/log
# prod backup
#/opt/ericsson/bin/amosbatch -p 10 -t 5 -v ip_database=${wdir}/ipdatabase.txt ${wdir}/list_rbs.txt "lt all;s+;prox;st ret;lget . electricalAntennaTilt;lst cell;alc;q" ${wdir}/log
#"lt all;license server;;q"
#command below is working
#/opt/ericsson/amos/moshell/mobatch -p 10 -t 5  ${wdir}/list_rbs.txt  "lt all;s+;prox;lst cell;st ret;lget . electricalAntennaTilt;alc;q" ${wdir}/log

#"lt all;s+;prox;lget . maxtilt;rbs;lget . mintilt;st retu;get ret ele;rbs;hget ExternalAntenna;lget aux hwid;al;rbs;license server;get licensing;rbs;get . maxtot;get . maxdl;get 0;get . numeul;get . numhs;lget . radiob;get . att;hget TpaDevice reservedBy;pmx . pmprop -m 24 -a;q"

echo "removing temporary files and caches"
cd /var/opt/ericsson/amos/moshell_logfiles/fmuser2/logs_moshell/pmfiles
rm -rf *
cd /var/opt/ericsson/amos/moshell_logfiles/fmuser2/logs_moshell/cache
rm -rf *

echo "starting first python module"
#start parsing license data
python ${wdir}/1.py 

echo "starting second python module"
#start parsing e_tilt data
python ${wdir}/2.py 

echo "finish!!!" 
echo "The script has been finished to work at" `date` >> ${wdir}/response/script_time.log

echo "creation archive of result files"
cd ${wdir}/response
tar cvf ${wdir}/rbs_data_`date +%Y-%m-%d`.tar.gz *

echo "send result via email"
cd ${wdir}/
#${wdir}/smail_test.sh rbs_data_`date +%Y-%m-%d`.tar.gz
${wdir}/smail.sh rbs_data_`date +%Y-%m-%d`.tar.gz

