from matchers import And, HasAtLeast, PlaysIn, All, HasFewerThan, Or


class QueryBuilder:
    def __init__(self, query = All()):
        self.query_olio = query

    def build(self):
        return self.query_olio

    def playsIn(self, team):
        return QueryBuilder(And(self.query_olio, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_olio,HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_olio,HasFewerThan(value, attr)))

    def oneOf(self,m1,m2):
        return QueryBuilder(Or(m1,m2))

