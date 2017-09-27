import json

#current record set is fetched from shell script dns_scaleup.sh
file_path = '/home/ubuntu/cur_recordset.json'
ip_path = '/home/ubuntu/instance_private_ip.txt'
output_file = '/home/ubuntu/change_record_set.json'

with open(file_path, 'r') as content_file:
    content = content_file.read()

with open(ip_path, 'r') as content_file:
    ip_content = content_file.read()

pre_refined_json = eval(content)[0]
pre_refined_json["ResourceRecords"].append({"Value":ip_content})

refined_json={}
refined_json["ResourceRecordSet"]=pre_refined_json
refined_json["Action"]= "UPSERT"
changes_recordsets={"Comment":"update the record set","Changes":[refined_json]}

#print changes_recordsets
final_changes=json.dumps(changes_recordsets)
f = open(output_file,'w')
print >>f, final_changes
