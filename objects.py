import pprint

DATA = [
    {
        "company": 'Amazon', 
        "position": 'Senior Frontend Developer', 
        "posted": 1599715730, 
        "employment": 'Fulltime', 
        "location": 'USA', 
        "stack": ['frontend', 'HTML', 'CSS', 'JS', 'ReactJS']
    },
    {
        "company": 'Paypal', 
        "position": 'Junior FullStack Developer', 
        "posted": 1602318890, 
        "employment": 'Fulltime', 
        "location": 'Remote', 
        "stack": ['NodeJS', 'HTML', 'CSS', 'JS', 'ReactJS','Firebase']
    },
    {
        "company": 'Disney', 
        "position": 'Software Developer', 
        "posted": 1596875690, 
        "employment": 'Fulltime', 
        "location": 'USA', 
        "stack": ['HTML', 'CSS', 'JS', 'ReactJS',]
    },
]

#pprint.pprint(DATA)

#CRUD
newCompany = {
        "company": 'Stripe', 
        "position": 'ReactJS Developer', 
        "posted": 1602318890, 
        "employment": 'Fulltime', 
        "location": 'Remote', 
        "stack": ['NodeJS', 'HTML', 'CSS', 'JS', 'ReactJS','Firebase']
}
def create(newCompany):
    DATA.append(newCompany)


def read(company_name):
  for company in DATA:
    if company["company"] == company_name:
      return company

  return "Not Found"

def update(DATA, job_id, key, value):
    DATA[job_id][key] = value

def delete(job_id):
    DATA.pop(job_id)
