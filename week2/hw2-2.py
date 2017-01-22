import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students  # attach to db
grades = db.grades

try:
    docs = grades.find({"type": "homework"}).sort([('score', pymongo.ASCENDING), ('student_id', pymongo.ASCENDING)])
    user_id = []
    for d in docs:
        if d['student_id'] not in user_id:
            user_id.append(d['student_id'])
            grades.remove(d)

except Exception as e:
    print "Error trying to read collection:", type(e), e

print grades.count()
