# Exercise: Plan Scheduler
#
# Class: PlanScheduler
# 1. Properties:
# plans (a dictionary to store plans in the format {date: [list_of_tasks]})
# 2. Methods:
# add_plan(date: str, task: str): Adds a task to a specific date.
# remove_plan(date: str, task: str): Removes a task from a specific date.
# view_plans(date: str): Displays all tasks for a specific date.
# view_all_plans(): Displays all dates with their respective tasks.
#
# Task:
# 1. Create a PlanScheduler object.
# 2. Add the following tasks:
# "2025-01-10": "Python Project Submission"
# "2025-01-12": "Attend Data Science Workshop"
# 3. Remove a task: "Python Project Submission" on "2025-01-10".
# 4. Display all plans and view tasks for "2025-01-12".
class PlanScheduler:
    def __init__(self):
        self.plans={}
    def add_plan(self, date, plan):
        if date in self.plans:
            self.plans[date].append(plan)
        else:
            self.plans[date] = [plan]
        print(f'Task: "{plan}" added on Date:{date}')
    def remove_plan(self, date, plan):
        if date in self.plans:
            if plan in self.plans[date]:
                self.plans[date].remove(plan)
                print(f'\n{plan} Plan removed from Date:{date}')
        else:
            print("No plans in that specific date to remove.")
    def view_plans(self, date):
        if date in self.plans:
            c = 1
            print(f"Plans on Date - {date} :")
            print("============================")
            for i in self.plans[date]:
                print(f'{c}. {i}')
                c += 1
        else:
            print("No plans in that specific date found.")
    def view_all_plans(self):
        if len(self.plans) == 0:
            print(f"\nNo Plans on the Scheduler:")
        else:
            c1=0
            alphabet_range = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
            print(f"\nAll Plans on the Scheduler:")
            print(f"================================")
            for i in self.plans:
                print(f"{alphabet_range[c1].upper()}. Date - {i} :")
                c2 = 1
                for j in self.plans[i]:
                    print(f'    {c2}. Name :{j}')
                    c2+=1
                print()
                c1+=1
planner_obj = PlanScheduler()
planner_obj.add_plan("2025-01-10", "Python Project Submission 1")
planner_obj.add_plan("2025-01-10", "Python Project Submission 2")
planner_obj.add_plan("2025-01-10", "Python Project Submission 3")
planner_obj.add_plan("2025-01-12", "Attend Data Science Workshop 1")
planner_obj.add_plan("2025-01-14", "Attend Data Science Workshop 2")
planner_obj.add_plan("2025-01-14", "Attend Data Science Workshop 3")
planner_obj.view_all_plans()
planner_obj.view_plans("2025-01-10")
planner_obj.remove_plan("2025-01-10", "Python Project Submission 2")
planner_obj.view_all_plans()
