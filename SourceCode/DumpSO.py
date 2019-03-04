# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:25:13 2016
@author: MusfiqurRahman
"""


import xml.etree.ElementTree
import psycopg2, sys


data_field = ['id', 'posttypeid', 'parentid', 'acceptedanswerid', 'creationdate', 'score', 'viewcount', 'body', 'owneruserid', 'lasteditoruserid', 'lasteditordisplayname', 
              'lasteditdate', 'lastactivitydate', 'communityowneddate', 'closeddate', 'title', 'tags', 'answercount', 'commentcount', 'favoritecount']

query = ""

def prepare_query():
    global query    
    query = "INSERT INTO posts ("
    
    for i in range (0, len(data_field)):
        if i != (len(data_field) - 1):        
            query = query + str(data_field[i]) + ", "
        else:
            query = query + str(data_field[i]) + ") "
        
    query = query + 'VALUES ('
    
    for i in range (0, len(data_field)):
        if i != (len(data_field) - 1):        
            query = query + "%s, "
        else:
            query = query + "%s);"
            
def push_to_DB(data):
    global query
    
    connect_db = None
    try:
        connect_db = psycopg2.connect("dbname='StackOverflow' user='sumit'")  #put your dbname and user name
        connect_db.autocommit = True
        
        cursor = connect_db.cursor()
            
        cursor.execute(query, data)
                
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
        print '\nCould not dump data!\n'
    
    finally:
        if connect_db:
            connect_db.close() 

data_frame = []
def extract_from_XML(location_to_xml):
    i = 1
    e = xml.etree.ElementTree.parse(location_to_xml).getroot()
    for root in e.findall('row'):
        if str(root.get('Id')) != 'None':
            data_frame.append(str(root.get('Id')))
        else:
            data_frame.append(None)
        
        if str(root.get('PostTypeId')) != 'None':
            data_frame.append(str(root.get('PostTypeId')))
        else:
            data_frame.append(None)
        if str(root.get('ParentId')) != 'None':
            data_frame.append(str(root.get('ParentId')))
        else:
            data_frame.append(None)
        if str(root.get('AcceptedAnswerId')) != 'None':
            data_frame.append(str(root.get('AcceptedAnswerId')))
        else:
            data_frame.append(None)
        if str(root.get('CreationDate')) != 'None':
            data_frame.append(str(root.get('CreationDate')).replace('T', ' '))
        else:
            data_frame.append(None)
            
        if str(root.get('Score')) != 'None':
            data_frame.append(str(root.get('Score')))
        else:
            data_frame.append(None)
            
        if str(root.get('ViewCount')) != 'None':
            data_frame.append(str(root.get('ViewCount')))
        else:
            data_frame.append(None)
            
        if str(root.get('Body')) != 'None':
            data_frame.append(str(root.get('Body')))
        else:
            data_frame.append(None)

        if str(root.get('OwnerUserId')) != 'None':
            data_frame.append(str(root.get('OwnerUserId')))
        else:
            data_frame.append(None)
            
        if str(root.get('LastEditorUserId')) != 'None':
            data_frame.append(str(root.get('LastEditorUserId')))
        else:
            data_frame.append(None)
        if str(root.get('LastEditorDisplayName')) != 'None':
            data_frame.append(str(root.get('LastEditorDisplayName')))
        else:
            data_frame.append(None)
        if str(root.get('LastEditDate')) != 'None':
            data_frame.append(str(root.get('LastEditDate')).replace('T', ' '))
        else:
            data_frame.append(None)
        if str(root.get('LastActivityDate')) != 'None':
            data_frame.append(str(root.get('LastActivityDate')).replace('T', ' '))
        else:
            data_frame.append(None)
        if str(root.get('CommunityOwnedDate')) != 'None':
            data_frame.append(str(root.get('CommunityOwnedDate')).replace('T', ' '))
        else:
            data_frame.append(None)
        
        if str(root.get('ClosedDate')) != 'None':
            data_frame.append(str(root.get('ClosedDate')).replace('T', ' '))
        else:
            data_frame.append(None)
        
        if str(root.get('Title')) != 'None':
            data_frame.append(str(root.get('Title')))
        else:
            data_frame.append(None)
        
        if str(root.get('Tags')) != 'None':
            data_frame.append(str(root.get('Tags')))
        else:
            data_frame.append(None)
        
        if str(root.get('AnswerCount')) != 'None':
            data_frame.append(str(root.get('AnswerCount')))
        else:
            data_frame.append(None)
        
        if str(root.get('CommentCount')) != 'None':
            data_frame.append(str(root.get('CommentCount')))
        else:
            data_frame.append(None)
        
        if str(root.get('FavoriteCount')) != 'None':
            data_frame.append(str(root.get('FavoriteCount')))
        else:
            data_frame.append(None)
    
        print("Processing row " + str(i))
        push_to_DB(data_frame)
        print("Done")
        i = i + 1
        del data_frame[:]
        
if __name__ == '__main__':       
    prepare_query()
    extract_from_XML()
