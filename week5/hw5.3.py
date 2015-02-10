# There are documents for each student (student_id) across a variety of classes (class_id). Note that not all students in the same class have the same exact number of assessments. Some students have three homework assignments, etc.

# Your task is to calculate the class with the best average student performance. This involves calculating an average for each student in each class of all non-quiz assessments and then averaging those numbers to get a class average. To be clear, each student's average includes only exams and homework grades. Don't include their quiz scores in the calculation.

# What is the class_id which has the highest average student perfomance?

# Hint/Strategy: You need to group twice to solve this problem. You must figure out the GPA that each student has achieved in a class and then average those numbers to get a class average. After that, you just need to sort. The class with the lowest average is the class with class_id=2. Those students achieved a class average of 37.6
"student_id" : 0,
	"class_id" : 2,
	"scores" : [
		{
			"type" : "exam",
			"score" : 57.92947112575566
		},
		{
			"type" : "quiz",
			"score" : 21.24542588206755
		},
		{
			"type" : "homework",
			"score" : 68.1956781058743
		},
		{
			"type" : "homework",
			"score" : 67.95019716560351
		},
		{
			"type" : "homework",
			"score" : 18.81037253352722
		}


db.grades.find().pretty()

db.grades.aggregate([
  { $unwind: "$scores" },
  { $match: {$or: [ {"scores.type" : "homework"} , {"scores.type" : "exam"} ]} },
  { $group: {_id : {student_id: "$student_id", class_id: "$class_id"}, non_quizzes: {$avg: "$scores.score"} } },
  { $group: {_id : "$_id.class_id", avgScore: {$avg:"$non_quizzes"} } },
  { $sort: {avgScore : -1} }
  ])