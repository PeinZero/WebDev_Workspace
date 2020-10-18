from roughSpace import db,Discord

print(Discord.query.all())

searched = Discord.query.get("Mahad")
print(searched)

print(Discord.query.filter_by(name1="Elusive").all())

# db.session.delete(Discord.query.get("Mahad"))
searched = Discord.query.get("Abdullah")
searched.name2 = "WinUpdate"
db.session.add(searched)
db.session.commit()

print(Discord.query.all())
