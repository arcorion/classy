from animals import Animals

dogs = Animals("dog", 5)
dogs.shadow_report()

dogs.count = 10

result = dogs.shadow_report
result(20)

Animals.shadow_report(Animals)

cats = Animals()

cats.shadow_report()
cats.report()

Animals.report(dogs)
Animals.report(cats)
Animals.count = 100
Animals.shadow_report(Animals)
print(cats.count)