db.zips.aggregate([
    {$match:{$or: [{state:"CA"},{state: "NY"}]}},
    {$group:{ _id:{'citt':"$city",'stato':"$state" },'popolazione':{$sum: "$pop"}}},
    {$match:{popolazione:{$gte: 25000}}},
    {$group:{ _id:"$city",'avg_pop':{$avg: "$popolazione"}}}
])