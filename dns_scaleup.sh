#!/bin/sh
#hostedzone='$HOSTED_ZONE'
#replace the recorsetName and hostedzone-id with appropriate values
curl http://169.254.169.254/latest/meta-data/local-ipv4 > /home/ubuntu/instance_private_ip.txt
aws route53 list-resource-record-sets --hosted-zone-id $HOSTED_ZONE --query "ResourceRecordSets[?Name == 'route-testing.domain.com.']" > /home/ubuntu/cur_recordset.json
#download the file to /home/ubuntu from s3 or somewhere 
python /home/ubuntu/modify_recordsets.py
aws route53 change-resource-record-sets --hosted-zone-id $HOSTED_ZONE --change-batch file:///home/ubuntu/change_record_set.json

