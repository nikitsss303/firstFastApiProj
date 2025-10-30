from app.config.database import Base, engine


Base.metadata.create_all(engine)