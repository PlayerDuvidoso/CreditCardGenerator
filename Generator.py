import random
from randomtimestamp import randomtimestamp
from datetime import datetime
from faker import Faker


class CC():
  '''Individual card info and methods.
  '''
  CCDATA = {
    'AMERICAN EXPRESS': {
      'len_num': 15,
      'len_cvv': 4,
      'pre': [34, 37],
      'remaining': 13
    },
    'discover': {
      'len_num': 16,
      'len_cvv': 3,
      'pre': [6001],
      'remaining': 12
    },
    'MASTERCARD': {
      'len_num': 16,
      'len_cvv': 3,
      'pre': [51, 55],
      'remaining': 14
    },
    'visa13': {
      'len_num': 13,
      'len_cvv': 3,
      'pre': [4],
      'remaining': 12
    },
    'VISA': {
      'len_num': 16,
      'len_cvv': 3,
      'pre': [4],
      'remaining': 15
    },    
  }

  def __init__(self):
    self.cc_type = None
    self.cc_len = None
    self.cc_num = None
    self.cc_cvv = None
    self.cc_exp = None
    self.cc_holder = None
    self.cc_prefill = []

  def generate_cc_exp(self):
    '''Generates a card expiration date that is 
    between 1 and 3 years from today. Sets `cc_exp`.
    '''
    self.cc_exp = randomtimestamp(
        start_year = datetime.now().year + 1,
        text = True,
        end_year = datetime.now().year + 3,
        start = None,
        end = None,
        pattern = "%m/%y")
    
  def generate_cc_cvv(self):
    '''Generates a type-specific CVV number.
    Sets `cc_cvv`. 
    '''
    this = []
    length = self.CCDATA[self.cc_type]['len_cvv']

    for x_ in range(length):
      this.append(random.randint(0, 9))

    self.cc_cvv = ''.join(map(str,this))

  def generate_cc_prefill(self):
    '''Generates the card's starting numbers
    and sets `cc_prefill`.
    '''
    this = self.CCDATA[self.cc_type]['pre']
    self.cc_prefill = random.choices(this)

  def generate_cc_num(self):
    '''Uses Luhn algorithm to generate a theoretically 
    valid credit card number. Sets `cc_num`. 
    ''' 
    remaining = self.CCDATA[self.cc_type]['remaining']
    working = self.cc_prefill + [random.randint(1,9) for x in range(remaining - 1)] 

    check_offset = (len(working) + 1) % 2
    check_sum = 0

    for i, n in enumerate(working):
      if (i + check_offset) % 2 == 0:
        n_ = n*2
        check_sum += n_ -9 if n_ > 9 else n_
      else:
        check_sum += n

    temp = working + [10 - (check_sum % 10)]
    self.cc_num = "".join(map(str,temp)) 
    
  def generate_cc_holder(self):
    '''Generates a random name as the card holder.
    '''
    fake = Faker()
    self.cc_holder = fake.name()

  def return_new_card(self):
    '''Returns a dictionary of card details.
    '''
    return {'cc_type': self.cc_type,
            'cc_num': self.cc_num, 
            'cc_cvv': self.cc_cvv,
            'cc_exp': self.cc_exp,
            'cc_holder': self.cc_holder}


class CCNumGen(): 
  '''Generates theoretically valid credit card numbers
  with CVV and expiration date. Prints a list of dictionaries. 
  '''
  
  card_types = ['AMERICAN EXPRESS','discover','MASTERCARD','visa13','VISA']
  
  def __init__(self, type='VISA', number=1):

    self.type = type
    self.num = number
    self.card_list = []

    new = CC()
    new.cc_type = self.type
    new.generate_cc_exp()
    new.generate_cc_cvv()
    new.generate_cc_prefill()
    new.generate_cc_num()
    new.generate_cc_holder()
    self.card_list.append(new.return_new_card())