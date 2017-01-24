import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school  # attach to db
students = db.students

try:
    students_list = students.find({}).sort([('scores.score', pymongo.ASCENDING)])
    hw_min = sys.maxint
    for student in students_list:
        for score in student['scores']:
            if score['type'] == 'homework' and hw_min > score['score']:
                hw_min = score['score']
        if hw_min != sys.maxint:
            students.update({'_id': student['_id']}, {'$pull': {'scores': {'score': hw_min}}})
        hw_min = sys.maxint




except Exception as e:
    print "Error trying to read collection:", type(e), e

#print students_list.count()
