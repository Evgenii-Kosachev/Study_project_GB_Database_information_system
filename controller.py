from User_Interface import user_choice
from  process import data_processor
from work_file import *

data = 'processing_model.csv'
user_list = data_processor(read_file(data), user_choice())
print(user_list)

write_file(user_list, mod='a')