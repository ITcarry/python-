from db.mysql import DBAction
from db.model_keys import Model

action = DBAction()
select_sql = 'select * from friend'
insert_sql = 'insert into friend values("lily", "female", "18")'
update_sql = 'UPDATE `friend` SET `age`=52 where name="xiaoming"'

print action.data_operate(insert_sql)
print action.data_inquiry_all(select_sql)

ret = action.data_inquiry_all(select_sql)
model = Model()
print model.for_json(ret)