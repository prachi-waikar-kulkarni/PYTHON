# Inner Class sirf logically same classes ko together organise karne ke liye hai, they are exclusive classes.
# Inner Class can't access the variables of Outer class.
# In order to use the variable of Inner Class from the outer class
#  self.minfo = self.ManagerInfo()


class Team():  #OUTER CLASS
    def __init__(self,teamName,teamSize,Manager):
        self.teamName = teamName
        self.teamSize = teamSize
        self.manager = Manager
        self.minfo = self.ManagerInfo("Prateek",10,"Admin")

    def showdetails(self):
        print("The Team Name is",self.teamName)
        print("The Team Size is",self.teamSize)
        print("The Team Manager is",self.manager)
        self.minfo.showdetails()

    class ManagerInfo() :  #INNER CLASS
        def __init__(self,name,experience,designation):
            self.name = name
            self.experience = experience
            self.designation = designation

        def showdetails(self):
            print("The Manager Name is",self.name)
            print("The Manager Experience is",self.experience)
            print("The Manager Designation is",self.designation)

AdminTeam = Team("Admin",10,"Prateek")
AdminTeam.showdetails()
AdminManager = Team.ManagerInfo("Prachi",10,"Admin")

AdminManager.showdetails()

#print(AdminTeam.minfo.designation)

# AdminTeamManager = Team.ManagerInfo()
# AdminTeamManager.showdetails()

