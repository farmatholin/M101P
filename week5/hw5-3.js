db.grades.aggregate([{$unwind: "$scores"}, {$match: {"scores.type": {$ne: "quiz"}} }, {$group: {"_id": "$class_id", "ScoreAvg": {$avg: "$scores.score"} } }, {$sort: {"ScoreAvg": -1}} ])
