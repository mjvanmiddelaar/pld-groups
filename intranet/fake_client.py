import random


class FakeIntranetClient:
    def get_student_projects(self, student_id):
        return [{
            "id": 19,
            "score": random.randint(50, 100)
        }]

    def get_student(self, student_id):
        return [{
            "product": {
                "average": random.randint(50, 100)
            }
        }]
