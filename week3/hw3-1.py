# -*- coding: utf-8 -*-
import pymongo
# set up database
connection = pymongo.MongoClient("mongodb://localhost", safe=True)
db = connection.school
students = db.students
studentlist = students.find()
doc_size = students.count()
# loop through the database to find the lowest score of each student
for n in range(doc_size):
    student = studentlist[n]
    student_id = student['_id']
    lowest = 100
    for element in student['scores']:        
        if element['score'] < lowest and element['type']=="homework":
            lowest = element['score']
           
    del student['scores'][(student['scores'].index({
            'type' : "homework",
            'score' : lowest
        })
)]
# Update the documents by removing the lowest scores of all students in the database
    processed_scores = student['scores']
    students.update({'_id':student_id},{'$set':{'scores':processed_scores}})
