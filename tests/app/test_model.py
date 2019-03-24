from app.models import User

def test_create_user(db_session):
	user = User(email="test@email.com",
				username='test_user')
	db_session.add(user)
	db_session.commit()
	users = db_session.query(User).all()
	assert len(users) == 1