db.posts.aggregate([{$unwind: "$comments"},{$group: { _id: "$comments.author", "tot_comm": {$sum:1}} },{$sort:{"tot_comm":-1}}])