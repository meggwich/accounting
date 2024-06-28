from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
def main():
    get_employees()
    calculate_salary()
    print(datetime.date(datetime.today()))
if __name__ == '__main__':
    main()