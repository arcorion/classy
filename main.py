from animals import Animals

dogs = Animals("dog", 5)
dogs.report()

dogs.count = 10

result = dogs.report
result(20)

Animals.report(dogs)