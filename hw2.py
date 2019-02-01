import os, sys, json, re
import string
from xml.dom.minidom import Document

def getInfo(path):
    import_file = open('hw2_example.json')
    users_data = json.load(import_file)
    import_file.close()

    for tmp in users_data["matrix"]:
        putInfo(tmp["id"], tmp['number'], users_data['committer_name'], users_data['committer_email'])
       # print(tmp["id"], tmp['number'], tmp["result"])



def putInfo(id, number, name, mail):

    doc = Document()
    data_node = doc.createElement('data')
    doc.appendChild(data_node)

    users_node = doc.createElement('answer')
    users_node.attributes['id'] = str(id)
    data_node.appendChild(users_node)

    number_node = doc.createElement('number')
    users_node.appendChild(number_node)
    number_node.appendChild(doc.createTextNode(number))

    name_node = doc.createElement('committer_name')
    users_node.appendChild(name_node)
    name_node.appendChild(doc.createTextNode(name))

    mail_node = doc.createElement('committer_email')
    users_node.appendChild(mail_node)
    mail_node.appendChild(doc.createTextNode(mail))

    # export_file.write(doc.toprettyxml(indent="    ", encoding="utf-8"))





if __name__ == '__main__':
    export_file = open('export.xml', 'w')

    getInfo(1)
    # path_to_files = sys.argv[1]
    # path_to_result = sys.argv[2]
    export_file.close()
