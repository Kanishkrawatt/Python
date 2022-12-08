class person:
    def __init__(self, first_name, last_name, username, id_num):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.id_num = id_num

    def __str__(self):
        return 'First name: {}, Last name: {}, Username: {}, ID: {}'.format(self.first_name, self.last_name, self.username, self.id_num)


class student(person):
    def __init__(self, first_name, last_name, username, id_num):
        super().__init__(first_name, last_name, username, id_num)

    def __str__(self):
        return super().__str__()


class Instructor(person):
    def __init__(self, first_name, last_name, username, id_num):
        super().__init__(first_name, last_name, username, id_num)

    def __str__(self):
        return super().__str__()


class TeachingAssistant(person):
    def __init__(self, first_name, last_name, username, id_num):
        super().__init__(first_name, last_name, username, id_num)

    def __str__(self):
        return super().__str__()


class Parser:
    def __init__(self, students, instructors, tas):
        self.students = students
        self.instructors = instructors
        self.tas = tas

    def parse(self, filename):
        with open(filename) as file:
            for i in file:
                infolist = i.strip().split(",")
                if infolist[-1] == "Student":
                    self.students.append(
                        student(infolist[0], infolist[1], infolist[2], infolist[3]))
                elif infolist[-1] == "Instructor":
                    self.instructors.append(Instructor(
                        infolist[0], infolist[1], infolist[2], infolist[3]))

                elif infolist[-1] == "TA":
                    self.tas.append(TeachingAssistant(
                        infolist[0], infolist[1], infolist[2], infolist[3]))

    def get_students(self):
        return self.students

    def get_instructors(self):
        return self.instructors

    def get_tas(self):
        return self.tas

class Main:
    def __init__(self):
        self.Parser = Parser([],[],[])
    def parse_file(self,filename):
        self.Parser.parse(filename)
    def get_students(self,str1):
        return [i for i in self.Parser.get_students() if str1 in i.id_num]
    def write_to_file(self,persons,filename):
        with open(filename, "w") as file:
            for i in persons:
                infolist = i.__str__().split(", ")
                for j in infolist:
                    file.write(str(j)+"\n")
                file.write("\n")
