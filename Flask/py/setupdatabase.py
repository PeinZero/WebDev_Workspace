from roughSpace import db,Discord

db.create_all()

x1 = Discord("Abdullah", "Elusive" , "Agent_1_uhh_0170")
x2 = Discord("Mahad", "Peinzero" , "BoomerMan")


db.session.add_all([x1,x2])
db.session.commit()

print(x1)
print(x2)
